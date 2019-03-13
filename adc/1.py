# -*- coding:utf-8 -*-

import time
import websocket as ws
import json


def Random():
    w = ws.create_connection("ws://192.168.143.235:10101")
    data = {'cmd':3,'roleid':281480806154252}
    msg = json.dumps(data)
    w.send(msg)
    result = w.recv()
    print('111111:', result)
    time.sleep(1)
    for i in range(2):
        data1 = {'cmd': 25}
        msg1 = json.dumps(data1)
        w.send(msg1)
        result1 = w.recv()
        if(json.loads(result1)['cmd']==35):
            print('333333 diaid:',json.loads(result1)['diaid'])
        if (json.loads(result1)['cmd'] == 32):
            print('4444444 cnt:', json.loads(result1)['datas'][0]['cnt'])
    time.sleep(1)
    w.close()


if __name__ == "__main__":
    Random()
