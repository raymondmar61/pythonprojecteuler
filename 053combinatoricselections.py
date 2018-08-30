#https://projecteuler.net/problem=53 Combinatoric selections
#https://projecteuler.net/thread=53
#There are exactly ten ways of selecting three from five, 12345:  123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#In combinatorics, we use the notation, 5C3 = 10.
#In general, nCr = (n!)/(r!(n−r)!), where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
#It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
#How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?

import time
from math import factorial
startime = time.clock()

#https://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python
def nCr(n,r):
    f = factorial
    return f(n) // f(r) // f(n-r)

valuesgreater1m = 0
for eachn in range(1,101):
    for eachr in range(1,eachn+1):
        if nCr(eachn,eachr) > 1000000:
            valuesgreater1m += 1
print(valuesgreater1m) #print 4075

endtime = time.clock()
print((endtime-startime),"seconds") #print 0.009357999999999998 seconds
print((round(endtime-startime)),"seconds") #print 0 seconds

