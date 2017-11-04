#https://projecteuler.net/problem=30 Digit fifth powers
#https://projecteuler.net/thread=29
#Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
"""
1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.
"""
#The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# answer = []
# numbers = 1,5
# print(numbers[0])
# print(numbers[1])
# for eachnumber in range(0,10):
# 	for eachnumber2 in range(0,10):
# 		for eachnumber3 in range(0,10):
# 			for eachnumber4 in range(0,10):
# 				numbertuple = eachnumber, eachnumber2, eachnumber3, eachnumber4
# 				eachnumbersum = eachnumber + eachnumber2 + eachnumber3 + eachnumber4
# 				#print(numbertuple, eachnumbersum)
# 				if ((eachnumber**4) + (eachnumber2**4) + (eachnumber3**4) + (eachnumber4**4) == eachnumbersum) and eachnumbersum > 4:
# 					#print("yes",eachnumbersum)
# 					answer.append(numbertuple)
# print(answer)

# for eachnumber in range(1,5):
# 	for eachnumber2 in range(1,5):
# 		numbertuple = eachnumber, eachnumber2
# 		print(numbertuple, eachnumber+eachnumber2, (eachnumber**2+eachnumber2**2))
# test = [1,6,3,4]
# print(tuple(test))
# tupletest = tuple(test)
#print(tupletest[0]+tupletest[1]+tupletest[2]+tupletest[3])
test2 = 1634
test2 = map(int,str(test2))
#print(test2[0]**4,test2[1]**4,test2[2]**4,test2[3]**4) # error
#print(test2[0]**4+test2[1]**4+test2[2]**4+test2[3]**4) # error
#test2 = list(str(test2))
#print(test2)
tupletest2 = tuple(test2)
print(tupletest2) #print (1, 6, 3, 4)
print(tupletest2[0],tupletest2[1],tupletest2[2],tupletest2[3]) #print 1 6 3 4
print(tupletest2[0]**4,tupletest2[1]**4,tupletest2[2]**4,tupletest2[3]**4)
print(tupletest2[0]**4+tupletest2[1]**4+tupletest2[2]**4+tupletest2[3]**4)
print(type(tupletest2[0]**4+tupletest2[1]**4+tupletest2[2]**4+tupletest2[3]**4))
print(type(test2))
print(type(tupletest2))
test2 = int(''.join(map(str,tupletest2)))
print((tupletest2[0]**4+tupletest2[1]**4+tupletest2[2]**4+tupletest2[3]**4) == test2)