#https://projecteuler.net/problem=38 Pandigital multiples
#https://projecteuler.net/thread=38
#Take the number 192 and multiply it by each of 1, 2, and 3:
#192 × 1 = 192
#192 × 2 = 384
#192 × 3 = 576
#By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
#The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
#What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
#RM:  The answer is the largest pandigital itself.  The answer is not the largest integer producing the concatenated product largest pandigital.  9 and 192 are examples of the integer for which they're not the answer.  
#RM:  First of all the fixed number must contain less than 5 digits, since n has to be greater than 1.  Also first number in largest pandigital itself is a 9.  Source:  https://www.mathblog.dk/project-euler-38-pandigital-multiplying-fixed-number/
import time
startime = time.time()

#Acquire integers producing pandigitals
pandigitallistintegers = []
integerstart = 9000
while integerstart <= 9999:
	pandigitallist = []
	for eachproduct in range(1,integerstart):
		if pandigitallist == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
			pandigitallistintegers.append(integerstart)
			break
		if len(pandigitallist) > 8: #pandigital is nine digits and list count starts at 0 
			break
		answer = integerstart * eachproduct
		answer = str(answer)
		#print(answer)
		for eachanswer in answer:
			pandigitallist.append(eachanswer)		
			pandigitallist.sort()
	integerstart += 1
print(pandigitallistintegers) #print [9267, 9273, 9327]

#Take largest integer producing pandigitals and calculate its pandigital
largestpandigital = []
number = max(pandigitallistintegers)
for eachproduct in range(1,10):
	answer = number * eachproduct
	answer = str(answer)
	for eachanswer in answer:
		checklength = len(largestpandigital)
		if checklength > 8: #pandigital is nine digits and list count starts at 0 
			break
		largestpandigital.append(eachanswer)		
print(int("".join(largestpandigital))) #print 932718654
endtime = time.time()
print((endtime-startime),"seconds")
print((round(endtime-startime)),"seconds")
