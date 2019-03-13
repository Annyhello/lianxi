import logging

"""方法一"""
# def use_logging(func):
#
#     def wrapper():
#         logging.warning("%s is running" % func.__name__)
#         return func()   # 把foo当做参数传递进来时，执行func()就相当于执行foo()
#     return wrapper
#
#
# def foo():
#     print('i am foo')
#
#
# foo = use_logging(foo)  # 因为装饰器 use_logging(foo) 返回的时函数对象 wrapper，这条语句相当于  foo = wrapper
# foo()# 执行foo()就相当于执行 wrapper()

'''
    方法二
    装饰器在 Python 使用如此方便都要归因于 Python 的函数能像普通的对象一样能作为参数传递给其他函数，可以被赋值给其他变量，可以作为返回值，可以被定义在另外一个函数内
'''
def use_logging(func):
    def wrapper():
        logging.warning("%s is running" % func.__name__)
        return func()
    return wrapper

@use_logging
def foo():
    print("i am foo")

foo()

