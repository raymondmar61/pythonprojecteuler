#https://projecteuler.net/problem=7 10001st prime
#https://projecteuler.net/thread=4
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.  What is the 10,001st prime number?
#10,000th is 104729, 10,001st is 104743

# Some useful facts:
# 1 is not a prime.
# All primes except 2 are odd.
# All primes greater than 3 can be written in the form 6k+/-1.
# Any number n can have only one primefactor greater than n^.5.
# The consequence for primality testing of a number n is: if we cannot find a number f less than or equal n^.5 that divides n then n is prime: the only primefactor of n is n itself.

import math

def isprime(n):
	if n == 1:
		return False
	elif n < 4:
		return True #2 and 3 are prime numbers
	elif n % 2 == 0:
		return False #prime numbers except 2 are odd
	elif n < 9:
		return True #4, 6, and 8 are excluded
	elif n % 3 == 0:
		return False
	else:
		r = math.floor(n**.5)  #n^.05 rounded to the greatest integer r so r*r<=n
		f = 5
		while f<=r:
			if n % f == 0:
				False
				break
			elif n % (f+2) == 0:
				False
				break
			f = f + 6
		return True
print(isprime(101))
counter = 25
n = 2
while n <= counter:
	print("Is",n, "a prime number? " +str(isprime(n)))
	n += 1



