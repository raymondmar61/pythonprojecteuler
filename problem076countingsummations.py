#Project Euler Problem 76 Counting Summations
#Problem 76： Counting Summations and Partitions - Project Euler Walkthrough [PAXG49dkYVA]
#Project Euler Problem 76： Counting Summations [Rm2QbeUtRIQ]
'''
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
'''
#Partitions of an integer p(n).  We need to subtract 1 for p(n)-1 because we don't count the number itself because the partition function counts the number.  It's p(100)-1.  A recurrence relation can simplify.  Use Euler's Pentagonal Number Theorem and the partition function.  Multiply the two equals 1.  We can a polynominal with clear coefficients equal to 1.  p(0)=1.  p must be a postive number.
#function(n) f(n).  f(n) is the number of ways n can be represented as the sum of at least two positive integers.
'''
The number 6 can be represented as
f(1) 1+1+1+1+1+1
f(2) 2+1+1+1+1
f(2) 2+2+1+1
f(2) 2+2+2
f(3) 3+1+1+1
f(3) 3+2+1
f(3) 3+3
f(4) 4+1+1
f(4) 4+2
f(5) 5+1
'''
#Recursion
#f(n,x) where x < n is the number of ways n can be represented as the sum of integers starting with x.
#f(1) = 0
#f(n) = f(n,1)+f(n,2)+f(n,3)+ . . . +f(n,n-1).  For example, f(8,3)=3+1+1+1+1+1 for which x < n.
#f(n,n-1) = 1
def countsums(n):
    if n <= 3:
        return n - 1
    sumnumber = 0
    for i in range(1, n):
        count = countsumslargestx(n, i)
        sumnumber += count
        # print(f"Found count of {count} for n={n} and x={i}")
    return sumnumber

def countsumslargestx(n, x):
    # print(f"Called f(n,x) with n={n} and x={x}")
    if x >= n:
        return 0
    if x == 1:
        return 1
    if x == 2:
        return int(n / 2)
    if x == n - 1:
        return 1
    if x + 1 == n - x:
        return countsums(n - x)
    if x < n / 2:
        sumnumber = 0
        for i in range(1, x + 1):
            sumnumber += countsumslargestx(n - x, i)
        return sumnumber
    return countsums(n - x) + 1



# print(countsums(6))
'''
Called f(n,x) with n=6 and x=1
Found count of 1 for n=6 and x=1
Called f(n,x) with n=6 and x=2
Found count of 3 for n=6 and x=2
Called f(n,x) with n=6 and x=3
Found count of 3 for n=6 and x=3
Called f(n,x) with n=6 and x=4
Found count of 2 for n=6 and x=4
Called f(n,x) with n=6 and x=5
Found count of 1 for n=6 and x=5
10
'''
print(countsums(100)) #print 190569291
