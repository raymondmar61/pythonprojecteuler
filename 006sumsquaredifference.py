#https://projecteuler.net/problem=6 Sum Square Difference
#https://projecteuler.net/thread=4
#The sum of the squares of the first ten natural numbers is 1^2 + 2^2 + ... + 10^2 = 385.  The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)^2 = 55^2 = 3025.  Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.  Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

firstnumbers = 100
counter = 1
squares = 0
natural = 0
while counter <= firstnumbers:	
	squares = squares + (counter**2)
	natural = natural + counter
	print(counter," ",counter**2," ",squares," ",natural)
	counter += 1
print(squares)
print(natural)
natural = natural**2
print(natural)
print(natural - squares)

# while counter <= firstnumbers:	
# 	squares = squares + (counter**2)
# 	natural = natural + counter
# 	print(counter," ",counter**2," ",squares," ",natural)
# 	counter += 1
# print(squares)
# print(natural)
# natural = natural**2
# print(natural)
# print(natural - squares)