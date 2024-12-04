#Okay to delete:  yes
#Project Euler Problem 68 Magic 5-gon Ring
#Project Euler Problem 68： Magic 5-gon Ring [6o41FyxNbiY]
'''
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.  Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.
Total   Solution Set
9:   4,2,3; 5,3,1; 6,1,2
9:   4,3,2; 6,2,1; 5,1,3
10:  2,3,5; 4,5,1; 6,1,3
10:  2,5,3; 6,3,1; 4,1,5
11:  1,4,6; 3,6,2; 5,2,4
11:  1,6,4; 5,4,2; 3,2,6
12:  1,5,6; 2,6,4; 3,4,5
12:  1,6,5; 3,5,4; 2,4,6
By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?

YouTuber:  The 16 digits happens when the number 10 is one of the external nodes.  A 17 digit string every internal node appears twice and every external node appears once.  The last number in a node must be at the center of two adjacent nodes.  The node set can't end on an external number.
'''
from itertools import permutations
numbers = list(range(1, 11))
print(numbers) #print
sets = permutations(numbers, 3)
print(sets) #print <itertools.permutations object at 0x744cc188eb10>
lines = list(permutations(numbers, 3))
# print(lines) #print [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 2, 6), . . .
#Convert the list of permutations to a dictionary to index each possible line
nextlines = {}
for line in lines:
    nextlines.setdefault(line, [])
    if 10 in [line[1] or line[2]]: #The number ten is not an interior node.  Must be exterior.
        continue
    for nextline in lines:
        if 10 in [nextline[1] or nextline[2]]: #The number ten is not an interior node.  Must be exterior.
            continue
        if sum(line) != sum(nextline):
            continue
        if (line[2] == nextline[1]) and (line[0] not in nextline) and (line[1] not in nextline):
            nextlines[line].append(nextline)
# print(nextlines) #print {(1, 2, 3): [], (1, 2, 4): [], (1, 2, 5): [], (1, 2, 6): [], (1, 2, 7): [], (1, 2, 8): [], (1, 2, 9): [], (1, 2, 10): [], (1, 3, 2): [], (1, 3, 4): [], (1, 3, 5): [], (1, 3, 6): [], (1, 3, 7): [], (1, 3, 8): [], (1, 3, 9): [], (1, 3, 10): [], (1, 4, 2): [], (1, 4, 3): [], (1, 4, 5): [(2, 5, 3), (3, 5, 2)], (1, 4, 6): [(2, 6, 3), (3, 6, 2)], (1, 4, 7): [(2, 7, 3), (3, 7, 2)], (1, 4, 8): [(2, 8, 3), (3, 8, 2)], (1, 4, 9): [(2, 9, 3), (3, 9, 2)], (1, 4, 10): [(2, 10, 3), (3, 10, 2)], (1, 5, 2): [], (1, 5, 3): [(2, 3, 4), (4, 3, 2)], . .
possibilities = []
for line1 in nextlines:
    for line2 in nextlines[line1]:
        for line3 in nextlines[line2]:
            for line4 in nextlines[line3]:
                for line5 in nextlines[line4]:
                    if line1[1] != line5[2]:
                        continue
                    exteriornode = {line1[0], line2[0], line3[0], line4[0], line5[0]}
                    interiornode1 = [line1[1], line2[1], line3[1], line4[1], line5[1]]
                    interiornode2 = [line1[2], line2[2], line3[2], line4[2], line5[2]]
                    interiornode1.sort()
                    interiornode2.sort()
                    if interiornode1 != interiornode2 or len(exteriornode) != 5 or min(exteriornode) != line1[0]:
                        continue
                    possible = True
                    for key in exteriornode:
                        if key in interiornode1:
                            possible = False
                    if possible:
                        possibilities.append([line1, line2, line3, line4, line5])

print(possibilities) #print [[(2, 5, 9), (4, 9, 3), (6, 3, 7), (8, 7, 1), (10, 1, 5)], [(2, 9, 5), (10, 5, 1), (8, 1, 7), (6, 7, 3), (4, 3, 9)], [(6, 3, 5), (7, 5, 2), (8, 2, 4), (9, 4, 1), (10, 1, 3)], [(6, 5, 3), (10, 3, 1), (9, 1, 4), (8, 4, 2), (7, 2, 5)]]
maxpossibility = 0
for possibility in possibilities:
    newlist = []
    for item in possibility:
        newlist += list(item)
    sumdigitstring = int("".join([str(n) for n in newlist]))
    maxpossibility = max(maxpossibility, sumdigitstring)
    print(newlist) #RM:  fifteen numbers, sixteen digits because the number 10 is two digits
    '''
    [2, 5, 9, 4, 9, 3, 6, 3, 7, 8, 7, 1, 10, 1, 5]
    [2, 9, 5, 10, 5, 1, 8, 1, 7, 6, 7, 3, 4, 3, 9]
    [6, 3, 5, 7, 5, 2, 8, 2, 4, 9, 4, 1, 10, 1, 3]
    [6, 5, 3, 10, 3, 1, 9, 1, 4, 8, 4, 2, 7, 2, 5]
    '''
print(maxpossibility) #print 6531031914842725
