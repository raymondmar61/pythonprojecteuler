#https://projecteuler.net/problem=5 Smallest multiple
#https://projecteuler.net/thread=4
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.  What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math
# WTF am I thinking!?!  The for loop I created doesn't answer the question.
# for eacha in reversed(range(2,11)):
# 	for eachb in reversed(range(2,11)):
# 		smallnumber = eacha * eachb
# 		print(eacha,"/",eachb, (eacha/eachb), math.fmod(eacha,eachb))

# for smallest in range(1,2521):
# 	for eachnumber in reversed(range(1,11)):
# 		if math.fmod(smallest,eachnumber) == 0.0:
# 			print(smallest, "is divisible by", eachnumber)
# 		else:
# 			break

smallest = 20
maxdivisible = smallest
counter = 0
while counter < maxdivisible:
	for eachnumber in reversed(range(1,maxdivisible+1)):
		if math.fmod(smallest,eachnumber) == 0.0:
			#print(smallest, "is divisible by", eachnumber)
			counter += 1
		else:
			counter = 0
			break
		smallest +=20
print(smallest) #for 1 to 5 answer is 60, for 1 to 10, answer is 2520, for 1 to 20, answer is 232792560
print(counter)
