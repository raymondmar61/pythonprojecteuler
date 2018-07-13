#https://projecteuler.net/problem=46 Goldbach's other conjecture
#https://projecteuler.net/thread=46
#It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square or a square number multipled by two.
#9 = 7 + 2×1^2 2*1=2
#15 = 7 + 2×2^2 2*4=8
#21 = 3 + 2×3^2 2*9=18
#25 = 7 + 2×3^2 2*9=18
#27 = 19 + 2×2^2 2*4=8
#33 = 31 + 2×1^2 2*2=4
#35 = 17 + 2×3^2 2*9=18 
#It turns out that the conjecture was false.
#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

#https://www.quora.com/What-are-odd-composite-numbers
#An odd number is any number not divisible by two. A composite number is a number with more than one prime factor. So an odd composite has two or more prime factors, none of which are two.
#First, odd numbers are numbers of the form 2n+1 where n is a positive integer.  1, 3, 5, 7, 9, . . . are all odd numbers.  Secondly, composite numbers are numbers which are product of two or more prime numbers.  All even integers except 2 are composite  All odd integers which are not prime are odd composite numbers.  Examples: 9, 15, 21, 25, 27, 33, 35, . . . are all odd composite numbers.
#A composite number is one that has factors other than itself and one.  An odd number is one that leaves a remainder of 1 when divided by 2.  An odd composite number is a number that fulfils both of those requirements.  For example, 9 is a composite number because it leaves a remainder of 1 when divided by 2 and has the factors 1, 3, 9.
#Prime numbers have exactly two factors: 1 and itself.Composites have more than two factors. The number 1 is neither prime nor composite. Finally, if you are trying to figure out if an odd number is a prime, test to see if the number is divisible by primes like 3 and 7 first.
import time
startime = time.clock()

#upload 10,000 prime numbers in a list from primenumbers10000.txt
with open("primenumbers10000.txt","r") as fileobject:	
	contents = fileobject.read()
	contents = contents.replace("\t",",")
	contents = contents.replace("\n",",")
	shortprimenumbers = list((map(int,contents.split(","))))	

#upload 50,000 odd composite numbers in a list from oddcompositenumbers50000.txt
with open("oddcompositenumbers50000.txt","r") as fileobject:	
	contents = fileobject.read()
	contents = contents.replace("\t",",")
	contents = contents.replace("\n",",")
	shortoddcompositenumbers = list((map(int,contents.split(","))))	

#loop prime numbers and odd composite numbers
foundanswer = False
for eachshortoddcompositenumbers in shortoddcompositenumbers:
	breakwhileloop = False
	if foundanswer == True:
		break
	for eachshortprimenumbers in shortprimenumbers:	
		if breakwhileloop is True:
			break
		answer = 0
		counter = 1
		while eachshortoddcompositenumbers >= answer:
			answer = eachshortprimenumbers + (2*(counter**2))
			if eachshortoddcompositenumbers == answer:
				breakwhileloop = True
				break
			elif eachshortoddcompositenumbers < eachshortprimenumbers:
				print(eachshortoddcompositenumbers) #print 5777
				breakwhileloop = True
				foundanswer = True
				break
			counter += 1

endtime = time.clock()
print((endtime-startime),"seconds") #print 2.425474 seconds
print((round(endtime-startime)),"seconds") #print 2 seconds
