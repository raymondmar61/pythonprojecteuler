#https://projecteuler.net/problem=37 Truncatable primes
#https://projecteuler.net/thread=37
#The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
import time
startime = time.time()

#read one million prime numbers text file excluding 2, 3, 5, 7
with open("primenumbers1000000.txt","r") as fileobject:
	contents = fileobject.read()
	contents = contents.replace("         ",",")
	contents = contents.replace("        ",",")
	contents = contents.replace("       ",",")
	contents = contents.replace("      ",",")
	contents = contents.replace("     ",",")
	contents = contents.replace("    ",",")
	contents = contents.replace("   ",",")
	contents = contents.replace("  ",",")	
	#RM:  delete the last line break \n in text file for the conversion to work
	#RM:  Word Wrap must be deactivated to check primenumbers50000.txt spacing.  Source:  https://www2.cs.arizona.edu/icon/oddsends/primes.htm.  Likewise for primenumbers1000000.txt check for number of spaces between prime numbers; there are no single spaces to replace.
	primenumberslist = list((map(int,contents.split(","))))

#primeanswerlist preanswered 2, 3, 5, 7
primeanswerlist = [2,3,5,7]
#check number is prime
def isprime(n):
	if n == 1:
		return False #1 is not a prime number
	for d in range(2, n):
		if n % d == 0:
			return False
	return True

#truncate the prime number
def truncate(number,numberlength):
	truncatelist = []	
	for n in range(0,numberlength):		
		numbertruncatelefttoright = int((str(number)[n:numberlength]))
		truncatelist.append(numbertruncatelefttoright)
		numbertruncaterightoleft = int((str(number)[0:numberlength-n]))
		truncatelist.append(numbertruncaterightoleft)
	truncatelist2 = (list(set(truncatelist))) #convert to set and then list to remove duplicates
	#while loop check trunicatelist2 prime number; if no primes, break while loop
	counter = 0
	while counter <= len(truncatelist2)-1:
		primenumbercheck = isprime(truncatelist2[counter])
		if primenumbercheck == True:
			pass
		else:
			break
		#if all trunicate numbers prime, add nummber to primeanswerlist list solution
		if counter == len(truncatelist2)-1:
			primeanswerlist.append(number)
		counter +=1

for eachprimenumberslist in primenumberslist:
	eachprimenumberslist = str(eachprimenumberslist)
	eachprimenumberslistlastdigit = len(eachprimenumberslist)-1
	#first digit or last digit is not prime number pass for loop
	if (eachprimenumberslist[0] == "1") or (eachprimenumberslist[0] == "4") or (eachprimenumberslist[0] == "6") or (eachprimenumberslist[0] == "8") or (eachprimenumberslist[0] == "9") or (eachprimenumberslist[eachprimenumberslistlastdigit] == "1") or (eachprimenumberslist[eachprimenumberslistlastdigit] == "9"):
		#print(eachprimenumberslist+" is out")
		pass
	else:
		#print(eachprimenumberslist+" is in")
		numberlength = len(str(eachprimenumberslist))
		truncate(int(eachprimenumberslist),numberlength)
		pass
print(primeanswerlist) #print [2, 3, 5, 7, 23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
print(sum(primeanswerlist)-sum([2,3,5,7])) #print 748317
endtime = time.time()
print((endtime-startime),"seconds")
print((round(endtime-startime)),"seconds")