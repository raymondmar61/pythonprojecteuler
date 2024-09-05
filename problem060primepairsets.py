#YouTube Project Euler Problem 60： Prime Pair Sets [1OMinBHEc68]
#The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 3+7+109+673=792, represents the lowest sum for a set of four primes with this property.
#Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

#Get all prime numbers.  Use Sieve of Erathosthemes method.
import math
howmanynumbers = 10000
isprime = [True] * (howmanynumbers + 1) #create an isprime list its index numbers is the list of numbers initial set to True.  All numbers are prime numbers initially.
isprime[0] = isprime[1] = False #0 and 1 are not prime numbers.  Set to False
for i in range(2, int(math.sqrt(howmanynumbers) + 1)):
    #print(i) #print 2
    if isprime[i] == True:
        kwhileloop = i * i
        #while loop set the number or the index number in isprime list to False because it's not a prime number
        while kwhileloop <= howmanynumbers:
            isprime[kwhileloop] = False
            kwhileloop += i

def checkisprimenumber(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0:
        return False
    if num < howmanynumbers:
        return isprime[num]
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


#Get list of primes excluding 2 and 5 because numbers divisible by 2 and 5 are not prime numbers
primes = [3]
for i in range(7, howmanynumbers):
    if isprime[i]:
        primes.append(i)

def isconcatenating(p1, p2):
    concat1 = str(p1) + str(p2)
    concat2 = str(p2) + str(p1)
    return checkisprimenumber(int(concat1)) and checkisprimenumber(int(concat2))


lowestsum = howmanynumbers * howmanynumbers
lowestset = []
for i1 in range(len(primes)):
    p1 = primes[i1]
    for i2 in range(i1 + 1, len(primes)):
        p2 = primes[i2]
        if isconcatenating(p1, p2):
            for i3 in range(i2 + 1, len(primes)):
                p3 = primes[i3]
                if isconcatenating(p1, p3) and isconcatenating(p2, p3):
                    for i4 in range(i3 + 1, len(primes)):
                        p4 = primes[i4]
                        if isconcatenating(p1, p4) and isconcatenating(p2, p4) and isconcatenating(p3, p4):
                            for i5 in range(i4 + 1, len(primes)):
                                p5 = primes[i5]
                                if isconcatenating(p1, p5) and isconcatenating(p2, p5) and isconcatenating(p3, p5) and isconcatenating(p4, p5):
                                    primeset = [p1, p2, p3, p4, p5]
                                    primesum = sum(primeset)
                                    if primesum < lowestsum:
                                        lowestsum = primesum
                                        lowestset = primeset
                                    break
                            break


print(f"found {len(lowestset)} concatenating primes {lowestset} with sum {lowestsum}")
'''
found 4 concatenating primes [3, 7, 109, 673] with sum 792 between 3 and 1000
found 5 concatenating primes [13, 5197, 5701, 6733, 8389] with sum 26033 between 3 and 10000.  Correct answer.
'''
