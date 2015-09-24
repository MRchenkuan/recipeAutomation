# coding=utf-8
from urlconsister import consistUrl,consistData
import  urllib,urllib2,cookielib
cookie = cookielib.CookieJar()
openner = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))


host = 'http://api.hoto.cn/index.php'
query = {
    'appid': '4',
    'appkey': '573bbd2fbd1a6bac082ff4727d952ba3',
    'channel': 'appstore',
    'deviceid': '0f607264fc6318a92b9e13c65db7cd3c%7C9C1AC02E-D531-485C-B717-D2F95C9F78B1%7C286FB2FF-BDFA-487A-ABA0-504131EF1400',
    'format': 'json',
    'method': 'Recipephoto.photoReport',
    'nonce': '1431659275',
    'sessionid': '1431651637',
    'signmethod': 'md5',
    'timestamp': '1431659275',
    'v': '2',
    'vc': '36',
    'vn': 'v4.10.0',

    'uuid': '1f6803b1f672597397ddeb1210974030',
    'appsign': 'a81b3667efac2aee6eca71c3297a25f9',
    'loguid': '4041054'
}
data = {
    'content': u'from automation',
    'id': '1203130',
    'sign': '04ebba0c37d4b834c851dfcc9634edef',
    'type': '1',
    'uid': '4041054',
    'uuid': '1f6803b1f672597397ddeb1210974030'
}

cookies = {
    'PHPSESSID	':'63e7347ddd864e06fbabfbdec48ea02e'
}

headers = {
}

url = consistUrl(host, query)
openner.addheaders=headers.items()+cookies.items()






# 举报测试
users = [
    # 普通用户举报
    ('04ebba0c37d4b834c851dfcc9634edef',4041379,'1f6803b1f672597397ddeb1210974030'),
    # 白名单用户举报
    ('04ebba0c37d4b834c851dfcc9634edef',4041054,'1f6803b1f672597397ddeb1210974030'),
    ('04ebba0c37d4b834c851dfcc9634edef',4040919,'1f6803b1f672597397ddeb1210974030')
]


data['id']=1202066
data['sign'] = users[1][0]
data['uid'] = users[1][1]
data['uuid'] = None#users[1][2]
req = urllib2.Request(url=url,headers=headers,data=consistData(data))
response = openner.open(req).read()

print response


