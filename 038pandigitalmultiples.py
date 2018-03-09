#https://projecteuler.net/problem=38 Pandigital multiples
#https://projecteuler.net/thread=37
#Take the number 192 and multiply it by each of 1, 2, and 3:
#192 × 1 = 192
#192 × 2 = 384
#192 × 3 = 576
#By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
#The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
#What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

pandigitallist = []
# number = 192
# for eachproduct in range(1,4):
# 	answer = number * eachproduct
# 	print(list(str(answer))) #print ['1', '2', '3', '4', '5']
# 	answer = list(str(answer))
# 	for eachanswer in answer:
# 		pandigitallist.append(eachanswer)
# print(pandigitallist)
# pandigitallist.sort()
# print(pandigitallist)
# print(pandigitallist == ['1', '2', '3', '4', '5', '6', '7', '8', '9'])
# print("\n")

pandigitallisttwo = []
numbertwo = 327
for eachproduct in range(1,9):
	if pandigitallisttwo == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
		break
	answer = numbertwo * eachproduct
	answer = str(answer)
	print(answer)
	for eachanswer in answer:
		pandigitallisttwo.append(eachanswer)		
		pandigitallisttwo.sort()		
print(pandigitallisttwo)

pandigitallistthreesolution = []
numberthree = 192
while numberthree <= 330:
	pandigitallistthree = []
	for eachproduct in range(1,numberthree):
		if pandigitallistthree == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
			pandigitallistthreesolution.append(numberthree)
			break
		if len(pandigitallistthree) >= 10:
			break
		answer = numberthree * eachproduct
		answer = str(answer)
		#print(answer)
		for eachanswer in answer:
			pandigitallistthree.append(eachanswer)		
			pandigitallistthree.sort()
			#print(pandigitallistthree)
	#print(numberthree, pandigitallistthree)
	numberthree += 1
	#print(pandigitallistthree)
print(pandigitallistthreesolution) #print [9, 192, 219, 273, 327]