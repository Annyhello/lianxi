 # -*- coding: utf-8 -*-
import httplib
import urllib


def sendhttp():
        data = urllib.urlencode({'spam':1,'eggs':2,'bacon':0})
        print data
        headers = {"Content-type": "text/html",  "Accept": "text/html"}
        conn = httplib.HTTPConnection('www.baidu.com')#创建一个http类型的请求链接
        conn.request('GET', '', data, headers)#发送一个请求，参数：(method, url, body, headers)
        httpres = conn.getresponse()#获取一个http响应对象，相当于执行最后的2个回车
        #print httpres.status#当次请求的状态
        #print httpres.reason#当次请求的结果的表述内容，200是ok，404是Not Found
        print httpres.read()#获得http响应的内容部分，即网页源码
        conn.close()


if __name__ == '__main__':
    sendhttp()