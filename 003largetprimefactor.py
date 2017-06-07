#https://projecteuler.net/problem=3 Larget prime factor
#https://projecteuler.net/thread=3
#Problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143

number = 600851475143
primenumbers = []
primefactors = []

# answer works.  Need more memory to run.
# #method
# def isprime(n):
# 	if n < 2: return False
# 	elif n in (2,3): return True
# 	elif n % 2 == 0 or n % 3 == 0: return False
# 	root = int(n**0.5) + 1
# 	for f in range(5, root, 6):
# 		if n % f == 0 or n % (f + 2) ==0:
# 			return False
# 	return True
# def primenumber_generator():
# 	yield 2
# 	n = 3
# 	while True:
# 		if isprime(n):
# 			yield n
# 		n+=2 #all prime numbers are odd except 2.  Add two when a number is not prime.
# p = primenumber_generator()
# for eachnumber in range(1,number):
# 	primenumber = (next(p))
# 	if number % primenumber == 0:
# 		primefactors.append(primenumber)
# print(primefactors)
# print(max(primefactors))

#run Python2.7
answers27 = []
primefactors27 = []
# Python program to check if the input number is prime or not
def factornum(num):
	if num > 1:
	   # check for factors
	   for i in range(2,num):
	       if (num % i) == 0:
	           print(num,"is not a prime number")
	           #print(i,"times",num//i,"is",num)
	           break
	   else:
	       print(num,"is a prime number")
	# if input number is less than
	# or equal to 1, it is not prime
	else:
	   print(num,"is not a prime number")
#https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
print((factors(number)))
print("\n")
answers = list(factors(number))
for eachanswer in answers:
	answers27.append(eachanswer)
print(answers27)
print("\n")
answers27 = sorted(answers27)
print(answers27)
print("\n")
for eachanswer27 in answers27:
	factornum(eachanswer27)	#memory error.  I answer 6857.

# count = answers27[-1]
# n = len(answers27)
# while n > 0:
# 	if number % answers27[n] == 0:
# 		primefactors27.append(answers27[n])
# 	n = n - 1
# print(primefactors27)

# while count != 1:
# 	factors(count)
# 	print(sorted(answers))
# 	count = answers[-1]

# for eachnumber in reversed(range(1,number)):
# 	primenumber = (next(p))
# 	if number % primenumber == 0:
# 		primefactors.append(primenumber)
# 		break
# print(primefactors)
# print(max(primefactors))

#error
# for eachnumber in range(1,number):
# 	#print(next(p))
# 	if number % next(p) == 0:
# 		primefactors.append(next(p))
# print(primefactors)
# print(max(primefactors))

#error
# counter = 1
# while counter <= number:
# 	if number % next(p) == 0:
# 		primefactors.append(p)
# 	counter += 1
# print(primefactors)
# print(max(primefactors))

# Python program to check if the input number is prime or not
# def primefunction(num):
# 	for i in reversed(range(2,num)):
# 		if (num % i) == 0:
# 			print(num,"is not a prime number")
# 			print(i,"times",num//i,"is",num)
# 			break
# 		elif:
# 			print(num,"is a prime number")
# 		# if input number is less than or equal to 1, it is not prime
# 		else:
# 			print(num,"is not a prime number")

# # for eachnumber in reversed(range(1,number)):
# # 	if number % eachnumber == 0:
# # 		print(eachnumber)

# for eachnumber in reversed(range(1,number)):
# 	primenumber = (primefunction(eachnumber))
# 	if number % primenumber == 0:
# 		primefactors.append(primenumber)
# 		break
# print(primefactors)
# print(max(primefactors))

#https://www.programiz.com/python-programming/examples/prime-number
# Python program to check if the input number is prime or not
num = 407
# take input from the user
# num = int(input("Enter a number: "))
# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")