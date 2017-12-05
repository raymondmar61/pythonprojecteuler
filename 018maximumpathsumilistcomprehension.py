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
newlinesintegers = []
filename = "018maximumpathsumismalltriangle.txt"
with open(filename, "r") as text_file:
	lines = text_file.readlines()
print("lines",lines)
for i in lines:
	print("i:",i,end="")
	j = i.split(" ")
	print("j:",j)
	k = [int(n) for n in j]
	print("k:",k)
	newlinesintegers.append(k)

print("\n")
print(newlinesintegers)
n=1
for eachlist in newlinesintegers:
	globals()['numberlist%s' % n] = eachlist
	n+=1
print(numberlist1)
print(numberlist2)
print(numberlist3)
print(numberlist4)
numberlist1234 = [a+b+c+d for a in numberlist1 for b in numberlist2 for c in numberlist3 for d in numberlist4]
print(numberlist1234)
print(max(numberlist1234)) #print 25.  Correct answer is 23.

"""
list1 = [1]
list2 = [2, 3]
list3 = [4, 5, 6]
list123 = [a*b*c for a in list1 for b in list2 for c in list3]
print(list123) #print [8, 10, 12, 12, 15, 18]
listall = [[1], [2, 3], [4, 5, 6]]
listallproduct = [a for a in listall]
print(listallproduct) #print [[1], [2, 3], [4, 5, 6]]

list1 = [1]
list2 = [2, 3]
list3 = [4, 5, 6]
list123 = [a+b+c for a in list1 for b in list2 for c in list3]
print(list123) #print [8, 10, 12, 12, 15, 18]
"""