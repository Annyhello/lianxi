# coding=utf-8


import socket

s = socket.socket()
ip_port = ('127.0.0.1', 8003)

s.bind(ip_port)
s.listen(2)

while True:
    conn, addr = s.accept()
    print 'get a data from ', addr
    while True:
        data = conn.recv(1024)
        print data
        if not data:
            break

s.close()