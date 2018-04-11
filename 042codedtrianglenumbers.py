#https://projecteuler.net/problem=42 Coded Triangle Numbers
#https://projecteuler.net/thread=42
#The nth term of the sequence of triangle numbers is given by, tn = 1/2*n*(n+1); so the first ten triangle numbers are:  1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
#Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
import time
startime = time.time()

#open file renamed from p042_words.txt to 042codedtrianglenumberswords.txt for personal file organization and create list nameslist
with open("042codedtrianglenumberswords.txt","r") as fileobject:
	contents = fileobject.read()
	contents = contents.replace('"','')
	nameslist = contents.split(",")

#calculate the largest word
maxlength = 0
for eachname in nameslist:
	if len(eachname) > maxlength:
		maxlength = len(eachname)
print(maxlength,"is the largest number count") #print 14 is the largest number count

#the largest word is 14 letters.  The maximum word value is 14*26=364 because the letter z is 26.  Create a list of triangle numbers.
n = 1
trianglenumberlist = []
trianglenumber = 0
while trianglenumber <= 364:	
	trianglenumber = 0
	trianglenumber = int((0.5)*n*(n+1))
	trianglenumberlist.append(trianglenumber)
	n+=1
print(trianglenumberlist) #print [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378]

#calculate the word values and count the number of triangle words
counter = 0
trianglewordcounter = 0
while counter < len(nameslist):
	wordnumber = 0
	for eachword in nameslist[counter]:
		wordnumber = wordnumber + int(ord(eachword)-64)
	if wordnumber in trianglenumberlist:
		trianglewordcounter+=1
	counter+=1
print(trianglewordcounter,"triangle words") #print 162 triangle words

endtime = time.time()
print((endtime-startime),"seconds") #print 0.005393028259277344 seconds
print((round(endtime-startime)),"seconds") #print 0 seconds
