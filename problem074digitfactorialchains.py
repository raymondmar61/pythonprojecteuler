#Project Euler Problem 74 Digit Factorial Chains
#Project Euler Problem 74： Digit Factorial Chains [qPGW9rHXPUs]
'''
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
1! + 4! + 5! = 1 + 24 + 120 = 145.

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:  169 --> 363601 --> 1454 --> 169.  RM:  !3+!6+!3+!6+!0+!1=1454 and !0=1.  871 --> 45361 --> 871.  872 --> 45362 --> 872.

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,  69 --> 363600 --> 1454 --> 169 --> 363601 (--> 1454).  78 --> 45360 --> 871 --> 45361 (--> 871).  540 --> 145 (--> 145).

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
'''
from math import factorial
numbertonextnumber = {}
def findnextn(n):
    # print("n", n) #print n 9. n 362880
    if n in numbertonextnumber.keys():
        return numbertonextnumber[n]
    arrn = [*str(n)]
    # print("arrn", arrn) #print arrn ['9']. arrn ['3', '6', '2', '8', '8', '0']
    nextfactorial = sum([factorial(int(d)) for d in arrn])
    numbertonextnumber[n] = nextfactorial
    return nextfactorial


limit = 1000000
numbersixtycount = 0
for n in range(1, limit):
    #calculate length of chain
    chain = [n]
    nextn = findnextn(n)
    while nextn not in chain:
        chain.append(nextn)
        nextn = findnextn(nextn)
    # print(f"For {n}, chain length is {len(chain)}") #print for 9, chain length is 35
    if len(chain) == 60:
        # print(f"For {n}, found chain: {chain}") #print For 974322, found chain: [974322, 367954, 368790, 408967, 408985, 443665, 1614, 746, 5784, 45504, 289, 403202, 36, 726, 5762, 5882, 80762, 46083, 41071, 5067, 5881, 80761, 46082, 41067, 5786, 46200, 748, 45384, 40494, 362953, 363734, 5802, 40443, 79, 367920, 368649, 404670, 5810, 40442, 75, 5160, 842, 40346, 775, 10200, 6, 720, 5043, 151, 122, 5, 120, 4, 24, 26, 722, 5044, 169, 363601, 1454]
        numbersixtycount += 1
    # print(f"For {n}, found chain: {chain}") #print For 9, found chain: [9, 362880, 81369, 403927, 367953, 368772, 51128, 40444, 97, 367920, 368649, 404670, 5810, 40442, 75, 5160, 842, 40346, 775, 10200, 6, 720, 5043, 151, 122, 5, 120, 4, 24, 26, 722, 5044, 169, 363601, 1454]


print(f"Found count {numbersixtycount} with 60 unique terms") #print Found count 402 with 60 unique terms
