# class A:
#     def add(self, x):
#         y = x + 1
#         print(y)
#
#
# class B(A):
#     def add(self, x):
#         super().add(x)
#
#
# b = B()
# b.add(2)


# # !/usr/bin/python
# # -*- coding: UTF-8 -*-
#
# class A(object):  # Python2.x 记得继承 object
#     def add(self, x):
#         y = x + 1
#         print(y)
#
#
# class B(A):
#     def add(self, x):
#         super(B, self).add(x)
#
#
# b = B()
# b.add(2)  # 3


# def add(n, i):
#     return n + i
#
#
# def test():
#     for i in range(4):
#         yield i
#         print(i)
#
#
# g = test()
# for n in [1, 10, 5]:
#     g = (add(n, i) for i in g)
# print(list(g))

x = 1
y = 2
def add (x, y):
    z = x + y
    return z
print(add(x,y))


# x = 1
# y = 2
# def add (x, y):
#     z = x + y
#     print(z)
# print(add(x,y))


