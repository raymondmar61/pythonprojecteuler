#https://projecteuler.net/problem=32 Pandigital products
#https://projecteuler.net/thread=32
#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
#RM:  we approximate the number of digits of a product from the number of digits of a multiplicand and number of digits of a multiplier using log10.  Sum the log10 multiplicand and log10 multiplier.  Add 1.  Then take the floor.  The total digits of the multiplicand, multiplier, and product must equal nine.  Multiplicand and multiplier must be 2 and 3 or 3 and 2 and product must be 4 equal nine.  Also multiplicand and multiplier must be 1 and 4 or 4 and 1 and product must be 4 equal nine.  Any other combination is less than nine or greater than nine.

from itertools import permutations
from time import time
startime = time()

pandigital9 = []
#create a string list 1-9
n = list(map(str,range(1,10)))
#for loop check permutations 1-9.  If divisibility identity is true, then add the product to pandigital9 list.
for n9 in permutations(n, 9):
	if int(n9[0]+n9[1])*int(n9[2]+n9[3]+n9[4])==int(n9[5]+n9[6]+n9[7]+n9[8]):
		pandigital9.append(int(n9[5]+n9[6]+n9[7]+n9[8]))
	if int(n9[0])*int(n9[1]+n9[2]+n9[3]+n9[4])==int(n9[5]+n9[6]+n9[7]+n9[8]):
		pandigital9.append(int(n9[5]+n9[6]+n9[7]+n9[8]))
print(sum(set(pandigital9))) #print 45228
endtime = time()
print((endtime-startime),"seconds") #print 0.7603359222412109 seconds
print((round(endtime-startime)),"seconds") #print 1 seconds