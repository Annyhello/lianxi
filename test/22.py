# coding=utf-8

import httplib, urllib
import json
from sockettest import convert,excel

p=198
def  clientReq(p):
    httpClient = None
    global y
    try:
        data = {"d" : ('{"itemPeriodId":"2018-06-28-12:00:00_1_Molunga_2_2_card_825","bidPrice":%d,"priceType":"d"}')%p, "t" :'f8dc3e3fff822b86c6d320b7c77dbe50',"seq" : 51,"rseq":51}
        params = urllib.urlencode(data)
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept-Encoding":"gzip"}
        httpClient = httplib.HTTPConnection('192.168.5.111', 8590, timeout=30)
        httpClient.request("POST", "/transfer/bid", params, headers)
        response = httpClient.getresponse()
        result = response.read()
        js =json.dumps(result)
        jsonData = json.loads(js,encoding='UTF-8')
        j = convert.convert(json.loads(jsonData))
        if j.get('d'):
            y = j['d']['list'][0]['bidPrice']
            return y
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()

def fun():
    global p
    y = clientReq(p)
    print y
    z = clientReq(y)
    print z

if __name__ =='__main__':
    fun()