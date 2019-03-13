import httplib, urllib
params = urllib.urlencode({'spam':1,'eggs':2,'bacon':0})
print params
headers = {"Content-type": "text/html",  "Accept": "text/html"}
conn = httplib.HTTPConnection("www.baidu.com")
conn.request("GET", "", params, headers)
response = conn.getresponse()
data = response.read()
print data
conn.close()