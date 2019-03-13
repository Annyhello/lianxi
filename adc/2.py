# -*- coding:utf-8 -*-


import time
import websocket
import json
# from threading import Thread

count =1
def on_message(self, message):
        if json.loads(message)['cmd']==32:
            return
        print("2222222222", json.loads(message))

        global count
        if count<3:
            self.send("{\"cmd\":25}")
        else:
            print("count:", count)
        count = count+1

def on_error(self, error):
    print("error:",error)


def on_close(self):
    print("### closed ###")


def on_open(self):
        self.send("{\"cmd\":3,\"roleid\":281480806154252}")
        time.sleep(1)
        print("send111111")


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://192.168.143.235:10101",on_message=on_message,on_error=on_error,on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
