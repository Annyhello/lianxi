import httplib, urllib2
import ssl
# params = urllib2.urlencode({'spam':1,'eggs':2,'bacon':0})
# print params
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
url = 'https://www.python.org/'
req = urllib2.Request(url,headers = headers)
context = ssl._create_unverified_context()
content = urllib2.urlopen(req,context=context).read()
print content.decode('u8')