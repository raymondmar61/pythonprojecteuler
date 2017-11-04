#https://projecteuler.net/problem=28 Number spiral diagonals
#https://projecteuler.net/thread=28
#Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
"""
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
"""
#It can be verified that the sum of the numbers on the diagonals is 101.
#What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
#RM:  square root of 1001 is 31.  31 spirals or 31x31 square.
from math import sqrt
squaredimensionlist = []
squaredimension = 1001
for eachsquare in range(3,squaredimension+1,2):
	squaredimensionlist.append(eachsquare**2)
#print(squaredimensionlist)
squarecounter = 1
diagonalsum = 0
diagonalsquarerootcheck = 1
for n in range(1,(squaredimension**2)+1):
	#print(n)
	if n == diagonalsquarerootcheck:
		diagonalsum = n + diagonalsum
		if n in squaredimensionlist:
			squarecounter = n
		diagonalsquarerootcheck = diagonalsquarerootcheck + int(sqrt(squarecounter)) + 1
		#print(n,squarecounter)
print(diagonalsum) #print 669171001
