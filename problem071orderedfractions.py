#Project Euler Problem 71 Ordered Fractions
#Project Euler Problem 71： Ordered Fractions [A6UzH1u0JaE]
'''
Consider the fraction, n/d, where n and d are positive integers. If n < d and HCF(n,d) = 1, it is called a reduced proper fraction.  HCF is highest common factor.

If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get: 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8.

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d <=1000000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.
'''
limit = 1000000
target = 3 / 7
#Create list of prime numbers represented by True.  Not prime numbers is False
# isprime = [True] * (limit + 1)
# isprime[0] = isprime[1] = False
# for i in range(2, int(limit**0.5 + 1)):
#     if isprime[i]:
#         k = i * i
#         while k <= limit:
#             isprime[k] = False
#             k += i
# primesarray = [i for i in range(len(isprime)) if isprime[i] == True]

numerator = 2
denominator = 5 #YouTuber guesses answer is between 2/5 and 3/7.
fraction = numerator / denominator
for ddenominator in range(2, limit + 1):
    start = int(ddenominator * fraction)
    for nnumerator in range(start, ddenominator):
        ffraction = nnumerator / ddenominator
        if ffraction >= target:
            break
        # if nnumerator / ddenominator >= target:
        #     break
        if ffraction > (numerator / denominator):
            # Check if fraction is reduced or lowest reduced fraction such as 2/5 and 1/3.
            # isreducedfraction = True
            # for p in primesarray:
            #     if p > nnumerator:
            #         break
            #     if ddenominator % p == 0 and nnumerator % p == 0:
            #         isreducedfraction = False
            #         break
            # if isreducedfraction:
            #    numerator = nnumerator
            #    denominator = ddenominator
            numerator = nnumerator
            denominator = ddenominator
            fraction = ffraction
            break
    if ddenominator % 10000 == 0:
        print(f"Checkpoint.  Found fractions through ddenominator = {ddenominator}")


print(f"answer is {numerator}/{denominator} {numerator/denominator}") #print answer is 428570/999997 0.42857128571385716
