#Project Euler Problem 75 Singular Integer Right Triangles
#Project Euler Problem 75： Singular Integer Right Triangles [v9beNhiIZH4]
'''
<p>It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

<p>Given that L is the length of the wire, for how many values of L <= 1,500,000 can exactly one integer sided right angle triangle be formed?
'''
#Find Primitive Pythagorean Triples from the Tree Of Primitive Pythagorean Triples.  For each primitive, find the perimeter and multiply the perimeter until limit is exceeded, counting along the way.  Go through the perimeter dictionary and find all perimeters with one triple.
limit = 1500000
start = (3, 4, 5)
primitivesarray = [start]
def findnexttriples(a, b, c):
    if (a + b + c) > limit:
        return
    aone = a - (2 * b) + (2 * c)
    bone = (2 * a) - b + (2 * c)
    cone = (2 * a) - (2 * b) + (3 * c)
    atwo = a + (2 * b) + (2 * c)
    btwo = (2 * a) + b + (2 * c)
    ctwo = (2 * a) + (2 * b) + (3 * c)
    athree = -a + (2 * b) + (2 * c)
    bthree = -(2 * a) + b + (2 * c)
    cthree = -(2 * a) + (2 * b) + (3 * c)
    primitivesarray.append((aone, bone, cone))
    primitivesarray.append((atwo, btwo, ctwo))
    primitivesarray.append((athree, bthree, cthree))
    findnexttriples(aone, bone, cone)
    findnexttriples(atwo, btwo, ctwo)
    findnexttriples(athree, bthree, cthree)


findnexttriples(*start)
print(primitivesarray) #print [(3, 4, 5), (5, 12, 13), (21, 20, 29), (15, 8, 17), (7, 24, 25), (55, 48, 73), (45, 28, 53), (9, 40, 41), (105, 88, 137), (91, 60, 109), (11, 60, 61), (171, 140, 221), (153, 104, 185), (39, 80, 89), (119, 120, 169), (77, 36, 85), (33, 56, 65), (65, 72, 97), (35, 12, 37), (85, 132, 157), (133, 156, 205), (63, 16, 65), . . .]
perimetertocount = {}
for primitive in primitivesarray:
    p = sum(primitive)
    newp = p
    while newp <= limit:
        perimetertocount.setdefault(newp, 0)
        perimetertocount[newp] += 1
        newp += p
print(perimetertocount) #print {12: 1, 24: 1, 36: 1, 48: 1, 60: 2, 72: 1, 84: 2, 96: 1, 30: 1, 90: 2, 70: 1, 40: 1, 80: 1, 56: 1, . . .}
print(sum([1 for p in perimetertocount if perimetertocount[p] == 1])) #print 161667
