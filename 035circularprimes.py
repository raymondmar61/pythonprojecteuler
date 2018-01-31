#https://projecteuler.net/problem=35 Circular primes
#https://projecteuler.net/thread=34
#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#How many circular primes are there below one million?
#Sources:  https://stackoverflow.com/questions/8458244/swap-letters-in-a-string-in-python

#2 is added circularprimeslist because it's the only even prime number
circularprimeslist = [2]
#check number is prime
def isprime(n):
	if n == 1:
		return False #1 is not a prime number
	for d in range(2, n):
		if n % d == 0:
			return False
	return True
#circular rotate number
def rotate(numberstring,length):
	rotatenumberslist = []
	primeanswerlist = []
	counter = 0
	while counter < length:
		rotatenumberslist.append(numberstring[counter:length]+numberstring[0:counter])
		counter +=1
	for eachrotatenumberslist in rotatenumberslist:
		eachrotatenumberslistinteger = int(eachrotatenumberslist)
		primenumbercheck = isprime(eachrotatenumberslistinteger)
		if primenumbercheck == True:
			primeanswerlist.append(eachrotatenumberslistinteger)
		else:
			break
	#circular prime count of primeanswerlist equals length of prime number
	if len(primeanswerlist) == length:
		circularprimeslist.append(numberstring)

initialize = 3
while initialize < 1000000:
	if initialize % 75 == 0:
		print(initialize)
	if initialize in circularprimeslist:
		initialize = initialize + 2
	elif isprime(initialize) == False:
		initialize = initialize + 2
	else:
		numberstring = str(initialize)
		numberlength = len(numberstring)
		rotate(numberstring,numberlength)
		initialize = initialize + 2
print(circularprimeslist)
print(len(circularprimeslist))
#2-100 13; 2-1000 25; 2-10000 33; 2-100000 43
#[2, '3', '5', '7', '11', '13', '17', '31', '37', '71', '73', '79', '97', '113', '131', '197', '199', '311', '337', '373', '719', '733', '919', '971', '991', '1193', '1931', '3119', '3779', '7793', '7937', '9311', '9377', '11939', '19391', '19937', '37199', '39119', '71993', '91193', '93719', '93911', '99371', '193939', '199933', '319993', '331999', '391939', '393919', '919393', '933199', '939193', '939391', '993319', '999331'] 55
