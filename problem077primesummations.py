#Project Euler Problem 77 Prime Summations
#Project Euler Problem 77： Prime Summations [zFN7B2qelAs]
'''
It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?
'''
#function(n) f(n).  f(n) is the number of ways n can be represented as the sum of at least two primes.
#f(n,x) is the number of ways n can be represented as the sum of primes starting with x and x < n
#f(n) = f(n,2)+f(n,3)+f(n,5)+f(n,7) . . . +f(n,y) for which y is the largest prime smaller than n
#f(2) = 0
#f(3) = 0
#f(5) = 1

#f(n,2) = 1 if n is even.  0 if n is odd.
#f(n,3) = f(n-3,2)+f(n-3,3)

#f(n,x) = f(n-x,2)+f(n-x,3)+f(n-x,5)+ . . . + f(n-x,x) where n-x > x
#f(n,x) = f(n-x)+1 where n-x <= x

limit = 100
target = 5000
isprime = [True] * (limit + 1)
isprime[0] = isprime[1] = False
for i in range(2, int(limit**0.5 + 1)):
    if isprime[i]:
        k = i * i
        while k <= limit:
            isprime[k] = False
            k += i
primes = [i for i in range(len(isprime)) if isprime[i]]


def countsums(n):
    if n <= 3:
        return 0
    sumnumber = 0
    for p in primes:
        if p >= n:
            break
        sumnumber += countsumslargestx(n, p)
    return sumnumber

def countsumslargestx(n, x):
    if x >= n:
        return 0
    if x == 2:
        return 1 if n % 2 == 0 else 0
    if x <= (n - x):
        sumnumber = 0
        for p in primes:
            if p > x:
                break
            sumnumber += countsumslargestx(n - x, p)
        return sumnumber
    return countsums(n - x) + 1


# print(countsums(10)) #print 5
n = 1
while n <= limit:
    count = countsums(n)
    print(f"Counted sums n = {n}")
    '''
    ...
    Counted sums n = 66
    Counted sums n = 67
    Counted sums n = 68
    Counted sums n = 69
    Counted sums n = 70
    Counted sums n = 71
    '''
    if count > target:
        print(f"Found count of {count} for n of {n}") #print Found count of 5304 for n of 71
        break
    n += 1
