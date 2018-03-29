#https://projecteuler.net/problem=40 Champernowne's constant
#https://projecteuler.net/thread=40
#An irrational decimal fraction is created by concatenating the positive integers:  0.12345678910"1"112131415161718192021...  It can be seen that the 12th digit of the fractional part is 1.
#If dn represents the nth digit of the fractional part, find the value of the following expression. d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
from timeit import default_timer
start = default_timer()
#begin irrational decimal fraction as string with the decimal at position 0 or irrational[0]
irrational = "."
initialize = 1
#while loop generate numbers from 1 to 1000000 for irrational decimal fraction concatenate positive integers as a string
while initialize < 1000001:
	irrational = irrational+str(initialize)
	initialize += 1
#multiply the d1 to d1000000
print(int(irrational[1])*int(irrational[10])*int(irrational[100])*int(irrational[1000])*int(irrational[10000])*int(irrational[100000])*int(irrational[1000000])) #print 210
print(default_timer()-start) #0.3424473909999506
print(round(default_timer()-start),"seconds") #0 seconds