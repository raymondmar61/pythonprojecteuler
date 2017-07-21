#https://projecteuler.net/problem=9 Special Pythagorean triplet
#https://projecteuler.net/thread=4
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2.  For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.  Find the product abc.
#In laments terms, find a, b, and c for which the a, b, and c sums to 1000.  The a, b, and c must satisfy a^2 + b^2 = c^2.  Take the a in a^2, b in b^2, and c in c^2, sum a, b, and c to equal 1000.

# save it's good
# for a in range(1,6):
# 	for b in range(2,6):
# 		for c in range(3,6):
# 			if (a**2) + (b**2) == (c**2):
# 				print(a, b, c)
# 				break
# 			else:
# 				continue

#save it's good
#a^2 + b^2 = c^2
# clist = []
# for a in range(1,100):
# 	for b in range(2,100):
# 		for c in range(3,100):
# 			if (c**2) in clist:
# 				continue
# 			elif (a**2) + (b**2) == (c**2):
# 				clist.append(c**2)
# 				print(a, b, c)
# 				break
# 			else:
# 				continue
# print(clist)

#save it's good except too long to calculate
# for a in range(1,1000):
# 	for b in range(2,1000):
# 		for c in range(3,1000):
# 			if ((a**2) + (b**2) == (c**2)) and (a + b + c == 1000):
# 				print(a, b, c)
# 				print(a * b * c)
# 				break
# 			else:
# 				continue

for a in range(1,1000):
	for b in range(a,1000): # a < b or b > a
		c = 1000 - a - b #don't need "for c in range(b,1000)" because of algebra
		if ((a**2) + (b**2) == (c**2)) and (a + b + c == 1000):
			print(a, b, c)
			print(a * b * c)
			break
		else:
			continue

# online solution http://www.w3resource.com/euler-project/euler-problem9.php
# for a in range(1, 1000):
#      for b in range(a, 1000):
#          c = 1000 - a - b
#          if c > 0:
#              if c*c == a*a + b*b:
#              	print(a, b, c)
#              	print(a*b*c)
#              	break