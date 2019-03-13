import websocket
import json

try:
    import thread
except ImportError:
    import _thread as thread
import time

g_ws = None
g_count = 0
g_dict = {}

#on_message方法在连接接收到新的消息时被调用
def on_message(ws, message):
    #    print(message)
    ms = json.loads(message)
    if ms["cmd"] == 32:
        print('32:')
        return
    print(ms)

    global g_count
    if ms["cmd"] == 35:
        if ms["diaid"] in g_dict:
            g_dict[ms["diaid"]] = g_dict[ms["diaid"]] + 1
        else:
            g_dict[ms["diaid"]] = 1

    g_count = g_count + 1
    if (g_count % 100) == 0:
        time.sleep(1)

    if g_count < 101:
        g_ws.send("{\"cmd\":25}")
        print("send 25:")
    #        time.sleep(0.01)
    else:
        print("g_count:", g_count)
        print(g_dict)

def on_error(ws, error):
    print(error)

#on_close方法在客户端关闭时被调用
def on_close(ws):
    print("### closed ###")

#open方法在一个新的WebSocket连接打开时被调用
def on_open(ws):
    ws.send("{\"cmd\":3, \"roleid\":281480806154252}")
    time.sleep(1)
    print('send 3:')

if __name__ == "__main__":
    websocket.enableTrace(True)#打开跟踪，查看日志
    g_ws = websocket.WebSocketApp("ws://192.168.143.235:10101",
                                  on_message=on_message,
                                  on_error=on_error,
                                  on_close=on_close)
    g_ws.on_open = on_open
    g_ws.run_forever()

'''
(1)on_open:在建立Websocket握手时调用的可调用对象,这个方法只有一个参数,就是该类本身。

(2)on_message:这个对象在接收到服务器返回的消息时调用。有两个参数,一个是该类本身,一个是我们从服务器获取的字符串(utf-8格式)。

(3)on_error:这个对象在遇到错误时调用,有两个参数,第一个是该类本身,第二个是异常对象。

(4)on_close:在遇到连接关闭的情况时调用,参数只有一个,就是该类本身。

(5)Run_forever是一个无限循环,只要这个websocket连接未断开,这个循环就会一直进行下去
'''
