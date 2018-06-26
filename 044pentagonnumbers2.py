#https://projecteuler.net/problem=44 Pentagon Numbers
#https://projecteuler.net/thread=44
#Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:  1, 5, 12, 22, 35, 51, 70, 92, 117, 145, . . . 
#It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.
#Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?
import time
startime = time.clock()

from itertools import combinations
from math import sqrt
pentagonalcombos = []

#Want 10,000 pentagonal numbers.  The largest pair sum is the 10,000th p multiply by two.  Calculate the upper limit n with p*2 to generate the pentagonal numbers list.
startn = 10000
p = (startn*((3*startn)-1))/2
p = p*2
upperlimitn = int((sqrt(1+24*(p))+1)/6)

#generate pentagonal numbers set
pentagonalnumbers = {(n*((3*n)-1))//2 for n in range(1,upperlimitn+1)}

#calculate pentagonal numbers pair sum
for pairsum in combinations(pentagonalnumbers,2):		
	if (pairsum[0]+pairsum[1]) in pentagonalnumbers:
		pentagonalcombos.append(pairsum)

#calculate pentagonal numbers pair difference
for eachpentagonalcombos in pentagonalcombos:	
	difference = eachpentagonalcombos[1]-eachpentagonalcombos[0]
	if difference in pentagonalnumbers:
		print(difference) #print 5482660
endtime = time.clock()
print((endtime-startime),"seconds")
print((round(endtime-startime)),"seconds")
#RM:  answer is 5482660
#Time: 15 seconds

# #williamtell from Project Euler thread
# #RM:  for loop for each combinations p.  Inside the for loop generate the sum and the difference.  If the sum and the difference are the same, then print the difference.  I don't understand the {} generating the pentagonal numbers p.  I believe the answer is create a set which is faster than a list?
# from itertools import combinations
# p = {int((num * ((3 * num) - 1)) / 2) for num in range(1, 3000)}
# for x, y in combinations(p, 2):
# 	diff = abs(x - y)
# 	_sum = x + y
# 	if diff in p and _sum in p:
# 		print(diff, _sum, x, y) #print 5482660 8602840 1560090 7042750

# #Ignacio from Project Euler thread
# #RM:  I don't understand the a in for b in range(a,len(pents)):.  If I remove the a, then the Winner: is printed twice.
# pents=[int(n*(3*n-1)/2) for n in range(1,4000)]
# pents_set=set(pents)
# for a in range(len(pents)):
# 	for b in range(a,len(pents)):
# 		if pents[a]+pents[b] in pents_set and abs(pents[a]-pents[b]) in pents_set:
# 			print('Winner:',abs(pents[a]-pents[b]))

# #Aashish_Ranjan from Project Euler thread
# #RM:  Why for x in lista[-2::-1]:?
# lista,i=[],1
# while i:
# 	#print(lista)
# 	lista.append((i*(3*i-1))//2)
# 	for x in lista[-2::-1]:
# 		#print("x",x)
# 		if lista[-1]-x in lista:
# 			if abs(lista[-1]-2*x) in lista:
# 				print(abs(lista[-1]-2*x))
# 				i=-1
# 				break
# 	i+=1

# #Moppzilla from Project Euler thread
# import numpy as np
# pentagonals=np.array([int(n*(3*n-1)/2) for n in range(1,10001)])
# pentagonalsums=[(pentagonals[a+1:] + i) for a,i in
# enumerate(pentagonals[0:-1])]
# pentagonaldiffs=[(pentagonals[a+1:] - i) for a,i in
# enumerate(pentagonals[0:-1])]
# for a,i in enumerate(pentagonaldiffs):
# 	for b,j in enumerate(i):
# 		if j in pentagonals:
# 			if pentagonalsums[a][b] in pentagonals:
# 				print(pentagonals[a+b+1] - pentagonals[a])

