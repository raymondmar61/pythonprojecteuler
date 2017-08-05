#https://projecteuler.net/problem=11 Largest product in a grid
#https://projecteuler.net/thread=4
#n the 20×20 grid below, four numbers along a diagonal line have been marked in red or asterik.

#08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
#49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
#81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
#52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
#22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
#24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
#32 98 81 28 64 23 67 10 *26 38 40 67 59 54 70 66 18 38 64 70
#67 26 20 68 02 62 12 20 95 *63 94 39 63 08 40 91 66 49 94 21
#24 55 58 05 66 73 99 26 97 17 *78 78 96 83 14 88 34 89 63 72
#21 36 23 09 75 00 76 44 20 45 35 *14 00 61 33 97 34 31 33 95
#78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
#16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
#86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
#19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
#04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
#88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
#04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
#20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
#20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
#01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

#The product of these numbers is 26 × 63 × 78 × 14 = 1788696
#What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

#https://stackoverflow.com/questions/595374/whats-the-python-function-like-sum-but-for-multiplication-product
#sum([3,4,5]) == 3 + 4 + 5 == 12
#from functools import reduce # Valid in Python 2.6+, required in Python 3
#import operator
#reduce(operator.mul, (3, 4, 5), 1)
from functools import reduce
import operator
grid = [8, 2, 22, 97, 38, 15]
print(sum(grid)) #print 182
print(reduce(operator.mul, (3, 4, 5), 1)) #print 60
print(reduce(operator.mul, (3, 4, 5), 2)) #print 120
print(reduce(operator.mul, (3, 4, 5), 3)) #print 180
print(reduce(operator.mul, (3, 4, 5), 10)) #print 600
print(reduce(operator.mul, (grid), 1)) #print 19462080
print(reduce(operator.mul, (grid), 2)) #print 38924160
print(reduce(operator.mul, (grid), -10)) #print -19462080
def product(iterable):
	p = 1
	for n in iterable:
		p = p * n
	return p
threefourfive = (3,4,5)
#print(product(3,4,5)) #error  TypeError: product() takes 1 positional argument but 3 were given
print(product(threefourfive)) #print 60
print(product(grid)) #print 19462080
print("\n")

#https://chrisalbon.com/python/iterate_over_multiple_lists_simultaneously.html
names = ['James', 'Bob', 'Sarah', 'Marco', 'Nancy', 'Sally']
ages = [42, 13, 14, 25, 63, 23]
list3 = [1,2,3,4,5,6, 700]
for eachname in names:
	print(eachname)
for eachages in ages:
	print(eachages)
#for eachname, eachages in (names, ages):
	#print(eachname, eachages) #ValueError: too many values to unpack (expected 2)
for eachname, eachages in zip(names, ages):
	print(eachname, eachages) #James 42\nBob 13\nSarah 14\nMarco 25\nNancy 63\nSally 23\n
for eachname, eachages, eachlist3 in zip(names, ages, list3):
	print(eachname, eachages, eachlist3) #James 42 1\n Bob 13 2\n Sarah 14 3\n Marco 25 4\n Nancy 63 5\n Sally 23 6\n
print("\n")

#https://www.codecademy.com/en/forum_questions/5492e5289113cbcd5b004b52
#The zip function stops when it reaches the end of the shortest list.
lista = [3, 9, 17, 15, 19]
listb = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
for eachlista, eachlistb in zip(lista, listb):
	print(eachlista, eachlistb) #print 3 2\n 9 4\n 17 8\n15 10\n19 30\n
for eachlista, eachlistb in zip(lista, listb):
	if eachlista > eachlistb:
		print(eachlista,"is greater than",eachlistb)
	else:
		print(eachlistb,"is greater than",eachlista)
	print(max(eachlista, eachlistb))

#https://www.saltycrane.com/blog/2008/04/how-to-use-pythons-enumerate-and-zip-to/
#enumerate- Iterate over indices and items of a list
alist = ["a1","a2","a3"]
for i, a in enumerate(alist):
	print(i, a) #print 0 a1\n 1 a2\n 2 a3
#zip- Iterate over two lists in parallel
alist = ["a1","a2","a3"]
blist = ["b1","b2","b3"]
clist = []
for a, b in zip(alist, blist):
	print(a, b) #print a1 b1\n a2 b2\n a3 b3
print(list(zip(alist, blist))) #print [('a1', 'b1'), ('a2', 'b2'), ('a3', 'b3')]
for a, b in enumerate(zip(alist, blist)):
	print(a, b) #print 0 ('a1, b1')\n 1 ('a2, b2')\n 2 ('a3, b3')
	print(a) #print 0\n 1\n 2
	print(b) #print ('a1, b1')\n ('a2, b2')\n ('a3, b3')
	print(list(b)) #print ['a1, b1']\n ['a2, b2']\n ['a3, b3']
for a, b in zip(alist, blist):
	clist.append(a)
	clist.append(b)
print(clist) #['a1', 'b1', 'a2', 'b2', 'a3', 'b3']
# from itertools import izip, count
# for i, a, b in izip(count(), alist, blist):
# 	print(i, a, b) #ImportError:  cannon import name 'izip'

boys = ["Bob","Henry","Jason"]
girls = ["Heather","Jen","Michelle","Maria"]
pairings = []
for eachboys in boys:
	for eachgirls in girls:
		print(eachboys, eachgirls) #print Bob Heather Bob Jen Bob Michelle Bob Maria Henry Heather Henry Jen enry Michelle Henry Maria Jason  eather Jason Jen Jason Michelle Jason Maria
		boygirl = eachboys, eachgirls
		pairings.append(boygirl)
print(pairings) #print [('Bob', 'Heather'), ('Bob', 'Jen'), ('Bob', 'Michelle'), ('Bob', 'Maria'), ('Henry', 'Heather'), ('Henry', 'Jen'), ('Henry', 'Michelle'), ('Henry', 'Maria'), ('Jason', 'Heather'), ('Jason', 'Jen'), ('Jason', 'Michelle'), ('Jason', 'Maria')]
#print(list(pairings))
boys = ("Bob","Henry","Jason")
girls = ("Heather","Jen","Michelle","Maria")
for eachboys in boys:
	for eachgirls in girls:
		print(eachboys, eachgirls) #print Bob Heather Bob Jen Bob Michelle Bob Maria Henry Heather Henry Jen enry Michelle Henry Maria Jason  eather Jason Jen Jason Michelle Jason Maria
boys = ["Bob","Henry","Jason"]
girls = ["Heather","Jen","Michelle","Maria"]
boysgirls = []
for a in boys:
	boysgirls.append(a)
for a in girls:
	boysgirls.append(a)
print(boysgirls) #print ['Bob', 'Henry', 'Jason', 'Heather', 'Jen', 'Michelle', 'Maria']
print(", ".join(boysgirls)) #print Bob, Henry, Jason, Heather, Jen, Michelle, Maria

#grid = [8, 2, 22, 97, 38, 15, 0]
# grid1 = [8, 2, 22, 97, 38, 15, 0]
# grid2 = [49, 49, 99, 40, 17, 81, 18]
# grid3 = [81, 49, 31, 73, 55, 79, 14]
# grid4 = [52, 70, 95, 23, 4, 60, 11]
# grid5 = [22, 31, 16, 71, 51, 67, 63]
# left = 0
# right = 4
# gridnumber = 1
# print(gridnumber)
# print(gridnumber+3)
#print(grid+int((gridnumber)))
#print(len(grid(gridnumber+3)))
# while True:
#     if right == len(grid(gridnumber)) - 2:
#         break
#     print(grid[left:right],grid2[left+1:right+1],grid3[left+2:right+2],grid4[left+3:right+3])
#     gridsum = sum(grid[left:right])
#     gridsum2 = sum(grid2[left+1:right+1])
#     gridsum3 = sum(grid3[left+2:right+2])
#     gridsum4 = sum(grid4[left+3:right+3])
#     print(gridsum + gridsum2 + gridsum3 + gridsum4)
#     left += 1
#     right += 1

#sum four diagonally top left to bottom right four grids
# while True:
#     if right == len(grid4) - 2:
#         break
#     print(grid[left:right],grid2[left+1:right+1],grid3[left+2:right+2],grid4[left+3:right+3])
#     gridsum = sum(grid[left:right])
#     gridsum2 = sum(grid2[left+1:right+1])
#     gridsum3 = sum(grid3[left+2:right+2])
#     gridsum4 = sum(grid4[left+3:right+3])
#     print(gridsum + gridsum2 + gridsum3 + gridsum4)
#     left += 1
#     right += 1

#sum four diagonally top left to bottom right three grids
# while True:
#     if right == len(grid3) - 1:
#         break
#     print(grid[left:right],grid2[left+1:right+1],grid3[left+2:right+2])
#     gridsum = sum(grid[left:right])
#     gridsum2 = sum(grid2[left+1:right+1])
#     gridsum3 = sum(grid3[left+2:right+2])
#     print(gridsum + gridsum2 + gridsum3)
#     left += 1
#     right += 1

#sum four diagonally top left to bottom right two grids
# while True:
#     if right == len(grid2):
#         break
#     print(grid[left:right],grid2[left+1:right+1])
#     #print(sum(grid[left:right],grid2[left+1:right+1])) #error message
#     gridsum = sum(grid[left:right])
#     gridsum2 = sum(grid2[left+1:right+1])
#     print(gridsum + gridsum2)
#     left += 1
#     right += 1

# sum four across
# while True:
#     if right == len(grid) + 1:
#         break
#     print(grid[left:right])
#     print(sum(grid[left:right]))
#     left += 1
#     right += 1

# grid = [8, 2, 22, 97, 38, 15, 0]
# left = 0
# right = 4
# while True:
#     if right == len(grid) + 1:
#         break
#     print(grid[left:right])
#     print(reduce(operator.mul, grid[left:right],1))    
#     left += 1
#     right += 1