#Project Euler Problem 78 Coin Partitions
#Project Euler Problem 78： Coin Partitions [4kMDkAIgp50]
'''
Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O
Find the least value of n for which p(n) is divisible by one million.
'''
#Use the partition function.
#p(n) = p(n-1) + p(n-2) - (p-5)- p(n-7) + p(n-12) + p(n-15) - p(n-22) - . . .
#sequence 1, 2, 5, 7, 12, 15, 22, . . .
#comes from k(3*k-1)/2, k(3k+1)/2 where k starts at 1
#The first values of the partition function starting with p(0) = 1 are 1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42, 56, 77, 101, 135, 176, 231, 297, 385, 490 ,627, 792. 1002, 1255, . . .
subtractsequence = []
for k in range(1, 1000001):
    first = k * (3 * k - 1) / 2
    second = k * (3 * k + 1) / 2
    subtractsequence.append(int(first))
    subtractsequence.append(int(second))
pdict = {}
def calculatep(n):
    # print(f"calculate function called with {n}")
    if n < 0:
        return 0
    if n <= 1:
        return 1
    if n in pdict.keys():
        return pdict[n]
    sumnumber = 0
    issubtract = False
    count = 0
    for x in subtractsequence:
        if x > n:
            break
        subp = calculatep(n - x)
        if issubtract:
            sumnumber -= subp
        else:
            sumnumber += subp
        count += 1
        if count % 2 == 0:
            issubtract = not issubtract
    pdict[n] = sumnumber
    return sumnumber


n = 10
while True:
    p = calculatep(n)
    if n % 100000 == 0:
        print(f"found p({n}) = {p}")
    if p % 1000000 == 0:
        print(f"found p({n}) = {p}") #print found p(55374) = 36325300925435785930832331577396761646715836173633893227071086460709268608053489541731404543537668438991170680745272159154493740615385823202158167635276250554555342115855424598920159035413044811245082197335097953570911884252410730174907784762924663654000000
        break
    n += 1
