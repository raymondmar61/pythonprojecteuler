#https://projecteuler.net/problem=23 Non-Abundant Sums
#https://projecteuler.net/thread=23
#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#A number n is called deficient if the sum of its proper divisors is less than n
#A number n is called abundant if the sum of its proper divisors is greater than n.
#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#The first perfect number is 6.  https://en.wikipedia.org/wiki/Perfect_number
#Every integer greater than 20161 can be written as the sum of two abundant numbers https://en.wikipedia.org/wiki/Abundant_number
#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

abundantnumberslist = []
targetnumber = 20161
number = 1
while number <= targetnumber:
	divisorslist = []
	for eachnumber in range(1,number):
		if number % eachnumber == 0:
			divisorslist.append(eachnumber)
	sumdivisors = sum(divisorslist)
	if sumdivisors > number:
		abundantnumberslist.append(number)
	number += 1
abundantnumberslistsum = []
for i in abundantnumberslist:
	for j in abundantnumberslist:
		ij = i + j
		if ij > targetnumber:
			pass
		elif ij not in abundantnumberslistsum:
			abundantnumberslistsum.append(ij)
numberslist = list(range(1,targetnumber+1))
for eachabundantnumberslistsum in abundantnumberslistsum:	
	if (eachabundantnumberslistsum in numberslist):
		numberslist.remove(eachabundantnumberslistsum)
print(sum(numberslist)) #print 4179871

# perfectnumberslist = []
# deficientnumberslist = []
# abundantnumberslist = []
# number = 1
# while number <= 100:
# 	divisorslist = []
# 	for eachnumber in range(1,number-1):
# 		if number % eachnumber == 0:
# 			divisorslist.append(eachnumber)
# 	#print(divisorslist)
# 	sumdivisors = sum(divisorslist)
# 	if sumdivisors == number:
# 		#print("Perfect Number")
# 		perfectnumberslist.append(number)
# 	elif sumdivisors > number:
# 		#print("Abundant sum divisors %d greater than number %d." %(sumdivisors, number))
# 		abundantnumberslist.append(number)
# 	elif sumdivisors < number:
# 		#print("Deficient sum divisors %d less than number %d." %(sumdivisors, number))
# 		deficientnumberslist.append(number)
# 	number += 1
# #print("Perfect Numbers List",perfectnumberslist)
# #print("Deficient Numbers List",deficientnumberslist)
# print("Abundant Numbers List",abundantnumberslist)
# abundantnumberslistsum = []
# for i in abundantnumberslist:
# 	for j in abundantnumberslist:
# 		ij = i + j
# 		if ij not in abundantnumberslistsum:
# 			abundantnumberslistsum.append(ij)
# abundantnumberslistsum.sort()
# print(abundantnumberslistsum)
# numberslist = []
# for eachnumber in range(1,101):
# 	numberslist.append(eachnumber)
# print(numberslist)
# for eachabundantnumberslistsum in abundantnumberslistsum:	
# 	if (eachabundantnumberslistsum in abundantnumberslistsum) and (eachabundantnumberslistsum <= 100):
# 		numberslist.remove(eachabundantnumberslistsum)
# print(numberslist)
# print(sum(numberslist))