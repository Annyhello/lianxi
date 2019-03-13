#!/usr/bin/env python
# _*_ coding:utf-8 _*_


import socket
#cd learn/sockettest/socket_test
# 阻塞式
sk = socket.socket()
ip_port = ('127.0.0.1', 8003)

sk.bind(ip_port)
sk.listen(2)

while True:
    conn, addr = sk.accept()
    print 'get a data from ', addr
    while True:
        data = conn.recv(1024)
        print 'recevie:', data

        if not data: break
        conn.send(data.upper())

    break
sk.close()