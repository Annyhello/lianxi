#!/usr/bin/python
import httplib

conn = httplib.HTTPConnection("www.csdn.net")
conn.request("GET", "/")
r1 = conn.getresponse()

print 'status:',r1.status, 'reason:',r1.reason
print '-' * 40

headers = r1.getheaders()
for h in headers:
    print h
print '-' * 40

print r1.msg