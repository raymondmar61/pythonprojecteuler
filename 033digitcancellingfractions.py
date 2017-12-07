#https://projecteuler.net/problem=33 Digit cancelling fractions
#https://projecteuler.net/thread=33
#The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
#If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

nontrivialfractions = []
for numerator in range(10,100):
	for denominator in range(10,100):
		if (numerator/denominator) < 1:
			#print(numerator,denominator,(numerator/denominator))
			bigfraction = numerator/denominator
			numerator = str(numerator)
			denominator = str(denominator)
			if numerator[0] == denominator[0] and numerator[1] != "0" and denominator[1] != "0": #exclude numerator[1] in tens 10, 20, 30, etc.
				if int(numerator[1])/int(denominator[1]) == bigfraction:		
					nontrivialfractions.append(numerator[1]+"/"+denominator[1])
			elif numerator[0] == denominator[1] and numerator[1] != "0" and denominator[0] != "0":
				if int(numerator[1])/int(denominator[0]) == bigfraction:
					nontrivialfractions.append(numerator[1]+"/"+denominator[0])
			elif numerator[1] == denominator[1] and numerator[1] != "0" and denominator[0] != "0":
				if int(numerator[0])/int(denominator[0]) == bigfraction:
					nontrivialfractions.append(numerator[0]+"/"+denominator[0])
			elif numerator[1] == denominator[0] and numerator[1] != "0"and denominator[1] != "0":
				if int(numerator[0])/int(denominator[1]) == bigfraction:
					nontrivialfractions.append(numerator[0]+"/"+denominator[1])
			else:
				pass
			numerator = int(numerator)
			denominator = int(denominator)
		else:
			pass
print(nontrivialfractions) #print ['1/4', '1/5', '2/5', '4/8']
import fractions
data = [float(fractions.Fraction(x)) for x in nontrivialfractions]
print(data) #print [0.25, 0.2, 0.4, 0.5]
data2 = [str(float(fractions.Fraction(x))) for x in data]
print(data2) #print ['0.25', '0.2', '0.4', '0.5']
solution = 1
for eachdata in data:
	solution = eachdata * solution
print(solution) #print 0.010000000000000002.  Answer is 100.

"""
fraction = []
counter=0
for numerator in range(10,21):
	for denominator in range(10,21):
		if (numerator/denominator) < 1:
			print(numerator,denominator,(numerator/denominator))
			numerator = str(numerator)
			denominator = str(denominator)
			print(str(numerator[0]))
			print(str(numerator[1]))
			print(str(denominator[0]))
			print(str(denominator[1]))
			if numerator[0] == denominator[0]:
				print(numerator[1]+"/"+denominator[1])
				fraction.append([])
				fraction[counter].append(numerator+"/"+denominator)
				fraction[counter].append(numerator[1]+"/"+denominator[1])
				counter +=1
			elif numerator[0] == denominator[1]:
				print(numerator[1]+"/"+denominator[0])
				fraction.append([])
				fraction[counter].append(numerator+"/"+denominator)
				fraction[counter].append(numerator[1]+"/"+denominator[0])
				counter +=1
			elif numerator[1] == denominator[1]:
				print(numerator[0]+"/"+denominator[0])
				fraction.append([])
				fraction[counter].append(numerator+"/"+denominator)
				fraction[counter].append(numerator[0]+"/"+denominator[0])
				counter +=1
			elif numerator[1] == denominator[0]:
				print(numerator[0]+"/"+denominator[1])
				fraction.append([])
				fraction[counter].append(numerator+"/"+denominator)
				fraction[counter].append(numerator[0]+"/"+denominator[1])
				counter +=1
			else:
				pass
			numerator = int(numerator)
			denominator = int(denominator)
		else:
			pass
"""

# print(fraction)
# import numpy as np
# x = np.array(fraction)
# #print(x)
# y = x.astype(np.float)
# print(y)

# def myFloat(myList):
#     return map(float, myList)
# map(myFloat, fraction)
#[map(float,i) for i in fraction]
#print(fraction)

# solution = []
# for eachfraction1 in fraction:
# 	if eachfraction1[0] == eachfraction1[1]:
# 		solution.append(eachfraction1[0])
# print(solution)

# numerator = 21
# denominator = 13
# numerator = str(numerator)
# denominator = str(denominator)
# print(str(numerator[0]))
# print(str(numerator[1]))
# print(str(denominator[0]))
# print(str(denominator[1]))
# if numerator[0] == denominator[0]:
# 	print(numerator[1]+"/"+denominator[1])
# elif numerator[0] == denominator[1]:
# 	print(numerator[1]+"/"+denominator[0])
# elif numerator[1] == denominator[1]:
# 	print(numerator[0]+"/"+denominator[0])
# elif numerator[1] == denominator[0]:
# 	print(numerator[0]+"/"+denominator[1])
# else:
# 	pass

"""
elements = []
elements.append([])
elements[0].append(10)
elements[0].append(20)
elements.append([])
elements[1].append(11)
elements[1].append(21)
elements.append([])
elements[2].append(12)
elements[2].append(22)
print(elements)
"""

"""
menu = {}
menu["49/98"] = "4/8"
menu["30/50"] = "3/5"
print(menu)
for key in menu:
	print(key)
	print(menu[key])
	print(key, menu[key])
"""

"""
for numerator in range(10,21):
	for denominator in range(10,21):
		if numerator/denominator <1:
			print(numerator,denominator,(numerator/denominator))
"""