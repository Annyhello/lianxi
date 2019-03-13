#!/usr/bin/python
# coding=utf-8

import socket
host_name = socket.gethostname()#获取hostname
print host_name
ip_address = socket.gethostbyname(host_name)
print ip_address#获取主机IP
print socket.gethostbyaddr('172.31.187.13')