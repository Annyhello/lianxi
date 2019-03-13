import httplib
conn = httplib.HTTPSConnection("www.baidu.com")
conn.request("HEAD","/")
res = conn.getresponse()
print res.status, res.reason

data = res.read()
print len(data)
data == ''
