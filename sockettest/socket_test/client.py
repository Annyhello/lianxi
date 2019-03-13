from socket import *

s=socket(AF_INET,SOCK_STREAM)
s.connect(('127.0.0.1',8003))
print 'server->client :',s.recv(1024)

s.send('hi,i am client')

s1=socket(AF_INET,SOCK_STREAM)
s1.connect(('127.0.0.1',8003))
print 's2:',s1.recv(512)
s1.send('client send use sock2')
s1.close()
s.close()