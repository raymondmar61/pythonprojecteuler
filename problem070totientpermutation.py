#Project Euler Problem 70 Totient Permutation
#Project Euler Problem 70： Totient Permutation [93LiT_cmz2o]
'''
Euler's totient function [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n.  For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, phi(9)=6.  The number 1 is considered to be relatively prime to every positive number, so phi(1)=1.

Interestingly, phi(87109)=79180, and it can be seen that 87190 is a permutation of 79180.

Find the value of n, 1<n<10^7, for which phi(n) is a permutation of n and the ratio n/phi(n) produces a minimum.
'''
from collections import Counter
def ispermutation(x, y):
    arrx = [*str(x)]
    arry = [*str(y)]
    arrx.sort()
    arry.sort()
    return arrx == arry


limit = 10**7
#Create list of prime numbers represented by True.  Not prime numbers is False
isprime = [True] * (limit + 1)
isprime[0] = isprime[1] = False
for i in range(2, int(limit**0.5 + 1)):
    if isprime[i]:
        k = i * i
        while k <= limit:
            isprime[k] = False
            k += i
# print(isprime) #print [0 False, 1 False, 2 True, 3 True, 4 False, 5 True, 6 False, 7 True, 8 False, 9 False, 10 False . . . ]
minimumphi = 0
minimumratio = limit
minimumn = 0
for n1 in range(2, int(limit / 2) + 1):
    print("n=", n1, "maximum=", minimumratio)
    '''
    ...
    n= 4999997 maximum= 1.0007090511248113
    n= 4999998 maximum= 1.0007090511248113
    n= 4999999 maximum= 1.0007090511248113
    n= 5000000 maximum= 1.0007090511248113
    '''
    if isprime[n1]:
        for n2 in range(n1 + 1, limit + 1):
            if isprime[n2]:
                n = n1 * n2
                if n >= limit:
                    break
                #calculate phi(n)
                # isrelativeprime = [True] * n
                # isrelativeprime[0] = False
                # k = n1
                # while k < n:
                #     isrelativeprime[k] = False
                #     k += n1
                # k = n2
                # while k < n:
                #     isrelativeprime[k] = False
                #     k += n2
                #calculate phi(n)
                # for i in range(2, int(n / 2) + 1):
                #     if isrelativeprime[i] and n % i == 0:
                #         isrelativeprime[i] = False
                #         k = i * i
                #         while k < n:
                #             isrelativeprime[k] = False
                #             k += i
                # phi = Counter(isrelativeprime)[True]
                #calculate phi(n)
                phi = n - n1 - n2 + 1
                ratio = n / phi
                #check if ratio is less than saved ratio.
                #check if phi(n) is permutation of n
                if ratio < minimumratio and ispermutation(n, phi):
                    minimumphi = phi
                    minimumratio = ratio
                    minimumn = n


print(f"found n of {minimumn} to have phi of {minimumphi} and ratio of {minimumratio}") #print found n of 8319823 to have phi of 8313928 and ratio of 1.0007090511248113
