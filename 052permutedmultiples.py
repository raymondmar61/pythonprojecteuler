#https://projecteuler.net/problem=52 Permuted multiples
#https://projecteuler.net/thread=52
#It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
#RM:  x is an integer.  Question is not finding 2x permutations, 3x permutations, 4x permutations, 5x permutations, 6x permutations.  Check 2x, 3x, 4x, 5x, 6x in the permutations.
import time
from itertools import permutations
startime = time.clock()

number = 125874
x = True
while x is True:
    numberlength = str(number)
    samedigitslist = []
    #all permutations for x or x permutations list
    for combos in permutations(numberlength,len(numberlength)):
        samedigitslist.append(int("".join(map(str,combos))))
    #check 2x, 3x, 4x, 5x, 6x in permutations list
    if number*2 in samedigitslist and number*3 in samedigitslist and number*4 in samedigitslist and number*5 in samedigitslist and number*6 in samedigitslist:        
        print(number) #print 142857
        x = False
    number +=1

endtime = time.clock()
print((endtime-startime),"seconds") #print 14.881447999999999 seconds
print((round(endtime-startime)),"seconds") #print 15 seconds

