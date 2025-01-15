#Project Euler Problem 72 Counting Fractions
#Project Euler Problem 72： Counting Fractions [L0ILsaSdpOg]
'''
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.  RM:  HCF is Highest Common Factor.

If we list the set of reduced proper fractions for d<=8 in ascending order of size, we get:  1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d <=1000000?

RM:  "72： Counting Fractions - Project Euler [why8za0ntms]" video says find the sum of Totient's of n from 1 to 1000000.
'''
limit = 15
factors = {}
isprime = [True] * (limit + 1)
isprime[0] = isprime[1] = False
for i in range(2, int((limit / 2) + 1)):
    if isprime[i]:
        k = i * 2
        while k <= limit:
            factors.setdefault(k, [])
            factors[k].append(i)
            isprime[k] = False
            k += i
print(f"Found all factors {factors}") #print Found all factors {4: [2], 6: [2, 3], 8: [2], 10: [2, 5], 12: [2, 3], 14: [2, 7], 9: [3], 15: [3, 5] . . .}
sumnumber = 0
for d in range(2, limit + 1):
    phi = d - 1
    if not isprime[d]:
        phi = d
        for eachfactors in factors[d]:
            numerator = eachfactors - 1
            denominator = eachfactors
            number = phi * numerator
            number = number / denominator
            # print(f"Multiply {phi} by {numerator}/{denominator} for {d}")
            phi = number
    sumnumber += phi
print(f"Total count the elements {sumnumber}") #print Total count the elements 303963552391.0
