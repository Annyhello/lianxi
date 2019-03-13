#coding:utf-8
import json
from convert import *

# data = { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 }
# #使用参数让 JSON 数据格式化输出
# with open("test_json.json","w") as f:
#     data1 = f.write(json.dumps(data,indent=4))
#     dump = json.loads(data1)
#     print data1
#     print dump
#json1 = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
#print(json1)
#dump = json.loads(json1)
#print dump
'''
json.dumps() 是将一个Python数据结构转换为一个JSON编码的字符串
json.loads() 是将一个JSON编码的字符串转换为一个Python数据结构
'''
a = {'name':'Tom', 'age':23}
with open("test.json", "w") as f:
    # indent 超级好用，格式化保存字典，默认为None，小于0为零个空格
    d = json.dumps(a, indent=4)
    da = f.write(d)
    print 'result:',eval(json.dumps(a))#eval()解析json
    # json.dump(a,f,indent=4)   # 和上面的效果一样
# with open("test.json", "r") as f:
#     du = json.loads(f.read().encode('utf-8'))
    du = convert(json.loads(d))
    print 'jieguo:',du