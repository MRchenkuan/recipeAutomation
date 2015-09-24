# coding=utf-8
def consistUrl(host,query):
    _templist = []
    for k,v in query.items():
        _templist.append(u'%s=%s'%(k,v))
    return u'%s?%s'%(host,'&'.join(_templist))

def consistData(data):
    _templist = []
    for k,v in data.items():
        _templist.append(u'%s=%s'%(k,v))
    return u'&'.join(_templist)