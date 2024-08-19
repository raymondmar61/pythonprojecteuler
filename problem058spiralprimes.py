#YouTube Project Euler Problem 58： Spiral Primes [smHUa4v9xWc]
#Starting with and spiralling anticlockwise in the following way, a square spiral with side length is formed.
'''
37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49
'''
#It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13~62%.
#If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
#YouTuber used Problem 28 as a template.
# limit = 1001
# biggestvalue = limit**2
# valueinitialize = 1
# addvalue = 2
# sumanswer = valueinitialize
# while valueinitialize < biggestvalue:
#     sumanswer +=addvalue * 10
#     sumanswer += valueinitialize * 4
#     valueinitialize += addvalue * 4
#     addvalue += 2
# print(sumanswer) #print 669171001

def checkisprimenumber(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5)+1,2):
        if num % i == 0:
            return False
    return True

valueinitialize = 1
addvalue = 0
numbercountdiagonals = 1
numberofprimes = 0

while True:
    #Form the corners of each square spiral
    addvalue += 2
    for i in range(4):
        valueinitialize += addvalue
        if checkisprimenumber(valueinitialize):
            numberofprimes +=1
    numbercountdiagonals += 4 #Add four for the next four corners of the square spiral
    percentagediagonalsareprimes = numberofprimes/numbercountdiagonals * 100
    if percentagediagonalsareprimes < 10:
        print(f"Found {numberofprimes} prime numbers out of {numbercountdiagonals} diagonal numbers for a percentage of {percentagediagonalsareprimes}") #print Found 5248 prime numbers out of 52481 diagonal numbers for a percentage of 9.999809454850327
        break
print(f"Found {numberofprimes} prime numbers out of {numbercountdiagonals}") #print Found 5248 prime numbers out of 52481
print(f"Sides of length {addvalue+1}") #print Sides of length 26241