# -*- coding:utf-8 -*-
import time
import websocket
import json

def on_message(self, message):
        if json.loads(message)['cmd']==32:
            #print(json.loads(message)['datas'][0]['cnt'])
            pass
        print("2222222222", json.loads(message))
        if json.loads(message)['cmd']==13:
            self.send("{\"cmd\":22,\"itemid\":1,\"itemcnt\":10000}")

def on_error(self, error):
    print("error:",error)

def on_close(self):
    print("### closed ###")

def on_open(self):
        self.send("{\"cmd\":3,\"roleid\":\"1153202985413891276\"}")
        time.sleep(1)
        print("send111111")

if __name__ == "__main__":
    websocket.enableTrace(True)
    #ws = websocket.WebSocketApp("ws://yfb-h5-game.gxpan.cn:10101",on_message=on_message,on_error=on_error,on_close=on_close)
    ws = websocket.WebSocketApp("ws://192.168.143.235:10101", on_message=on_message, on_error=on_error, on_close= on_close )
    ws.on_open = on_open
    ws.run_forever
