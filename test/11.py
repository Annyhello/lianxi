#coding=utf-8

'''
def fun(x):
    global y
    y=2
    print("乘法的运行结果：",x*y)
num1=1
print("初始num1=",num1)
fun(num1)
print("y的值是：",y)
'''

a = 2
def func(y):
    print y
    dict = {'id':y}
    print dict

def func1():
    global a
    b=a+5
    a=b
    print a
    func(a)
   # global a
   #  dic={'id',3}
   #  print dic



if __name__ =='__main__':
  # func()
    func1()

