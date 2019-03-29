# coding=utf-8

import http.client, urllib
import json
from lianxi import convert
import sys

p=198
def  clientReq(p):
    httpClient = None
    global y
    try:
        data = {"d" : ('{"itemPeriodId":"2018-06-28-12:00:00_1_Molunga_2_2_card_825","bidPrice":%d,"priceType":"d"}')%p, "t" :'f8dc3e3fff822b86c6d320b7c77dbe50',"seq" : 51,"rseq":51}
        #{"itemPeriodId":"2018-06-26-00:00:00_1_Molunga_2_2_card_221","bidPrice":180,"priceType":"d"}
        params = urllib.urlencode(data)
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept-Encoding":"gzip"}

        httpClient = http.client.HTTPConnection('192.168.5.111', 8590, timeout=30)
        httpClient.request("POST", "/transfer/bid", params, headers)
        response = httpClient.getresponse()
        result = response.read()
        print(response.msg)
        print(response.status)
        print(response.reason)
        print("result:",type(result))#字符串
        print(result)

        js =json.dumps(result)
        print(str(sys._getframe().f_lineno)+"        " +"js:", type(js))#字符串
        jsonData = json.loads(js,encoding='UTF-8')
        j = convert.convert(json.loads(jsonData))
        print(str(sys._getframe().f_lineno)+"        " +"jsonData:", type(j))#字典
        print(str(sys._getframe().f_lineno)+"        " +"jsonData:",j)
        if j.get('d'):
            x = j.get('d')
            print(x)#与40行值输出一样
            print(str(sys._getframe().f_lineno)+"        " +"d:",type(x))#字典
            print(str(sys._getframe().f_lineno)+"        " +"d:",j['d'])
            print(str(sys._getframe().f_lineno)+"        " +"d:",type(j['d']))#字典
            y = j['d']['list'][0]['bidPrice']
            print(str(sys._getframe().f_lineno)+"        " +'bidPrice:',y)
            print(type(y))#int
            return y
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()

def fun():
    global p
    #print sys._getframe().f_lineno+"        " +p
    y = clientReq(p)
    print('fghkjghdfgk:',y)
    z = clientReq(y)
    print(z)

if __name__ =='__main__':
    fun()

    '''
              print  type(y)#字典
              list = y['list'] 
              #list1 =list
              dict2 =list
              print type(dict2)#列表
              print "list:", dict2
              list2 = dict2[0]
              print list2
              list3 =list2
              print type(list3)#字典
              bidPrice = list3['bidPrice']
              print 'bidPrice:',bidPrice
              #for key in :
                  #if key=='bidPrice':
                      #break
                      #print list3[key]
              '''