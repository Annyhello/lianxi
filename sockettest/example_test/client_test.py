#! /usr/bin/env python
#coding=utf-8

import socket
# import sys
# import os
# os.chdir("..")
# sys.path.append(os.getcwd())
from sockettest.example_test import test_pb_pb2

'''
1、client封包SerializeToString()
2、client->APIserver：发包send（）
APIserver：1、得到数据2、解包数据3、处理数据4、打包回包数据5、回包给请求数
3、APIserver->client：回包recv（）
4、client解包ParseFromString()
'''
'''
stu1 = test_pb_pb2.all_student()
stu2 =
stu.id=1001
stu.name = 'anny'
stu.age = 20

ip_port = ('127.0.0.1', 8003)
s = socket.socket()
s.connect(ip_port)
'''
s.send()
data = s.recv(1024)
print 'recevie:', data

s.close()
