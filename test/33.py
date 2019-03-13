# b =139
# a=('hello " %d"world ')%b
# print a


# p = 123
# a = {"d" :( '{"aa":"sss","bb":%d,"cc":"d"}')%p, "t" :'1234'}
# print a
p = 189
def A(p):
    data = {"d": ('{"itemPeriodId":"2018-06-22-12:00:00_1_Molunga_2_2_card_324","bidPrice":%d,"priceType":"d"}') % p,
    "t": 'f8dc3e3fff822b86c6d320b7c77dbe50', "seq": 19, "rseq": 19}
    print '11111111',data
    y = p+1
    print  '22222222',y
    return y

# A(p)
def B():
    global  p
    print  '33333333',p

    y = A(p)
    print '4444444',y
    # p=y
    # print '5555555',p
    z=A(y)
    print '6666666', z
    A(z)


B()
# if __name__ =='__main__':
#     B()