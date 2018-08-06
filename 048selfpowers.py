#https://projecteuler.net/problem=48 Self Powers
#https://projecteuler.net/thread=48
#The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
import time
startime = time.clock()
# n = 1
# sum = 0
# while n <1001:
#     sum += n**n
#     n+=1
# print(str(sum)[-10:])  #print 9110846700
# endtime = time.clock()
# print((endtime-startime),"seconds") #print 0.010152000000000001 seconds
# print((round(endtime-startime)),"seconds") #print 0 seconds

#The count iterator will return evenly spaced values starting with the number you pass in as its start parameter. Count also accept a step parameter.  count(start=0,step=1).  RM:  =number is default
from itertools import count
sum = 0
for i in count(1):
    if i == 1001:
        break
    else:
        sum += i**i
print(str(sum)[-10:])  #print 9110846700
endtime = time.clock()
print((endtime-startime),"seconds") #print 0.009283 seconds
print((round(endtime-startime)),"seconds") #print 0 seconds