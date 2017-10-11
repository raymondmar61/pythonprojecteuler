#https://projecteuler.net/problem=25 1000-digit Fibonacci number
#https://projecteuler.net/thread=25
#The Fibonacci sequence is defined by the recurrence relation:
#Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#Hence the first 12 terms will be:
#F1 = 1
#F2 = 1
#F3 = 2
#F4 = 3
#F5 = 5
#F6 = 8
#F7 = 13
#F8 = 21
#F9 = 34
#F10 = 55
#F11 = 89
#F12 = 144
#The 12th term, F12, is the first term to contain three digits.
#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

import math
#create a dictionary fibonacci_cache which stores recent function calls.
fibonacci_cache = {}
def fibonaccicache(n):
	#if we have cached the value, then return it
	if n in fibonacci_cache:
		return fibonacci_cache[n]
	# Compute the Nth term
	if n == 1:
		value = 1
	elif n == 2:
		value = 2
	elif n > 2:
		value = fibonaccicache(n-1) + fibonaccicache(n-2)
	#Cache the value in fibonacci_cache dictionary and return it
	fibonacci_cache[n] = value
	return value
n = 1
while True:
	#print(n, ":", fibonaccicache(n), "going faster use memorization.")
	digits = int(math.log10(abs(fibonaccicache(n)))+1)
	if digits == 1000:
		print(n+1)
		print(fibonaccicache(n))
		break
	n += 1
#answer is index 4782.  Number is 1070066266382758936764980584457396885083683896632151665013235203375314520604694040621889147582489792657804694888177591957484336466672569959512996030461262748092482186144069433051234774442750273781753087579391666192149259186759553966422837148943113074699503439547001985432609723067290192870526447243726117715821825548491120525013201478612965931381792235559657452039506137551467837543229119602129934048260706175397706847068202895486902666185435124521900369480641357447470911707619766945691070098024393439617474103736912503231365532164773697023167755051595173518460579954919410967778373229665796581646513903488154256310184224190259846088000110186255550245493937113651657039447629584714548523425950428582425306083544435428212611008992863795048006894330309773217834864543113205765659868456288616808718693835297350643986297640660000723562917905207051164077614812491885830945940566688339109350944456576357666151619317753792891661581327159616877487983821820492520348473874384736771934512787029218636250627816


# #https://stackoverflow.com/questions/22656345/how-to-count-the-number-of-digits-in-python
# n = -12345678900123456
# from math import log, ceil
# print(int(ceil(log(abs(n)+1, 10)))) #print 17

# #https://stackoverflow.com/questions/2189800/length-of-an-integer-in-python
# n = -456789
# import math
# digits = int(math.log10(abs(n))+1)
# print(digits) #print 6