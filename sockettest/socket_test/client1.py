#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import socket

ip_port = ('127.0.0.1', 8003)
sk = socket.socket()
sk.connect(ip_port)

while True:
    input_data = raw_input('')
    print 'hjdfhjkh'
    sk.send(input_data)
    print 'aaaaaaaaa'
    data = sk.recv(1024)
    print 'recevi:', data

sk.close()