#coding=utf-8
'''
解决python中json模块loads出来的结构都是unicode的问题
iteritems()返回一个迭代器
items函数，将一个字典以列表的形式返回，因为字典是无序的，所以返回的列表也是无序的。
'''

def convert(input):
    if isinstance(input, dict):
        return {convert(key): convert(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, str):
        return input.encode('utf-8')
    else:
        return input