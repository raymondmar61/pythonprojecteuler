#Project Euler Problem 67 Maximum Path Sum II
filename = "0067_triangle.txt"
with open(filename, "r") as textfile:
    lines = textfile.readlines()
list18 = []
for eachlines in lines:
    separatenumbers = eachlines.split()
    tointegersnewabunchofnumbers = list(map(int, separatenumbers))
    list18.append(tointegersnewabunchofnumbers)
print(list18) #print [[59], [73, 41], [52, 40, 9], [26, 53, 6, 34], [10, 51, 87, 86, 81], [61, 95, 66, 57, 25, 68], [90, 81, 80, 38, 92, 67, 73], [30, 28, 51, 76, 81, 18, 75, 44], [84, 14, 95, 87, 62, 81, 17, 78, 58], [21, 46, 71, 58, 2, 79, 62, 39, 31, 9], [56, 34, 35, 53, 78, 31, 81, 18, 90, 93, 15], [78, 53, 4, 21, 84, 93, 32, 13, 97, 11, 37, 51], [45, 3, 81, 79, 5, 18, 78, 86, 13, 30, 63, 99, 95], . . .
print("\n")

#Best explanation after clicking top Google search results Google search "maximum path sum 1 problem 18 project euler."  https://www.educative.io/answers/how-to-solve-project-euler--sharp18---maximum-path-sum-problem.  The question asked the maximum or highest path from top to bottom returning the largest sum.  It's not necessarily the maximum number on every row.  Example 16; 7, 8; 10, 91, 4; 100, 3, 2, 11;  The correct answer is 16+7+10+100=133, not 16+8+91+3=118.  It's the path returning the largest sum from top the bottom.  The 133 is the largest sum path from top to bottom connecting adjacent numbers.
#https://raw.org/puzzle/project-euler/problem-18/
listOfLists = list18
print("Number of rows", len(listOfLists)) #print Number of rows 100
print(f"Start checking rows at the {len(listOfLists) - 2}th index row.") #print Start checking rows at the 98th index row.
for rownumber in range(len(listOfLists) - 2, -1, -1):
    print(rownumber) #print 98
    print(listOfLists[rownumber]) #print [30, 11, 85, 31, 34, 71, 13, 48, 5, 14, 44, 3, 19, 67, 23, 73, 19, 57, 6, 90, 94, 72, 57, 69, 81, 62, 59, 68, 88, 57, 55, 69, 49, 13, 7, 87, 97, 80, 89, 5, 71, 5, 5, 26, 38, 40, 16, 62, 45, 99, 18, 38, 98, 24, 21, 26, 62, 74, 69, 4, 85, 57, 77, 35, 58, 67, 91, 79, 79, 57, 86, 28, 66, 34, 72, 51, 76, 78, 36, 95, 63, 90, 8, 78, 47, 63, 45, 31, 22, 70, 52, 48, 79, 94, 15, 77, 61, 67, 68]
print("\n")

for rownumber in range(len(listOfLists) - 2, -1, -1):
    print("TRUE ROW NUMBER", rownumber + 1, listOfLists[rownumber])
    indexcounter = 0
    for rownumbercompare in range(len(listOfLists[rownumber])):
        # print("row number compare", rownumbercompare + 1)
        # print("row number compare list", listOfLists[rownumbercompare])
        print("Row", rownumber + 2, "below row", rownumber + 1, listOfLists[rownumber + 1], "replaced with maximums sums starting row", rownumber)
        print("number row", str(rownumber + 1) + ":", listOfLists[rownumber][rownumbercompare])
        print("index number", indexcounter, "row", rownumber + 2, "below row", str(rownumber + 1) + ":", listOfLists[rownumber + 1][rownumbercompare])
        print("index number", indexcounter + 1, "row", rownumber + 2, "below row", str(rownumber + 1) + ":", listOfLists[rownumber + 1][rownumbercompare + 1])
        print("maximum number between index numbers", indexcounter, "and", str(indexcounter + 1) + ":", max(listOfLists[rownumber + 1][rownumbercompare], listOfLists[rownumber + 1][rownumbercompare + 1]))
        print("Replace listOfLists[rownumber][rownumbercompare] listOfLists[" + str(rownumber) + "][" + str(rownumbercompare) + "] with", listOfLists[rownumber][rownumbercompare], "+", max(listOfLists[rownumber + 1][rownumbercompare], listOfLists[rownumber + 1][rownumbercompare + 1]), "=", listOfLists[rownumber][rownumbercompare] + max(listOfLists[rownumber + 1][rownumbercompare], listOfLists[rownumber + 1][rownumbercompare + 1]))
        #Replace listOfLists[rownumber][rownumbercompare] with the maximum number
        listOfLists[rownumber][rownumbercompare] += max(listOfLists[rownumber + 1][rownumbercompare], listOfLists[rownumber + 1][rownumbercompare + 1])
        indexcounter += 1
    print("\n")
'''
TRUE ROW NUMBER 99 [30, 11, 85, 31, 34, 71, 13, 48, 5, 14, 44, 3, 19, 67, 23, 73, 19, 57, 6, 90, 94, 72, 57, 69, 81, 62, 59, 68, 88, 57, 55, 69, 49, 13, 7, 87, 97, 80, 89, 5, 71, 5, 5, 26, 38, 40, 16, 62, 45, 99, 18, 38, 98, 24, 21, 26, 62, 74, 69, 4, 85, 57, 77, 35, 58, 67, 91, 79, 79, 57, 86, 28, 66, 34, 72, 51, 76, 78, 36, 95, 63, 90, 8, 78, 47, 63, 45, 31, 22, 70, 52, 48, 79, 94, 15, 77, 61, 67, 68]
Row 100 below row 99 [23, 33, 44, 81, 80, 92, 93, 75, 94, 88, 23, 61, 39, 76, 22, 3, 28, 94, 32, 6, 49, 65, 41, 34, 18, 23, 8, 47, 62, 60, 3, 63, 33, 13, 80, 52, 31, 54, 73, 43, 70, 26, 16, 69, 57, 87, 83, 31, 3, 93, 70, 81, 47, 95, 77, 44, 29, 68, 39, 51, 56, 59, 63, 7, 25, 70, 7, 77, 43, 53, 64, 3, 94, 42, 95, 39, 18, 1, 66, 21, 16, 97, 20, 50, 90, 16, 70, 10, 95, 69, 29, 6, 25, 61, 41, 26, 15, 59, 63, 35] replaced with maximums sums starting row 98
number row 99: 30
index number 0 row 100 below row 99: 23
index number 1 row 100 below row 99: 33
maximum number between index numbers 0 and 1: 33
Replace listOfLists[rownumber][rownumbercompare] listOfLists[98][0] with 30 + 33 = 63
Row 100 below row 99 [23, 33, 44, 81, 80, 92, 93, 75, 94, 88, 23, 61, 39, 76, 22, 3, 28, 94, 32, 6, 49, 65, 41, 34, 18, 23, 8, 47, 62, 60, 3, 63, 33, 13, 80, 52, 31, 54, 73, 43, 70, 26, 16, 69, 57, 87, 83, 31, 3, 93, 70, 81, 47, 95, 77, 44, 29, 68, 39, 51, 56, 59, 63, 7, 25, 70, 7, 77, 43, 53, 64, 3, 94, 42, 95, 39, 18, 1, 66, 21, 16, 97, 20, 50, 90, 16, 70, 10, 95, 69, 29, 6, 25, 61, 41, 26, 15, 59, 63, 35] replaced with maximums sums starting row 98
number row 99: 11
index number 1 row 100 below row 99: 33
index number 2 row 100 below row 99: 44
maximum number between index numbers 1 and 2: 44
Replace listOfLists[rownumber][rownumbercompare] listOfLists[98][1] with 11 + 44 = 55
Row 100 below row 99 [23, 33, 44, 81, 80, 92, 93, 75, 94, 88, 23, 61, 39, 76, 22, 3, 28, 94, 32, 6, 49, 65, 41, 34, 18, 23, 8, 47, 62, 60, 3, 63, 33, 13, 80, 52, 31, 54, 73, 43, 70, 26, 16, 69, 57, 87, 83, 31, 3, 93, 70, 81, 47, 95, 77, 44, 29, 68, 39, 51, 56, 59, 63, 7, 25, 70, 7, 77, 43, 53, 64, 3, 94, 42, 95, 39, 18, 1, 66, 21, 16, 97, 20, 50, 90, 16, 70, 10, 95, 69, 29, 6, 25, 61, 41, 26, 15, 59, 63, 35] replaced with maximums sums starting row 98
number row 99: 85
index number 2 row 100 below row 99: 44
index number 3 row 100 below row 99: 81
maximum number between index numbers 2 and 3: 81
Replace listOfLists[rownumber][rownumbercompare] listOfLists[98][2] with 85 + 81 = 166
Row 100 below row 99 [23, 33, 44, 81, 80, 92, 93, 75, 94, 88, 23, 61, 39, 76, 22, 3, 28, 94, 32, 6, 49, 65, 41, 34, 18, 23, 8, 47, 62, 60, 3, 63, 33, 13, 80, 52, 31, 54, 73, 43, 70, 26, 16, 69, 57, 87, 83, 31, 3, 93, 70, 81, 47, 95, 77, 44, 29, 68, 39, 51, 56, 59, 63, 7, 25, 70, 7, 77, 43, 53, 64, 3, 94, 42, 95, 39, 18, 1, 66, 21, 16, 97, 20, 50, 90, 16, 70, 10, 95, 69, 29, 6, 25, 61, 41, 26, 15, 59, 63, 35] replaced with maximums sums starting row 98
number row 99: 31
...

TRUE ROW NUMBER 5 [10, 51, 87, 86, 81]
Row 6 below row 5 [6812, 6951, 6922, 6949, 6917, 6915] replaced with maximums sums starting row 4
number row 5: 10
index number 0 row 6 below row 5: 6812
index number 1 row 6 below row 5: 6951
maximum number between index numbers 0 and 1: 6951
Replace listOfLists[rownumber][rownumbercompare] listOfLists[4][0] with 10 + 6951 = 6961
Row 6 below row 5 [6812, 6951, 6922, 6949, 6917, 6915] replaced with maximums sums starting row 4
number row 5: 51
index number 1 row 6 below row 5: 6951
index number 2 row 6 below row 5: 6922
maximum number between index numbers 1 and 2: 6951
Replace listOfLists[rownumber][rownumbercompare] listOfLists[4][1] with 51 + 6951 = 7002
Row 6 below row 5 [6812, 6951, 6922, 6949, 6917, 6915] replaced with maximums sums starting row 4
number row 5: 87
index number 2 row 6 below row 5: 6922
index number 3 row 6 below row 5: 6949
maximum number between index numbers 2 and 3: 6949
Replace listOfLists[rownumber][rownumbercompare] listOfLists[4][2] with 87 + 6949 = 7036
Row 6 below row 5 [6812, 6951, 6922, 6949, 6917, 6915] replaced with maximums sums starting row 4
number row 5: 86
index number 3 row 6 below row 5: 6949
index number 4 row 6 below row 5: 6917
maximum number between index numbers 3 and 4: 6949
Replace listOfLists[rownumber][rownumbercompare] listOfLists[4][3] with 86 + 6949 = 7035
Row 6 below row 5 [6812, 6951, 6922, 6949, 6917, 6915] replaced with maximums sums starting row 4
number row 5: 81
index number 4 row 6 below row 5: 6917
index number 5 row 6 below row 5: 6915
maximum number between index numbers 4 and 5: 6917
Replace listOfLists[rownumber][rownumbercompare] listOfLists[4][4] with 81 + 6917 = 6998


TRUE ROW NUMBER 4 [26, 53, 6, 34]
Row 5 below row 4 [6961, 7002, 7036, 7035, 6998] replaced with maximums sums starting row 3
number row 4: 26
index number 0 row 5 below row 4: 6961
index number 1 row 5 below row 4: 7002
maximum number between index numbers 0 and 1: 7002
Replace listOfLists[rownumber][rownumbercompare] listOfLists[3][0] with 26 + 7002 = 7028
Row 5 below row 4 [6961, 7002, 7036, 7035, 6998] replaced with maximums sums starting row 3
number row 4: 53
index number 1 row 5 below row 4: 7002
index number 2 row 5 below row 4: 7036
maximum number between index numbers 1 and 2: 7036
Replace listOfLists[rownumber][rownumbercompare] listOfLists[3][1] with 53 + 7036 = 7089
Row 5 below row 4 [6961, 7002, 7036, 7035, 6998] replaced with maximums sums starting row 3
number row 4: 6
index number 2 row 5 below row 4: 7036
index number 3 row 5 below row 4: 7035
maximum number between index numbers 2 and 3: 7036
Replace listOfLists[rownumber][rownumbercompare] listOfLists[3][2] with 6 + 7036 = 7042
Row 5 below row 4 [6961, 7002, 7036, 7035, 6998] replaced with maximums sums starting row 3
number row 4: 34
index number 3 row 5 below row 4: 7035
index number 4 row 5 below row 4: 6998
maximum number between index numbers 3 and 4: 7035
Replace listOfLists[rownumber][rownumbercompare] listOfLists[3][3] with 34 + 7035 = 7069


TRUE ROW NUMBER 3 [52, 40, 9]
Row 4 below row 3 [7028, 7089, 7042, 7069] replaced with maximums sums starting row 2
number row 3: 52
index number 0 row 4 below row 3: 7028
index number 1 row 4 below row 3: 7089
maximum number between index numbers 0 and 1: 7089
Replace listOfLists[rownumber][rownumbercompare] listOfLists[2][0] with 52 + 7089 = 7141
Row 4 below row 3 [7028, 7089, 7042, 7069] replaced with maximums sums starting row 2
number row 3: 40
index number 1 row 4 below row 3: 7089
index number 2 row 4 below row 3: 7042
maximum number between index numbers 1 and 2: 7089
Replace listOfLists[rownumber][rownumbercompare] listOfLists[2][1] with 40 + 7089 = 7129
Row 4 below row 3 [7028, 7089, 7042, 7069] replaced with maximums sums starting row 2
number row 3: 9
index number 2 row 4 below row 3: 7042
index number 3 row 4 below row 3: 7069
maximum number between index numbers 2 and 3: 7069
Replace listOfLists[rownumber][rownumbercompare] listOfLists[2][2] with 9 + 7069 = 7078


TRUE ROW NUMBER 2 [73, 41]
Row 3 below row 2 [7141, 7129, 7078] replaced with maximums sums starting row 1
number row 2: 73
index number 0 row 3 below row 2: 7141
index number 1 row 3 below row 2: 7129
maximum number between index numbers 0 and 1: 7141
Replace listOfLists[rownumber][rownumbercompare] listOfLists[1][0] with 73 + 7141 = 7214
Row 3 below row 2 [7141, 7129, 7078] replaced with maximums sums starting row 1
number row 2: 41
index number 1 row 3 below row 2: 7129
index number 2 row 3 below row 2: 7078
maximum number between index numbers 1 and 2: 7129
Replace listOfLists[rownumber][rownumbercompare] listOfLists[1][1] with 41 + 7129 = 7170


TRUE ROW NUMBER 1 [59]
Row 2 below row 1 [7214, 7170] replaced with maximums sums starting row 0
number row 1: 59
index number 0 row 2 below row 1: 7214
index number 1 row 2 below row 1: 7170
maximum number between index numbers 0 and 1: 7214
Replace listOfLists[rownumber][rownumbercompare] listOfLists[0][0] with 59 + 7214 = 7273
'''
