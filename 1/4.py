import httplib
BODY = "***filecontents***"
conn = httplib.HTTPConnection("localhost", 8080)
conn.request("PUT", "/file", BODY)
response = conn.getresponse()
print response.status, response.reason