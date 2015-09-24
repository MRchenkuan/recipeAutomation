# coding=utf-8
import cookielib,urllib,random
from urllib2 import build_opener,Request,HTTPCookieProcessor,URLError

'''
    此部分为浏览指定帖子的方法
'''
opener = build_opener(HTTPCookieProcessor(cookielib.CookieJar()))
recipids = range(330356,330396)


succeselist = []
succeseCount =0
i=0

for i in range(1,4500):
    recipid = random.choice(recipids)
    rescode=0
    res=None
    try:
        res = opener.open(Request('http://group.haodou.com/topic-%s.html'%recipid))
        rescode = 200
        succeseCount+=1
    except URLError as e:
        if hasattr(e,'code'):
            rescode = e.code
        elif hasattr(e,'reason'):
            rescode = e.reason
    finally:
        print i,'complete,',recipid,'resp:',rescode
        if res :
            res.close()
    i+=1


print 'succese:\n',succeseCount