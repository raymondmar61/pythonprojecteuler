#https://projecteuler.net/problem=7 10001st prime
#https://projecteuler.net/thread=4
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.  What is the 10,001st prime number?
#10,000th is 104729, 10,001st is 104743

num = 1
primenumberstarget = 0
targetprime = 6
while primenumberstarget < targetprime:
	if num > 1:
	   # check for factors
	   for i in range(2,num):
	       if (num % i) == 0:
	           break
	   else:	   		
	       	primenumberstarget += 1
	       	if primenumberstarget == targetprime:
	       		break
	num += 1	
print(num)

# code works below.  It's good.
# num = 1
# primenumbers = []
# primenumberstarget = 1
# targetprime = 1000
# # take input from the user
# # num = int(input("Enter a number: "))
# # prime numbers are greater than 1
# while primenumberstarget < targetprime:
# 	if num > 1:
# 	   # check for factors
# 	   for i in range(2,num):
# 	       if (num % i) == 0:
# 	           # print(num,"is not a prime number")
# 	           # print(i,"times",num//i,"is",num)
# 	           break
# 	   else:
# 	       print(num,"is a prime number")
# 	       primenumbers.append(num)
# 	# if input number is less than
# 	# or equal to 1, it is not prime
# 	# else:
# 	#    print(num,"is not a prime number")
# 	num += 1
# 	primenumberstarget = len(primenumbers)	
# print(primenumbers)