#https://projecteuler.net/problem=49 Prime Permutations
#https://projecteuler.net/thread=49
#The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
#What 12-digit number do you form by concatenating the three terms in this sequence?
from itertools import count, permutations, combinations
import time
from collections import Counter
startime = time.clock()
def checkifprime(n): #n must be greater than one
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

answerlist = []
#permutation number list from its prime number
arithmeticpermutationlist = []
#start at 1488
n = 1487

while n < 10000:
    primepermutationlist = []
    #check n for prime permutation if n is a prime number, no zero(s), and not a permutation from prior n
    if checkifprime(n) == True and (("0") not in str(n)) and (n not in arithmeticpermutationlist):
        for each1487 in permutations(str(n),4):
            integernumber = int("".join(map(str, each1487)))            
            if checkifprime(integernumber) == True:
                primepermutationlist.append(integernumber)
                arithmeticpermutationlist.append(integernumber)
    #create a primepermutationdifference dictionary two permutations as a tuple key and its difference as a value
    primepermutationdifference = {}
    for eachprimepermutationlist in combinations(primepermutationlist,2):
        #two combinations eachprimepermutationlist positive numbers and its difference inserted to primepermutationdifference
        if eachprimepermutationlist[1]-eachprimepermutationlist[0] > 0:
            primepermutationdifference[eachprimepermutationlist] = eachprimepermutationlist[1]-eachprimepermutationlist[0]
    #find the second key and its value, sum both of them, answer is found if in primepermutationlist; e.g. 4817+3330=8147.  8147 is in primepermutationlist.  The keys for primepermutationdifference are from combinations primepermutationlist.
    for key, value in primepermutationdifference.items():
        if (key[1]+value) in primepermutationlist:
            answerlist.append(str(key[0])+str(key[1])+str(key[1]+value))
    n += 1

print(answerlist)  #print ['148748178147', '296962999629']
endtime = time.clock()
print((endtime-startime),"seconds") #print 0.038331000000000004 seconds
print((round(endtime-startime)),"seconds") #print 0 seconds