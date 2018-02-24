#https://projecteuler.net/problem=36 Double-base palindromes
#https://projecteuler.net/thread=36
#The decimal number, 585 = 1001001001v2 (binary), is palindromic in both bases.
#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#(Please note that the palindromic number, in either base, may not include leading zeros.)
#RM:  Sum of all numbers in both base 10 and base 2, not base 10 or base 2.
#use format(integer,"b") to convert base 10 to base 2
# n = 585
# convert = format(n,"b")
# print(convert) #print 1001001001

import time
startime = time.time()
def palindromenumbers(startnumber,endnumber):
	#find base2 palindrome numbers
	palindromebase2 = []
	for i in range (startnumber,endnumber+1,2): #there are no leading zeroes the last digit cannot be zero, which in base two means that only odd numbers can be palindromes.  source:  http://www.mathblog.dk/project-euler-36-palindromic-base-10-2/
		binary2base10 = i
		i = format(i,"b")
		i = str(i)
		ibackwards = i[::-1]
		if (i == ibackwards):
			palindromebase2.append(binary2base10)
	palindromebase2 = list(map(int,palindromebase2)) 

	#check base2 as base10 palindrome numbers
	palindromebase210 = []
	for i in palindromebase2:
		i = str(i)
		ibackwards = i[::-1]
		if (i == ibackwards):
			palindromebase210.append(i)
	palindromebase210 = list(map(int,palindromebase210)) 
	print(palindromebase210)
	print(sum(palindromebase210)) #answer is 872187

#palindromenumbers() must begin with an odd number
palindromenumbers(1,1000000) 
endtime = time.time()
print((endtime-startime),"seconds")