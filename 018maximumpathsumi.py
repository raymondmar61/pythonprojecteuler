#https://projecteuler.net/problem=18 Maximum path sum I
#https://projecteuler.net/thread=17
#By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.  That is, 3 + 7 + 4 + 9 = 23.
"""
3
7 4
2 4 6
8 5 9 3
"""
#Find the maximum total from top to bottom of the triangle below:
"""
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""
#NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
#Correct answer is 1074.  My answer is 1064.  Stopped.

"""
Highest Number Per Row
filename = "018maximumpathsumismalltriangle.txt"
#filename = "018maximumpathsumibigtriangle.txt"
newlines = []
newlinesintegers = []
with open(filename, "r") as text_file:
	lines = text_file.readlines()
	#print(lines) #print ['3\n', '7 4\n', '2 4 6\n', '8 5 9 3']
#create a new list converts the number strings to number integers
for i in lines:
	j = i.split(" ")
	k = [int(n) for n in j]
	newlinesintegers.append(k)
print(newlinesintegers) #print [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
maxnumber = 0
for eachnewlinesintegers in newlinesintegers:
	print(eachnewlinesintegers)
	maxeachnewlineintegers = max(eachnewlinesintegers)
	maxnumber = maxnumber + maxeachnewlineintegers
print(maxnumber)
"""

#TRIANGLE SUM
from numpy import * #import numpy module for matrix operations
#filename = "018maximumpathsumismalltriangle.txt"
filename = "018maximumpathsumibigtriangle.txt"
newlines = []
newlinesintegers = []

with open(filename, "r") as text_file:
	lines = text_file.readlines()
	#print(lines) #print ['3\n', '7 4\n', '2 4 6\n', '8 5 9 3']
#create a new list converts the number strings to number integers
for i in lines:
	j = i.split(" ")
	k = [int(n) for n in j]
	newlinesintegers.append(k)
# print(newlinesintegers) #print [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
newlinesintegers = list(newlinesintegers)
#print(type(newlinesintegers)) #<class 'list'>
# print(newlinesintegers[0][0]) #print 3
# print(newlinesintegers[1][0]) #print 7
# print(newlinesintegers[2][2]) #print 6
# print(newlinesintegers[3][1]) #print 5
#print(len(newlinesintegers)) #print 4
bottomrow = len(newlinesintegers)
#print(len(newlinesintegers[bottomrow-1])) #print 4
trianglesum = 0 #initialize trianglesum
love = 0
#trianglesum = newlinesintegers[0][0] #initialize trianglesum
for i in range(0,bottomrow):
	lengthpresentrow = len(newlinesintegers[i])
	print("row index",newlinesintegers.index(newlinesintegers[i]))
	print(newlinesintegers[i])
	for j in range(0,lengthpresentrow):
		if i == 0:			
			trianglesum = trianglesum + newlinesintegers[i][j]
			print("triangle sum",trianglesum)
		if i == 1:			
			leftnumber = newlinesintegers[i][0]
			rightnumber = newlinesintegers[i][1]
			print(leftnumber)
			print(rightnumber)
			if leftnumber >= rightnumber:
				love = leftnumber
				belowleft = 0
				belowright = 1
				trianglesum = trianglesum + love
				print("love",love)
				print(belowleft)
				print(belowright)
				break			
			else:
				love = rightnumber
				belowleft = 1
				belowright = 2				
				trianglesum = trianglesum + love
				print("love",love)
				print(belowleft)
				print(belowright)
				break
		if i >= 2:
			# if belowleft < 0:
			# 	belowleft = 0
			# if belowright > len(newlinesintegers[i]):
			# 	belowright = belowright - 1
			print("index",i,belowleft," ",newlinesintegers[i][belowleft])
			print("index",i,belowright," ",newlinesintegers[i][belowright])
			greaterleft = newlinesintegers[i][belowleft]
			greaterright = newlinesintegers[i][belowright]
			if greaterleft >= greaterright:
				love = greaterleft
				belowleft = belowleft
				belowright = belowright
			else:
				love = greaterright
				belowleft = belowleft + 1
				belowright = belowright + 1
			trianglesum = trianglesum + love
			print("love",love)
			print(belowleft)
			print(belowright)
			break			
print(trianglesum)