#https://projecteuler.net/problem=10 Summation of primes
#https://projecteuler.net/thread=4
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

newa = []
def eratosthenes(n):
    multiples = []
    for i in range(2, n+1):
        if i not in multiples:
            #print (i)
            newa.append(i)
            for j in range(i*i, n+1, i):
                multiples.append(j)
eratosthenes(10)
print(newa)
print(sum(newa))

#Run on Python 2.7
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]
#print(primes(2000000))
print(sum(primes(2000000))) #answer is 142913828922
