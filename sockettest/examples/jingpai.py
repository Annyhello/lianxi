#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import socket
import json
# from sockettest.examples import transfer_pb2

ip_port = ('192.168.5.111', 8590)
s = socket.socket()
s.connect(ip_port)


data={
    "d":{
        "itemPeriodId":"2018-06-15-12:00:00_1_Alafont_1_1_card_123",
        "bidPrice":80,
        "priceType":"d"
    },
    "t":"f8dc3e3fff822b86c6d320b7c77dbe50",
    "seq":27,
    "rseq":27
}

# 对数据进行序列化（封包）
dat = json.dumps(data,indent=4)
s.send(dat)
da = s.recv(1024)
print(da)
# resDat = json.loads(dat)
# print resDat
# bidPrice = resDat.get("bidPrice")
# print bidPrice

