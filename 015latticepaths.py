#https://projecteuler.net/problem=15 Lattice paths
#https://projecteuler.net/thread=15
#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#How many such routes are there through a 20×20 grid?
#additional sources:  http://www.robertdickau.com/lattices.html, http://www.mathsisfun.com/pascals-triangle.html, https://en.wikipedia.org/wiki/Lattice_path, https://en.wikipedia.org/wiki/Binomial_coefficient

import math

#Binomial coefficient
#n!/k!(n-k)! where n = number and k = choose and n >= k >= 0
#if we look at a cartisan coordinate, then 20x20 is 40 choose 20 or 20+20 choose 20.  Another example, if we choose x=3 and y=2 or (3,2), then it's 5 choose 2 or 3+2 choose 2.
number = 40
choose = 20
binomialcoefficient = (math.factorial(number))/(math.factorial(choose)*math.factorial((number-choose)))
print(binomialcoefficient) #answer is 137846528820

#pascal triangle
pascalterm = []
row = 5
for term in range(0,row+1):
	pascaltriangle = (math.factorial(row))/(math.factorial(term)*math.factorial((row-term)))
	pascalterm.append(pascaltriangle)
print(pascalterm)

#RM too hard method and poor short-term memory
pascaltrianglelist = []
grid = 20
pascaltriangleadjustment = grid -1
pascaltrianglegrid = grid + pascaltriangleadjustment
for term in range(0,pascaltrianglegrid+1):
	pascaltriangle = (math.factorial(pascaltrianglegrid))/(math.factorial(term)*math.factorial((pascaltrianglegrid-term)))
	pascaltrianglelist.append(pascaltriangle)
totalroutes = max(pascaltrianglelist) + max(pascaltrianglelist)
print(totalroutes)
