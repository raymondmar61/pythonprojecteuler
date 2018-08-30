#https://projecteuler.net/problem=44 Pentagon Numbers
#https://projecteuler.net/thread=44
#Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:  1, 5, 12, 22, 35, 51, 70, 92, 117, 145, . . . 
#It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.
#Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?
import time
startime = time.clock()

from itertools import combinations
from math import sqrt
import bisect
pentagonalnumbers = []
pentagonalcombos = []

#Want 10,000 pentagonal numbers.  The largest pair sum is the 10,000th p multiply by two.  Calculate the upper limit n with p*2 to generate the pentagonal numbers list.
startn = 10000
p = (startn*((3*startn)-1))/2
p = p*2
upperlimitn = int((sqrt(1+24*(p))+1)/6)

#generate pentagonal numbers list
for n in range(1,upperlimitn+1):
	p = (n*((3*n)-1))//2
	pentagonalnumbers.append(p)

#calculate pentagonal numbers pair sum
for combopairs in combinations(pentagonalnumbers[0:10000],2):
	locationright = bisect.bisect_right(pentagonalnumbers, combopairs[0]+combopairs[1]) #calculate the upper limit when checking the sum in pengatonal numbers list
	resultright = pentagonalnumbers[locationright]
	if (combopairs[0]+combopairs[1]) in pentagonalnumbers[pentagonalnumbers.index(combopairs[1]):pentagonalnumbers.index(resultright)]:		
		pentagonalcombos.append(combopairs)

#calculate pentagonal numbers pair difference
for eachpentagonalcombos in pentagonalcombos:
	difference = eachpentagonalcombos[1]-eachpentagonalcombos[0]
	locationleft = bisect.bisect_left(pentagonalnumbers, difference) #calculate the upper limit when checking the difference in pengatonal numbers list
	resultleft = pentagonalnumbers[locationleft]
	try:
		print(isinstance(pentagonalnumbers[pentagonalnumbers.index(resultleft):0:-1].index(difference),int) == True)
		print(difference,"in list")
		break
	except ValueError:
		continue
endtime = time.clock()
print((endtime-startime),"seconds")
print((round(endtime-startime)),"seconds")
#RM:  answer is 5482660
#Time: 8405 seconds