#https://projecteuler.net/problem=30 Digit fifth powers
#https://projecteuler.net/thread=30
#Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
"""
1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.
"""
#The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
RM:  What's the upper bound number?  Several websites provided different upper bound numbers thoughout well:

https://www.xarg.org/puzzle/project-euler/problem-30/ says the maximum upper bound can have at most 6 digits based on n=d*9^5, which results in a 6 digits number of all 9 using logs.  Summing over these six 9s raised to the 5th power gives 6*(9^5)=354294.

https://r.prevos.net/digit-fifth-powers-euler-problem-30/ says 9^5=59049.  5*59049=295245.

https://duncan99.wordpress.com/2009/01/31/project-euler-problem-30/ says 5 digit numbers the highest sum of the 5th powers is 295245 or 5*(9^5)=295245. So all 5 digit numbers fall within that range.  6 digit numbers the highest sum of the 5th powers is 354294 or 6*(9^5)=354294.  So we can cover 6 digit numbers up to that far and no further.  7 digit numbers the highest value is 413343 or 7*(9^5)=413343.  The highest sum of the 5th powers of a 7 digit number only adds up to a 6 digit number.  So we only need to loop from 2 to 354294.
"""

answerlist = []
power = 5
for i in range(10,354294):
	total = 0
	#print("i:",i)
	for eachi in str(i):
		total = total + int(eachi)**power
		#print(eachi,"^",power,":",total)
	if total == i:
		#print(i,"is an answer")
		answerlist.append(total)
print(answerlist) #print [4150, 4151, 54748, 92727, 93084, 194979]
print(sum(answerlist)) #print 443839

# FAILED PYTHON CODE BELOW
# RM:  I thought sum numbers fifth power is five digit numbers only.

# test2 = 1634
# test2 = map(int,str(test2))
# tupletest2 = tuple(test2)
# print(tupletest2) #print (1, 6, 3, 4)
# print(tupletest2[0],tupletest2[1],tupletest2[2],tupletest2[3]) #print 1 6 3 4
# print(tupletest2[0]**4,tupletest2[1]**4,tupletest2[2]**4,tupletest2[3]**4) #print 1 1296 81, 256
# print(tupletest2[0]**4+tupletest2[1]**4+tupletest2[2]**4+tupletest2[3]**4) #print 1634
# print(type(tupletest2[0]**4+tupletest2[1]**4+tupletest2[2]**4+tupletest2[3]**4)) #print <class 'int'>
# print(type(test2)) #print <class 'map'>
# print(type(tupletest2)) #print <class 'tuple'>
# test2 = int(''.join(map(str,tupletest2)))
# print((tupletest2[0]**4+tupletest2[1]**4+tupletest2[2]**4+tupletest2[3]**4) == test2)

# answerlist = []
# for eachnumber in range(1000,10000):
# 	test2 = eachnumber
# 	test2 = map(int,str(test2))
# 	tupletest2 = tuple(test2)
# 	print(tupletest2)
# 	print(tupletest2[0],tupletest2[1],tupletest2[2],tupletest2[3])
# 	print(tupletest2[0]**4,tupletest2[1]**4,tupletest2[2]**4,tupletest2[3]**4)
# 	print(tupletest2[0]**4+tupletest2[1]**4+tupletest2[2]**4+tupletest2[3]**4)
# 	test2 = int(''.join(map(str,tupletest2)))
# 	print((tupletest2[0]**4+tupletest2[1]**4+tupletest2[2]**4+tupletest2[3]**4) == test2)
# 	if ((tupletest2[0]**4+tupletest2[1]**4+tupletest2[2]**4+tupletest2[3]**4) == test2) is True:
# 		answerlist.append(test2)
# print(answerlist)

# answerlist = []
# for eachnumber in range(10000,100000):
# 	test2 = eachnumber
# 	test2 = map(int,str(test2))
# 	tupletest2 = tuple(test2)
# 	print(tupletest2)
# 	print(tupletest2[0],tupletest2[1],tupletest2[2],tupletest2[3],tupletest2[4])
# 	print(tupletest2[0]**5,tupletest2[1]**5,tupletest2[2]**5,tupletest2[3]**5,tupletest2[4]**5)
# 	print(tupletest2[0]**5+tupletest2[1]**5+tupletest2[2]**5+tupletest2[3]**5+tupletest2[4]**5)
# 	test2 = int(''.join(map(str,tupletest2)))
# 	print((tupletest2[0]**5+tupletest2[1]**5+tupletest2[2]**5+tupletest2[3]**5+tupletest2[4]**5) == test2)
# 	if ((tupletest2[0]**5+tupletest2[1]**5+tupletest2[2]**5+tupletest2[3]**5+tupletest2[4]**5) == test2) is True:
# 		answerlist.append(test2)
# print(answerlist) #print [54748, 92727, 93084]
# print(sum(answerlist)) #print 240559
