#https://projecteuler.net/problem=1 Multiples of 3 and 5
#Problem 1
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
multiple3 = []
multiple5 = []
for eachnumber in range(1,1000):
	if eachnumber % 3 == 0:
		multiple3.append(eachnumber)
	if eachnumber % 5 == 0:
		multiple5.append(eachnumber)
print(multiple3)
print(multiple5)
# multiple3 = multiple3.extend(multiple5) #error message appears
multiple3.extend(multiple5) #combine multiple5 list to multiple 3 list
print(multiple3)
multiple3 = set(multiple3) #remove duplicates
print(multiple3)
multiple3 = list(multiple3) #convert from set to list
print(multiple3)
sumlistsolution = sum(multiple3)
print(sumlistsolution) #answer is 233168

# faster solution
sumnaturalnumber = int(input("Enter a number to find the sum of natural numbers multiples of 3 and 5: "))
multiple35 = []
for eachnumber in range(1,sumnaturalnumber+1):
	if eachnumber % 3 == 0 or eachnumber % 5 == 0 :
		multiple35.append(eachnumber)
print(multiple35)
sumlistsolution35 = sum(multiple35)
print(sumlistsolution35) #answer is 233168
