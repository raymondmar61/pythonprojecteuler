#https://projecteuler.net/problem=4 Largest palindrome product
#https://projecteuler.net/thread=4
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.  Find the largest palindrome made from the product of two 3-digit numbers.

#works good below for numbers 1 to 11 adding
power = set()
for a in range(1,11):
	for b in range(1,11):
		power.add(a + b)
print(power)
for eachpower in power:
	if eachpower >= 10:		
		eachpower = str(eachpower)
		#print(eachpower)
		if (eachpower[0] == eachpower[1]):
			print(eachpower,"is a palindrome")

palindromeproduct = 91 * 99
print(palindromeproduct)
palindromeproductstring = str(palindromeproduct)
print(palindromeproductstring[0])
print(palindromeproductstring[2])
if ((palindromeproductstring[0] == palindromeproductstring[3]) and (palindromeproductstring[1] == palindromeproductstring[2])):
	print("Yay")

# works for two 2-digit numbers is 9009 = 91 × 99
# power = set()
# for a in range(91,100):
# 	for b in range(91,100):
# 		power.add(a * b)
# print(power)
# for eachpower in power:
# 	eachpower = str(eachpower)
# 	if (eachpower[0] == eachpower[3]):
# 		if (eachpower[1] == eachpower[2]):
# 			print(eachpower,"is a palindrome")

power = set()
for a in range(900,1000):
	for b in range(900,1000):
		power.add(a * b)
print(power)
for eachpower in power:
	eachpower = str(eachpower)
	length = len(eachpower)	
	if (eachpower[0] == eachpower[length-1]):
		if (eachpower[length-5] == eachpower[length-2]):
			if (eachpower[length-4] == eachpower[length-3]):
				print(eachpower,"is a palindrome") # 906609 is my answer

#error message doesn't work
# palindromeproductstring = str(palindromeproduct)
# for eachpalindromeproduct in palindromeproductstring:
# 	print(eachpalindromeproduct)
# 	if ((eachpalindromeproduct[0] == eachpalindromeproduct[3]) and (eachpalindromeproduct[1] == eachpalindromeproduct[2])):
# 		print("Yay")