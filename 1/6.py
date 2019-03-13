#!/usr/bin/python



sum =0
def getMaxandMin():
    global  sum
    for i in range(3,100):
        if(i%2!=0):
            sum = sum +i
            print i
    print sum
getMaxandMin()