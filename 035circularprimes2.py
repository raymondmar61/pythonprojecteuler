#https://projecteuler.net/problem=35 Circular primes
#https://projecteuler.net/thread=35
#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#How many circular primes are there below one million?
#Sources:  https://stackoverflow.com/questions/8458244/swap-letters-in-a-string-in-python

with open("primenumbers10000.txt","r") as fileobject:
	contents = fileobject.read()
	contents = contents.replace("\t",",")
	contents = contents.replace("\n",",")
	#RM:  delete the last line break \n in text file for the conversion to work
	primenumberslist = list((map(int,contents.split(","))))

circularprimeslist = []
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
		if eachrotatenumberslistinteger in primenumberslist:
			primeanswerlist.append(eachrotatenumberslistinteger)
		else:
			break
	#circular prime count of primeanswerlist equals length of prime number
	if len(primeanswerlist) == length:
 		circularprimeslist.append(numberstring)

for eachprimenumberslist in primenumberslist:
	numberstring = str(eachprimenumberslist)
	numberlength = len(numberstring)
	rotate(numberstring,numberlength)	
print(circularprimeslist)
print(len(circularprimeslist))
# #2-100 13; 2-1000 25; 2-10000 33; 2-100000 43
# #[2, '3', '5', '7', '11', '13', '17', '31', '37', '71', '73', '79', '97', '113', '131', '197', '199', '311', '337', '373', '719', '733', '919', '971', '991', '1193', '1931', '3119', '3779', '7793', '7937', '9311', '9377', '11939', '19391', '19937', '37199', '39119', '71993', '91193', '93719', '93911', '99371', '193939', '199933', '319993', '331999', '391939', '393919', '919393', '933199', '939193', '939391', '993319', '999331'] 55