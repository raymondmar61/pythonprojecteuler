#https://projecteuler.net/problem=17 Number letter counts
#https://projecteuler.net/thread=17
#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters threehundredandfortytwo and 115 (one hundred and fifteen) contains 20 letters onehundredandfifteen. The use of "and" when writing out numbers is in compliance with British usage.
#Sources:  https://pypi.python.org/pypi/num2words
#string functions.  .strip() remove leading and ending spaces.  str.replace(" ","") removes all spaces.  str.split() remove duplicated spaces.

#run Python 2.7
from num2words import num2words
# print(num2words(42)) #print forty-two
# print(num2words(342)) #print three hundred and forty-two
# print(num2words(115)) #print one hundred and fifteen
# print(num2words(1000)) #print one thousand

numberletters = 0
for eachnumber in range(1,1001):
	name = num2words(eachnumber)
	name = name.replace(" ","")
	name = name.replace("-","")
	numberletters = numberletters + len(name)
	#print(type(len(name))) #print <type 'int'>
print(numberletters) #answer is 21124



