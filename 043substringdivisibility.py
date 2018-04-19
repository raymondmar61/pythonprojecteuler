#https://projecteuler.net/problem=43 Sub-string divisibility
#https://projecteuler.net/thread=43
#The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
#Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#d2d3d4=406 is divisible by 2 123
#d3d4d5=063 is divisible by 3 234
#d4d5d6=635 is divisible by 5 345
#d5d6d7=357 is divisible by 7 456
#d6d7d8=572 is divisible by 11 567
#d7d8d9=728 is divisible by 13 678
#d8d9d10=289 is divisible by 17 789
#Find the sum of all 0 to 9 pandigital numbers with this property.
#RM:  Find pandigital numbers between 012345679 and 987654321 with the divisibility property.  Add these numbers.
from itertools import permutations
from time import time
startime = time()
pandigitalanswer = []

pandigitalnumber = "0123456789"
pandigitallist = list(map(str,pandigitalnumber))
#calculate all pandigital numbers from pandigitallist.  Check each pandigital10 with divisibility property.  If true, add pandigital10 to pandigitalanswer.
for pandigital10 in permutations(pandigitallist, 10):
	if int(pandigital10[1]+pandigital10[2]+pandigital10[3]) % 2 == 0 and int(pandigital10[2]+pandigital10[3]+pandigital10[4]) % 3 == 0 and int(pandigital10[3]+pandigital10[4]+pandigital10[5]) % 5 == 0 and int(pandigital10[4]+pandigital10[5]+pandigital10[6]) % 7 == 0 and int(pandigital10[5]+pandigital10[6]+pandigital10[7]) % 11 == 0 and int(pandigital10[6]+pandigital10[7]+pandigital10[8]) % 13 == 0 and int(pandigital10[7]+pandigital10[8]+pandigital10[9]) % 17 == 0:
		pandigitalanswer.append("".join(map(str,pandigital10)))
#convert pandigitalanswer numbers to integer and add
print(sum(list(map(int, pandigitalanswer)))) #print 16695334890

endtime = time()
print((endtime-startime),"seconds") #print 2.6239845752716064 seconds
print((round(endtime-startime)),"seconds") #print 3 seconds