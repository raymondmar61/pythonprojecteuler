#https://projecteuler.net/problem=56 Powerful digit sum
#https://projecteuler.net/thread=56
#A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
#Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?

import time
from math import factorial
startime = time.clock()

maximumdigitalsum = 0
for a in range(1,101):
	for b in range(1,101):
		massivenumber = a**b
		#convert massive number to string to sum its digits
		massivenumberstring = str(massivenumber)
		thesum = 0
		#for loop sum massive number digits
		for eachmassivenumberstring in massivenumberstring:
			thesum = thesum + int(eachmassivenumberstring)
			if thesum > maximumdigitalsum:
				maximumdigitalsum = thesum
print("Maximum Digital Sum is {}".format(maximumdigitalsum)) #print Maximum Digital Sum is 972

endtime = time.clock()
print((endtime-startime),"seconds") #print 0.260007 seconds
print((round(endtime-startime)),"seconds") #print 0 seconds