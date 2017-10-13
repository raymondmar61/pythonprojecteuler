#https://projecteuler.net/problem=26 Reciprocal Cycles
#https://projecteuler.net/thread=25
#A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 (and 11 to 23) are given:
#1/2=0.5 <-- 0 recurring
#1/3=0.(3) <-- 1 recurring
#1/4=0.25 <-- 0 recurring
#1/5=0.2 <-- 0 recurring
#1/6=0.1(6)  <--one digit recurring
#1/7=0.(142857) <--six digits recurring
#1/8=0.125 <-- 0 recurring
#1/9=0.(1) <-- 1 recurring
#1/10=0.1 <-- 0 recurring
#1/11=0.(09) <-- 2 recurring
#1/12=0.08(3) <-- 1 recurring
#1/13=0.(076923) <-- 6 recurring
#1/14=0.(0714285) <-- 6 recurring
#1/15=0.0(6) <-- 1 recurring
#1/16=0.0625 <-- 0 recurring
#1/17=0.(0588235294117647) <-- 16 recurring
#1/18=0.0(5) <-- 1 recurring
#1/19=0.(052631578947368421) <-- 18 recurring
#1/20=0.05 <-- 0 recurring
#1/21=0.(047619) <-- 6 recurring
#1/22=0.0(45) <-- 2 recurring
#1/23=0.(0434782608695652173913) <-- 22 recurring
#1/24=0.41(6) <-- 3 recurring
#1/25=0.04 <-- 0 recurring
#Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
#Additional sources:  https://en.wikipedia.org/wiki/Repeating_decimal

#https://zach.se/project-euler-solutions/26/
def recurring_cycle(n, d):
	# solve 10^s % d == 10^(s+t) % d
	# where t is length and s is start
	for t in range(1, d):
		if 1 == 10**t % d:
			return t
	return 0
longest = max(recurring_cycle(1, i) for i in range(2,1001))
print([i for i in range(2,1001) if recurring_cycle(1, i) == longest][0])

# decimal = []
# multiplylist = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# number = 23
# counter = 1
# numerator = 1
# while counter < number:
# 	print(numerator,"%",number)	
# 	remainder = numerator%number
# 	print("Remainder",remainder)
# 	decimal.append(remainder)
# 	#print(remainder)
# 	#numerator = multiplylist[remainder]
# 	numerator = remainder*10
# 	print("Numerator",numerator)
# 	counter +=1
# print(decimal)

# decimal = []
# multiplylist = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# number = 7
# remainder1 = 1%number
# decimal.append(remainder1)
# print(remainder1)
# remainder2 = multiplylist[remainder1]%number
# decimal.append(remainder2)
# print(remainder2)
# remainder3 = multiplylist[remainder2]%number
# decimal.append(remainder3)
# print(remainder3)
# remainder4 = multiplylist[remainder3]%number
# decimal.append(remainder4)
# print(remainder4)
# remainder5 = multiplylist[remainder4]%number
# decimal.append(remainder5)
# print(remainder5)
# remainder6 = multiplylist[remainder5]%number
# decimal.append(remainder6)
# print(remainder6)
# remainder7 = multiplylist[remainder6]%number
# decimal.append(remainder7)
# print(remainder7)
# remainder8 = multiplylist[remainder7]%number
# decimal.append(remainder8)
# print(remainder8)
# print(decimal)
# print(*decimal,sep="")
# #print(type(*decimal,sep=""))
# #check = (*decimal,sep="")
# print("".join(map(str, decimal)))
# a = ("".join(map(str, decimal)))
# #a = int("".join(map(str, decimal)))
# print(a)
# print(type(a))
# # import re
# # regex = re.compile(r"(.+?)(\1)+")
# # match = regex.search(a)
# # print("Match",match.group(0))
# # print("length",len(match.group(0)))

# from math import modf
# frac, whole = modf(1/7)
# print(frac) #print 0.14285714285714285
# print(whole) #print 0.0
# frac, whole = modf(1/14)
# print(frac) #print 0.07142857142857142
# import decimal
# d = decimal.Decimal(1/3)
# print(d.as_tuple().exponent) #print -54.  The negation of the exponent is the number of digits after the decimal point, unless the exponent is greater than 0.  Source:  https://stackoverflow.com/questions/6189956/easy-way-of-finding-decimal-places
# print("\n")

# #https://stackoverflow.com/questions/8672853/detecting-a-repeating-cycle-in-a-sequence-of-numbers-python
# #https://stackoverflow.com/questions/8633996/shortest-repeating-sub-string
# import re
# # regex = re.compile(r'(.+ .+)( \1)+')
# regex = re.compile(r"(.+?)(\1)+")
# match = regex.search("0505")
# print(match.group(0)) #print 0505
# print("\n")

# maximum = 0
# for eachnumber in range(2,10):
# 	fraction = 1/eachnumber
# 	print("Number", eachnumber,"Decimal", fraction)
# 	frac, whole = modf(fraction)
# 	rightdecimal = str(frac)
# 	#print(frac)
# 	regex = re.compile(r"(.+?)(\1)+")
# 	match = regex.search(rightdecimal)
# 	try:
# 		print("Match",match.group(1))
# 		print("length",len(match.group(1)))
# 		temporarymaximum = len(match.group(1))
# 		if temporarymaximum > maximum:
# 			maximum = temporarymaximum
# 	except AttributeError:
# 		pass
# 	finally:
# 		print("")
# print(maximum)
