#https://projecteuler.net/problem=20 Factorial digit sum
#https://projecteuler.net/thread=20
#n! means n × (n − 1) × ... × 3 × 2 × 1
#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#Find the sum of the digits in the number 100!
from math import factorial

# print(factorial(10)) #print 3628800
# factorialdigitsumlist = list(str(factorial(10)))
# print(factorialdigitsumlist) #print ['3', '6', '2', '8', '8', '0', '0']
# factorialdigitsum = 0
# for eachfactorialdigitsumlist in factorialdigitsumlist:
# 	eachfactorialdigitsumlist = int(eachfactorialdigitsumlist)
# 	factorialdigitsum = factorialdigitsum + eachfactorialdigitsumlist
# print(factorialdigitsum) #print 27

# print(factorial(100)) #print 9332621544394415268169923885626670049071596826438162146859296389521759999322991560894146397615651828625369792082722375825118521091686400000000000000000000000
# factorialdigitsumlist = list(str(factorial(100)))
# factorialdigitsum = 0
# for eachfactorialdigitsumlist in factorialdigitsumlist:
# 	eachfactorialdigitsumlist = int(eachfactorialdigitsumlist)
# 	factorialdigitsum = factorialdigitsum + eachfactorialdigitsumlist
# print(factorialdigitsum) #print 648

factorialdigitsumstring = str(factorial(100))
factorialdigitsum = 0
for eachfactorialdigitsumstring in factorialdigitsumstring:
	eachfactorialdigitsumstring = int(eachfactorialdigitsumstring)
	factorialdigitsum = factorialdigitsum + eachfactorialdigitsumstring
print(factorialdigitsum) #print 648

