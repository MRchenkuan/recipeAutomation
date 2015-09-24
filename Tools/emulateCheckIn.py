# coding=utf-8
import MySQLdb
from datetime import *
import time

#初始化签到列表
def makeDateList(stadate,entdate,exceptlist):
    datelist = []
    serisday = 0
    sdate = datetime.strptime(stadate,'%Y-%m-%d')
    edate = datetime.strptime(entdate,'%Y-%m-%d')
    for i in xrange(0,((edate-sdate).days+1)):
        elem = str(sdate + timedelta(days=i))[:10]
        if elem in exceptlist:
            serisday = 0
        else:
            datelist.append(elem)
            serisday+=1
    return {'datelist':datelist,'serisday':serisday}



def checkIn(userid,stadate,entdate,exceptlist=[]):
    #连接db
    conn = MySQLdb.connect(host="192.168.1.243", user="haodou_test", passwd="dbpasswd",charset='utf8')
    cursor = conn.cursor()

    #算表
    cursor.execute("select hex(%s%%256);"%userid)
    userTableId = cursor.fetchone()[0].lower()

    #清签到日志
    cursor.execute("DELETE FROM haodou_checkin.CheckInLog WHERE UserId = %s;"%userid)
    cursor.execute("DELETE FROM haodou_checkin.CheckInLog_%s WHERE UserId = %s;"%(userTableId,userid))
    cursor.execute("select * FROM haodou_checkin.CheckInLog_%s WHERE UserId = %s;"%(userTableId,userid))

    #清财富和经验日志
    today = time.strftime('%Y-%m-%d',time.localtime(time.time()))

    cursor.execute("DELETE FROM haodou_wealthlog.UserWealthLog_%s WHERE UserId = %s AND Type = 405 AND DATE(CreateTime) = '%s';"%(userTableId,userid,today))
    cursor.execute("DELETE FROM haodou_explog.UserExpLog_%s WHERE UserId = %s AND Type = 405 AND DATE(CreateTime) = '%s';"%(userTableId,userid,today))
    cursor.execute("select * FROM haodou_explog.UserExpLog_%s WHERE UserId = %s AND Type = 405 AND DATE(CreateTime) = '%s';"%(userTableId,userid,today))

    #然后开始插入
    datelist = makeDateList(stadate,entdate,exceptlist)
    for date in datelist['datelist']:
        print date
        #conn.select_db('haodou_checkin')
        #cursor = conn.cursor()
        cursor.execute("INSERT INTO haodou_checkin.CheckInLog(UserId, CreateTime, CreateDateTime) VALUES(%s, '%s', '%s');"%(userid,date,date))
        cursor.execute("INSERT INTO haodou_checkin.CheckInLog_%s(UserId, CreateTime, CreateDateTime) VALUES(%s, '%s', '%s');"%(userTableId,userid,date,date))
    #最后设置连续签到天数
    cursor.execute("UPDATE recipe_user.User SET SignNum = %s,SignTime = '%s' WHERE UserId = %s;"%(datelist['serisday'],datelist['datelist'][-1],userid))
    cursor.execute("UPDATE recipe_user.User_%s SET SignNum = %s,SignTime = '%s' WHERE UserId = %s;"%(userTableId,datelist['serisday'],datelist['datelist'][-1],userid))
    cursor.execute("UPDATE haodou_center.UserSignPrizeLog SET LastSignDate = '%s',PrizePeriodDays = %s WHERE UserId = %s;"%(datelist['datelist'][-1],datelist['serisday'],userid))
    print("UPDATE haodou_center.UserSignPrizeLog SET LastSignDate = '%s',PrizePeriodDays = %s WHERE UserId = %s;"%(datelist['datelist'][-1],datelist['serisday'],userid))
    cursor.execute("commit")
    cursor.close()
    conn.close()
    print datelist