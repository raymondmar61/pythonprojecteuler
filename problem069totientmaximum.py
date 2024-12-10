#Project Euler Problem 69 Totient Maximum
#Project Euler Problem 69： Totient Maximum [-L70Bpm6viU]
'''
Euler's totient function [sometimes called the phi function], is defined as the number of positive integers not exceeding n.  For example, as 1, 2, 4, 5, 7, and 8, are all less than or equal to nine and relatively prime to nine, phi(9)=6.  n=6 produces a maximum n/phi(n) for n is less than or equal to 10.  RM:  what's the definition of relatively prime?  It's the larger number which doesn't share any factors with the smaller number.

n   Relatively Prime   phi(n)  n/phi(n)
02  1                  1       2
03  1, 2               2       1.5
04  1, 3               2       2
05  1, 2, 3, 4         4       1.25
06  1, 5               2       3
07  1, 2, 3, 4, 5, 6   6       1.1666. . .
08  1, 3, 5, 7         4       2
09  1, 2, 4, 5, 7, 8   6       1.5
10  1, 3, 7, 9         4       2.5

Find the value of n<=1,000,000 for which n/phi(n) is a maximum.
'''
limit = 1000000
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
maximumn = 1
for n in range(2, limit + 1):
    print("n=", n, "maximum=", maximumn)
    if isprime[n]:
        print(n,"is a prime number")
        newmax = maximumn * n #Multiple the prime numbers together is the the number with the fewest relatively prime numbers below it.  An odd number all even numbers are relatively prime(?).  Multiple the prime numbers together is the number with the fewest relatively prime numbers below it(?).
        print("newmax new maximum number", newmax)
        if newmax > limit: #Stop multiplying when the maximum number exceeds the limit.
            break
        maximumn = newmax
print(maximumn) #print 510510