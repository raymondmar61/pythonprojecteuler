#https://projecteuler.net/problem=55 Lychrel numbers
#https://projecteuler.net/thread=55
#If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
#Not all numbers produce palindromes so quickly. For example,
#349 + 943 = 1292,
#1292 + 2921 = 4213
#4213 + 3124 = 7337
#That is, 349 took three iterations to arrive at a palindrome.
#Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).
#Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.
#How many Lychrel numbers are there below ten-thousand?
#NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.

import time
from math import factorial
startime = time.clock()

def lychreltest(number):
	#create number as a palindrome
	reversenumber = int(str(number)[::-1])
	stopconter = 0
	while True:
		#add number and number as a palindrome
		numbersum = number+reversenumber
		if numbersum == int(str(numbersum)[::-1]):
			return "Not Lychrel"
			break
		else:
			number = numbersum
			reversenumber = int(str(number)[::-1])
		#number is Lychrel if while loop loops 50 times
		if stopconter == 50:
			return "Lychrel"
			break
		stopconter += 1

#for loop start at 10,000 to 1.  If a number is Lychrel, counter adds 1
lychrelcounter = 0
for eachnumber in range(10000,1,-1):
	if lychreltest(eachnumber) == "Lychrel":
		lychrelcounter += 1
print("Lychrel counter {}".format(lychrelcounter)) #print Lychrel counter 249

endtime = time.clock()
print((endtime-startime),"seconds") #print 0.05188999999999999 seconds
print((round(endtime-startime)),"seconds") #print 0 seconds

