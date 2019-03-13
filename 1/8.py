# # coding=utf-8
# import math
# #
# #
# def area_of_circle(x):
#     s = math.pi*x*x
#     return s
# print area_of_circle(2)
#
#
# if __name__ == '__main__':
#     area_of_circle(2)

#11+22+33+……+100100

# def calc_num(n: int):
#     if n<10:
#         return n*11
#     elif n<100:
#         return n*101
#     elif n<1000:
#         return n*1001
#     else:
#         raise ValueError('数值过大，请输入小于1000的数值')
#
# L=[]
# for i in range(1,101):
#     L.append(calc_num(i))
# print(L)
# print(sum(L))

# def move(n, a, b, c):
#     if n==1:
#         print(a,"-->",c)
#     else:
#         move(n-1,a,c,b)
#
#         move(1,a,b,c)
#
#         move(n-1,b,a,c)
#
# move(2, 'A', 'B', 'C')


# L = ['Adam', 'Lisa', 'Bart', 'Paul']
# for t in enumerate(L):
#     index = t[0]
#     name = t[1]
#     print(index, '-', name)


# L = []
# x = 1
# while x <= 100:
#     L.append(x*x*10+x)
#     print L
#     x = x + 1
# print sum(L)

# a = 'python'
# print 'hello,', a or 'world'
#
# b = ''
# print 'hello,', b or 'world'
#
# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     for y in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
#         if x < y:
#             print x * 10 + y


# def is_not_empty(s):
#     return s and len(s.strip()) > 0

# y = filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])
# x =list(y)
# print(x)


import math

def is_sqr(x):
    r = int(math.sqrt(x))
    if r * r == x:
        return r*r

print(list(filter(is_sqr, range(1, 101))))

