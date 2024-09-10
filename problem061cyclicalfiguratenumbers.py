#okay to delete yes
#YouTube #61： Cyclical Figurate Numbers - Project Euler [hrRrPlrEfcg]
'''
Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers and are generated by the following formulae:

Triangle:  P3,n=n(n+1)/2.  1,3,6,10,15,...
Square:  P4,n=n^2.  1,4,9,16,25,...
Pentagonal:  p5,n=n(3n-1)/2.  1,5,12,22,35,...
Hexagonal:  p6,n=n(2n-1).  1,6,15,28,45,...
Heptagonal:  p7,n=n(5n-3)/2.  1,7,18,34,55,...
Octagonal:  p8,n=n(3n-2).  1,8,21,40,65,...

Triangle:    1,3,6,10,15,...
Square:      1,4,9,16,25,...
Pentagonal:  1,5,12,22,35,...
Hexagonal:   1,6,15,28,45,...
Heptagonal:  1,7,18,34,55,...
Octagonal:   1,8,21,40,65,...

The ordered set of three 4-digit numbers 8128, 2882, and 8281 has three interesting properties.

1 The set is cyclic for which the last two digits of each number is the first two digits of the next number (including the last number with the first).
2 Each polygonal type triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882) is represented by a different number in the set.  RM:  each set must include one of each number in the set.  The three 4-digit numbers are triangle, sequare, and pentagonal.  The four 4-digit numbers are triangle, sequare, pentagonal, and hexagonal.
3 This is the only set of 4-digit numbers with this property.  RM:  four digits the numbers are between 1,000 and 9,999.

Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.
'''

'''
3 cyclic 4-digit numbers to return 19291.  8128+2882+8281=19291
4 cyclic 4-digit numbers to return 28684.
5 cyclic 4-digit numbers to return 76255.
6 cyclic 4-digit numbers to return 28684.
'''

class Generatepolygonalnumbers():
    def __init__(self):
        #self.polygonaltype = polygonaltype
        self.digitnumbers = 1
        self.n = 1
        self.polygonalnumberslist = []
    def trianglepoly(self):
        while self.digitnumbers <= 9999:
            self.digitnumbers = int((self.n * (self.n + 1)) / 2)
            #print("triangle", self.digitnumbers)
            if self.digitnumbers >= 1000 and self.digitnumbers <= 9999:
                self.polygonalnumberslist.append(self.digitnumbers)
            self.n += 1
        #print(self.polygonalnumberslist)
        return self.polygonalnumberslist
    def squarepoly(self):
        while self.digitnumbers <= 9999:
            self.digitnumbers = pow(self.n, 2)
            #print("square", self.digitnumbers)
            if self.digitnumbers >= 1000 and self.digitnumbers <= 9999:
                self.polygonalnumberslist.append(self.digitnumbers)
            self.n += 1
        return self.polygonalnumberslist
    def pentagonalpoly(self):
        while self.digitnumbers <= 9999:
            self.digitnumbers = int((self.n * ((self.n * 3) - 1)) / 2)
            if self.digitnumbers >= 1000 and self.digitnumbers <= 9999:
                self.polygonalnumberslist.append(self.digitnumbers)
            self.n += 1
        return self.polygonalnumberslist
    def hexagonalpoly(self):
        while self.digitnumbers <= 9999:
            self.digitnumbers = int(self.n * ((self.n * 2) - 1))
            if self.digitnumbers >= 1000 and self.digitnumbers <= 9999:
                self.polygonalnumberslist.append(self.digitnumbers)
            self.n += 1
        return self.polygonalnumberslist
    def heptagonalpoly(self):
        while self.digitnumbers <= 9999:
            self.digitnumbers = int((self.n * ((self.n * 5) - 3)) / 2)
            if self.digitnumbers >= 1000 and self.digitnumbers <= 9999:
                self.polygonalnumberslist.append(self.digitnumbers)
            self.n += 1
        return self.polygonalnumberslist
    def octagonalpoly(self):
        while self.digitnumbers <= 9999:
            self.digitnumbers = int(self.n * ((self.n * 3) - 2))
            if self.digitnumbers >= 1000 and self.digitnumbers <= 9999:
                self.polygonalnumberslist.append(self.digitnumbers)
            self.n += 1
        return self.polygonalnumberslist


calltrianglepolyobject = Generatepolygonalnumbers()
# print(calltrianglepolyobject.trianglepoly()) #print [1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950, 5050, 5151, 5253, 5356, 5460, 5565, 5671, 5778, 5886, 5995, 6105, 6216, 6328, 6441, 6555, 6670, 6786, 6903, 7021, 7140, 7260, 7381, 7503, 7626, 7750, 7875, 8001, 8128, 8256, 8385, 8515, 8646, 8778, 8911, 9045, 9180, 9316, 9453, 9591, 9730, 9870]
trianglelist = calltrianglepolyobject.trianglepoly()
print("triangle", trianglelist) #print triangle [1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016, 2080, 2145, 2211, 2278, 2346, 2415, 2485, 2556, 2628, 2701, 2775, 2850, 2926, 3003, 3081, 3160, 3240, 3321, 3403, 3486, 3570, 3655, 3741, 3828, 3916, 4005, 4095, 4186, 4278, 4371, 4465, 4560, 4656, 4753, 4851, 4950, 5050, 5151, 5253, 5356, 5460, 5565, 5671, 5778, 5886, 5995, 6105, 6216, 6328, 6441, 6555, 6670, 6786, 6903, 7021, 7140, 7260, 7381, 7503, 7626, 7750, 7875, 8001, 8128, 8256, 8385, 8515, 8646, 8778, 8911, 9045, 9180, 9316, 9453, 9591, 9730, 9870]
callsquarepolyobject = Generatepolygonalnumbers()
squarelist = callsquarepolyobject.squarepoly()
print("square", squarelist) #print square [1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724, 6889, 7056, 7225, 7396, 7569, 7744, 7921, 8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801]
callpentagonalpolyobject = Generatepolygonalnumbers()
pentagonallist = callpentagonalpolyobject.pentagonalpoly()
print("poly", pentagonallist) #print poly [1001, 1080, 1162, 1247, 1335, 1426, 1520, 1617, 1717, 1820, 1926, 2035, 2147, 2262, 2380, 2501, 2625, 2752, 2882, 3015, 3151, 3290, 3432, 3577, 3725, 3876, 4030, 4187, 4347, 4510, 4676, 4845, 5017, 5192, 5370, 5551, 5735, 5922, 6112, 6305, 6501, 6700, 6902, 7107, 7315, 7526, 7740, 7957, 8177, 8400, 8626, 8855, 9087, 9322, 9560, 9801]
callhexagonalpolyobject = Generatepolygonalnumbers()
hexagonallist = callhexagonalpolyobject.hexagonalpoly()
callheptagonalpolyobject = Generatepolygonalnumbers()
heptagonallist = callheptagonalpolyobject.heptagonalpoly()
calloctagonalpolyobject = Generatepolygonalnumbers()
octagonallist = calloctagonalpolyobject.octagonalpoly()
print("\n")

class Last2first2loop2():
    def __init__(self, set1, set2, set3):
        self.set1 = set1
        self.set2 = set2
        self.set3 = set3
    def functionv(self):
        for eachset1 in self.set1:
            firsttwodigitsfirst = str(eachset1)[0:2]
            lasttwodigitsfirst = str(eachset1)[2:4]
            for eachset2 in self.set2:
                firsttwodigitsmiddle = str(eachset2)[0:2]
                lasttwodigitsmiddle = str(eachset2)[2:4]
                if lasttwodigitsfirst == firsttwodigitsmiddle:
                    # print(lasttwodigitsfirst, firsttwodigitsmiddle) #print 28 28
                    for eachset3 in self.set3:
                        firsttwodigitsthird = str(eachset3)[0:2]
                        lasttwodigitsthird = str(eachset3)[2:4]
                        if (lasttwodigitsmiddle == firsttwodigitsthird) and (lasttwodigitsthird == firsttwodigitsfirst):
                            print(int(lasttwodigitsfirst), int(firsttwodigitsmiddle), int(lasttwodigitsthird)) #print 28 28 81
                            print(int(eachset1) + int(eachset2) + int(eachset3)) #print 19291
                            print(eachset1, eachset2, eachset3) #print 8128 2882 8281
                            return eachset1, eachset2, eachset3, (int(eachset1) + int(eachset2) + int(eachset3))


knowanswer = Last2first2loop2(set1=trianglelist, set2=pentagonallist, set3=squarelist)
print(knowanswer.functionv()) #print (8128, 2882, 8281, 19291)
#RM:  Use a permutation to cycle the six polygonal number lists?
