#Project Euler Problem 73 Counting Fractions In A Range
#Project Euler Problem 73： Counting Fractions in a Range [IxyhZjCJ-k0]
'''
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.  RM:  HCF is Highest Common Factor.

If we list the set of reduced proper fractions for d<=8 in ascending order of size, we get:  1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8.

It can be seen that there are 3 fractions between 1/3 and 1/2 which are 3/8, 2/5, and 3/7.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d<=12000?
'''
lowerbound = 1 / 3
upperbound = 1 / 2
limit = 12000
numfractions = 0
for ddenominator in range(2, limit + 1):
    isrelativeprime = [True] * (ddenominator)
    isrelativeprime[0] = False
    for i in range(2, int(ddenominator / 2) + 1):
        if isrelativeprime[i] and ddenominator % i == 0:
            isrelativeprime[i] = False
            k = i * 2
            while k < ddenominator:
                isrelativeprime[k] = False
                k += i
    start = int(ddenominator * lowerbound)
    end = int(ddenominator * upperbound) + 1
    for nnumerator in range(start, end):
        #test nnumerator/ddenominator is reduced and between 1/3 and 1/2
        fraction = nnumerator / ddenominator
        if isrelativeprime[nnumerator] and lowerbound < fraction < upperbound:
            numfractions += 1
print(f"Found {numfractions} fractions") #print Found 7295372 fractions
