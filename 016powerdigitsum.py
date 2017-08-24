#https://projecteuler.net/problem=16 Power digit sum
#https://projecteuler.net/thread=16
#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2^1000?

import math

print(math.pow(2,15)) #print 32768.0
powersum = str(math.pow(2,15))
for eachpowersum in powersum:
	print(eachpowersum)

powersum = str((2**1000))
powersum = list(map(int,powersum))
print(powersum)
digitssum = 0
for eachpowersum in powersum:
	digitssum = digitssum + eachpowersum
print(digitssum) #answer is 1366

#easy solution from the thread
# sum = 0
# for n in str(2**1000):
# 	sum += int(n)
# print sum