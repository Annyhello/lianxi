# coding=utf-8
from socket import *

s=socket(AF_INET,SOCK_STREAM)
s.bind(('127.0.0.1',8003))
s.listen(5)
while 1:
    q,v = s.accept()
    print q
    q.send('hi,i am server')
    ra=q.recv(512)
    print 'client->server :',ra
    if not ra:
        print("连接已断开")
        break
q.close()