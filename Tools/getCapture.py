# coding=utf-8
import urllib2,json

#@type:
#adminlogin:后台登录
#saverecipe:发布菜谱
#savealbum:创建专辑
#savetopic:发表话题
#savediary:发表豆记
#emailreg:邮箱注册

#@ssid:
#to input session id

def getCapture(type='adminlogin',ssid=None):
    url = 'http://192.168.2.129/verifycode/%s?hdssid=%s'%(type,ssid)
    try:
        resp = urllib2.urlopen(url)
        resp = json.loads(resp.read())
    except:
        resp = {'status':False}
    if resp['status'] ==200:
        resp = resp['data']['code']
    else:
        return False
    return resp
