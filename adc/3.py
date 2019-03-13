#! /usr/bin/env python
# -*- coding:utf-8 -*-


# import time
# from websocket import create_connection
# ws = create_connection("ws://192.168.143.235:10101")
# print("Sending 'Hello, World'...")
# for i in range(1, 2):
#     time.sleep(1)
#     ws.send("Hello, World %s" % i)
#     print("Sent %s",  i)
#     print("Reeiving...%s",  i)
#     result = ws.recv()
#     print("Received '%s'" % result)
# time.sleep(30)
# ws.close()


import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://echo.websocket.org/",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()