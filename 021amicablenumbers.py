#https://projecteuler.net/problem=21 Amicable Numbers
#https://projecteuler.net/thread=21
#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#Evaluate the sum of all the amicable numbers under 10000.

amicablenumberslist = []
counter = 2
while counter < 10000:
	lista = []
	for eachnumber in range(1,counter):
		if counter % eachnumber == 0:
			lista.append(eachnumber)
	b = sum(lista)
	listb = []
	for eachnumber in range(1,b):
		if b % eachnumber == 0:
			listb.append(eachnumber)
	if (counter == sum(listb)) and (counter != b):
		amicablenumberslist.append(counter)
		amicablenumberslist.append(b)
	else:
		pass
	counter +=2
print(amicablenumberslist)
print(sum(set((amicablenumberslist)))) #print 31626

# a = 1184
# #a = 220
# #a = 6
# lista = []
# for eachnumber in range(1,a):
# 	if a % eachnumber == 0:
# 		lista.append(eachnumber)
# print(lista)
# print(sum(lista))
# b = sum(lista)
# listb = []
# for eachnumber in range(1,b):
# 	if b % eachnumber == 0:
# 		listb.append(eachnumber)
# print(listb)
# print(sum(listb))
# if (a == sum(listb)) and (a != b):
# 	print("yay")
# 	print(a)
# 	print(b)
# 	print(a+b)