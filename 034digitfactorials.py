#https://projecteuler.net/problem=34 Digit factorials
#https://projecteuler.net/thread=33
#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#Note: as 1! = 1 and 2! = 2 are not sums they are not included.
#Sources:  A factorion is a natural number that equals the sum of the factorials of its decimal digits. For example, 145 is a factorion because 1! + 4! + 5! = 1 + 24 + 120 = 145.  The upper bound is 1,499,999.  https://en.wikipedia.org/wiki/Factorion

from math import factorial
answer=[]
curiousnumber = 3
while curiousnumber < 1499999:
	check = 0
	for eachcuriousnumber in str(curiousnumber):
		check = factorial(int(eachcuriousnumber)) + check
	if check == int(curiousnumber):
		answer.append(check)
	curiousnumber +=1
print(answer)
print(sum(answer)) #answer is 40730