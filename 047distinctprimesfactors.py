#https://projecteuler.net/problem=47 Distinct primes factors
#https://projecteuler.net/thread=47
#The first two consecutive numbers to have two distinct prime factors are:
#14 = 2 × 7
#15 = 3 × 5
#The first three consecutive numbers to have three distinct prime factors are:
#644 = 2^2 × 7 × 23 or 2 x 2 x 7 x 23
#645 = 3 × 5 × 43
#646 = 2 × 17 × 19.
#Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?  Find four consecutive numbers containing containing four distinct prime factors.
from collections import defaultdict
import time
startime = time.clock()

#function calculate prime factors
#https://stackoverflow.com/questions/27628898/prime-factorization-algorithm
def ffs(num):
    factors = defaultdict(lambda: 0)
    n = 2
    while num != 1:
        while num % n == 0:
            factors[n] += 1
            num /= n
        n += 1
    return dict(factors)

#while loop check integers starting at intergerstart.  If counter greater than consecutivecouner, then found the first consecutive integer with distinct prime factors.
intergerstart = 1000
consecutivecounter = distinctprimefactors = 4
counter = 0
while counter < consecutivecounter:
	#add one to counter when integer contains distinctprimefactors count
	if len(ffs(intergerstart)) == distinctprimefactors:
		counter += 1
	else:
		counter = 0
	intergerstart += 1
print(intergerstart-distinctprimefactors) #print 134043

endtime = time.clock()
print((endtime-startime),"seconds") #print 140.01641999999998 seconds
print((round(endtime-startime)),"seconds") #print 140 seconds