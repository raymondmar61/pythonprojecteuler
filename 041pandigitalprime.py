#https://projecteuler.net/problem=41 Pandigital prime
#https://projecteuler.net/thread=41
#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#What is the largest n-digit pandigital prime that exists?
#RM:  start backward count from 987,654,321 because we're looking for the largest.  

import time
startime = time.time()
def checkifprime(n): #n must be greater than one
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	i = 3
	while i * i <= n:
		if n % i == 0:
			return False
		i += 2
	return True

largestpandigital = 0
#start 987654321+2 because subtract 2 immediately in while loop
integerstart = 987654323
pandigitallistkey = ['1','2','3','4','5','6','7','8','9']
#while loop stops when largestpandigital is found
while largestpandigital == 0:
	integerstart -= 2
	pandigitallist = []
	#convert number to string
	integerstartstring = str(integerstart)
	integerstartstringlength = len(integerstartstring)
	#pandigital numbers contain no zeros
	if "0" in integerstartstring:
		continue
	for eachlength in range(0,integerstartstringlength):
		pandigitallist.append(integerstartstring[eachlength])
	pandigitallist.sort()
	#if number contains digits 1 to n exactly once, check if number is prime
	if pandigitallist == pandigitallistkey[0:integerstartstringlength]:
		if checkifprime(integerstart) is True:
			largestpandigital = integerstart
print(largestpandigital) #print 7652413
endtime = time.time()
print((endtime-startime),"seconds")
print((round(endtime-startime)),"seconds") #print 728 seconds
