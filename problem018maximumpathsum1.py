list18 = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
list18 = [[75], [95, 64], [17, 47, 82], [18, 35, 87, 10], [20, 4, 82, 47, 65], [19, 1, 23, 75, 3, 34], [88, 2, 77, 73, 7, 63, 67], [99, 65, 4, 28, 6, 16, 70, 92], [41, 41, 26, 56, 83, 40, 80, 70, 33], [41, 48, 72, 33, 47, 32, 37, 16, 94, 29], [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31], [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]
print(list18) #print [[75], [95, 64], [17, 47, 82], [18, 35, 87, 10], [20, 4, 82, 47, 65], [19, 1, 23, 75, 3, 34], [88, 2, 77, 73, 7, 63, 67], [99, 65, 4, 28, 6, 16, 70, 92]]
print(list18[2][1]) #print 47
print(len(list18)) #print 8
print("\n")
numberofrows = len(list18)
maxnumberlistindex = 0
maxnumberlistindexchecknextindex = 1
cumulatedsum = list18[0][0]
print("Initialize cumulatedsum", cumulatedsum)

for rownumber in range(1, numberofrows):
    print("Row number", len(list18[rownumber]))
    print(list18[rownumber])
    # print("index+0", maxnumberlistindex)
    # print("index+1", maxnumberlistindexchecknextindex)
    # print("index+0 number", list18[rownumber][maxnumberlistindex])
    # print("index+1 number", list18[rownumber][maxnumberlistindexchecknextindex])
    # print("Larger number", max(list18[rownumber][maxnumberlistindex], list18[rownumber][maxnumberlistindexchecknextindex]))
    maxnumber = max(list18[rownumber][maxnumberlistindex], list18[rownumber][maxnumberlistindexchecknextindex])
    if list18[rownumber][maxnumberlistindex] >= list18[rownumber][maxnumberlistindexchecknextindex]:
        maxnumbereachrowindexposition = maxnumberlistindex
    else:
        maxnumbereachrowindexposition = maxnumberlistindexchecknextindex
    cumulatedsum = cumulatedsum + maxnumber
    print("cumulatedsum", cumulatedsum)
    maxnumberlistindex = maxnumbereachrowindexposition
    maxnumberlistindexchecknextindex = maxnumbereachrowindexposition + 1
    print("\n")

print(cumulatedsum) #print 1064

#Best explanation after clicking top Google search results Google search "maximum path sum 1 problem 18 project euler."  https://www.educative.io/answers/how-to-solve-project-euler--sharp18---maximum-path-sum-problem.  The question asked the maximum or highest path from top to bottom returning the largest sum.  It's not necessarily the maximum number on every row.  Example 16; 7, 8; 10, 91, 4; 100, 3, 2, 11;  The correct answer is 16+7+10+100=133, not 16+8+91+3=118.  It's the path returning the largest sum from top the bottom.  The 133 is the largest sum path from top to bottom connecting adjacent numbers.
#https://raw.org/puzzle/project-euler/problem-18/
listOfLists = [[75], [95, 64], [17, 47, 82], [18, 35, 87, 10], [20, 4, 82, 47, 65], [19, 1, 23, 75, 3, 34], [88, 2, 77, 73, 7, 63, 67], [99, 65, 4, 28, 6, 16, 70, 92], [41, 41, 26, 56, 83, 40, 80, 70, 33], [41, 48, 72, 33, 47, 32, 37, 16, 94, 29], [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31], [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]
print("Number of rows", len(listOfLists)) #print Number of rows 15
print("Start checking rows at the", len(listOfLists) - 2, "th index row.") #print Start checking rows at the 13 th index row.
for rownumber in range(len(listOfLists) - 2, -1, -1):
    print(rownumber) #print from 13 to 0
    print(listOfLists[rownumber])
'''

'''
print("\n")
for rownumber in range(len(listOfLists) - 2, -1, -1):
    print("TRUE ROW NUMBER", rownumber + 1, listOfLists[rownumber])
    indexcounter = 0
    for rownumbercompare in range(len(listOfLists[rownumber])):
        # print("row number compare", rownumbercompare + 1)
        # print("row number compare list", listOfLists[rownumbercompare])
        print("Row", rownumber + 2, "below row", rownumber + 1, listOfLists[rownumber + 1], "replaced with maximums sums starting row 13.")
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
TRUE ROW NUMBER 14 [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
Row 15 below row 14 [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23] replaced with maximums sums starting row 13.
number row 14: 63
index number 0 row 15 below row 14: 4
index number 1 row 15 below row 14: 62
maximum number between index numbers 0 and 1: 62
Replace listOfLists[rownumber][rownumbercompare] listOfLists[13][0] with 63 + 62 = 125
Row 15 below row 14 [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23] replaced with maximums sums starting row 13.
number row 14: 66
index number 1 row 15 below row 14: 62
index number 2 row 15 below row 14: 98
maximum number between index numbers 1 and 2: 98
Replace listOfLists[rownumber][rownumbercompare] listOfLists[13][1] with 66 + 98 = 164
Row 15 below row 14 [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23] replaced with maximums sums starting row 13.
number row 14: 4
index number 2 row 15 below row 14: 98
index number 3 row 15 below row 14: 27
maximum number between index numbers 2 and 3: 98
Replace listOfLists[rownumber][rownumbercompare] listOfLists[13][2] with 4 + 98 = 102
Row 15 below row 14 [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23] replaced with maximums sums starting row 13.
number row 14: 68
index number 3 row 15 below row 14: 27
index number 4 row 15 below row 14: 23
maximum number between index numbers 3 and 4: 27
Replace listOfLists[rownumber][rownumbercompare] listOfLists[13][3] with 68 + 27 = 95
Row 15 below row 14 [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23] replaced with maximums sums starting row 13.
number row 14: 89
index number 4 row 15 below row 14: 23
index number 5 row 15 below row 14: 9
maximum number between index numbers 4 and 5: 23
Replace listOfLists[rownumber][rownumbercompare] listOfLists[13][4] with 89 + 23 = 112
Row 15 below row 14 [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23] replaced with maximums sums starting row 13.
number row 14: 53
index number 5 row 15 below row 14: 9
index number 6 row 15 below row 14: 70
maximum number between index numbers 5 and 6: 70
Replace listOfLists[rownumber][rownumbercompare] listOfLists[13][5] with 53 + 70 = 123
Row 15 below row 14 [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23] replaced with maximums sums starting row 13.
number row 14: 67
index number 6 row 15 below row 14: 70
index number 7 row 15 below row 14: 98
maximum number between index numbers 6 and 7: 98
Replace listOfLists[rownumber][rownumbercompare] listOfLists[13][6] with 67 + 98 = 165
Row 15 below row 14 [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23] replaced with maximums sums starting row 13.
number row 14: 30
index number 7 row 15 below row 14: 98
index number 8 row 15 below row 14: 73
maximum number between index numbers 7 and 8: 98
Replace listOfLists[rownumber][rownumbercompare] listOfLists[13][7] with 30 + 98 = 128
Row 15 below row 14 [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23] replaced with maximums sums starting row 13.
number row 14: 73
index number 8 row 15 below row 14: 73
index number 9 row 15 below row 14: 93
maximum number between index numbers 8 and 9: 93
Replace listOfLists[rownumber][rownumbercompare] listOfLists[13][8] with 73 + 93 = 166
Row 15 below row 14 [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23] replaced with maximums sums starting row 13.
number row 14: 16
index number 9 row 15 below row 14: 93
index number 10 row 15 below row 14: 38
maximum number between index numbers 9 and 10: 93
Replace listOfLists[rownumber][rownumbercompare] listOfLists[13][9] with 16 + 93 = 109
Row 15 below row 14 [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23] replaced with maximums sums starting row 13.
number row 14: 69
index number 10 row 15 below row 14: 38
index number 11 row 15 below row 14: 53
maximum number between index numbers 10 and 11: 53
Replace listOfLists[rownumber][rownumbercompare] listOfLists[13][10] with 69 + 53 = 122
Row 15 below row 14 [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23] replaced with maximums sums starting row 13.
number row 14: 87
index number 11 row 15 below row 14: 53
index number 12 row 15 below row 14: 60
maximum number between index numbers 11 and 12: 60
Replace listOfLists[rownumber][rownumbercompare] listOfLists[13][11] with 87 + 60 = 147
Row 15 below row 14 [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23] replaced with maximums sums starting row 13.
number row 14: 40
index number 12 row 15 below row 14: 60
index number 13 row 15 below row 14: 4
maximum number between index numbers 12 and 13: 60
Replace listOfLists[rownumber][rownumbercompare] listOfLists[13][12] with 40 + 60 = 100
Row 15 below row 14 [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23] replaced with maximums sums starting row 13.
number row 14: 31
index number 13 row 15 below row 14: 4
index number 14 row 15 below row 14: 23
maximum number between index numbers 13 and 14: 23
Replace listOfLists[rownumber][rownumbercompare] listOfLists[13][13] with 31 + 23 = 54


TRUE ROW NUMBER 13 [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
Row 14 below row 13 [125, 164, 102, 95, 112, 123, 165, 128, 166, 109, 122, 147, 100, 54] replaced with maximums sums starting row 13.
number row 13: 91
index number 0 row 14 below row 13: 125
index number 1 row 14 below row 13: 164
maximum number between index numbers 0 and 1: 164
Replace listOfLists[rownumber][rownumbercompare] listOfLists[12][0] with 91 + 164 = 255
Row 14 below row 13 [125, 164, 102, 95, 112, 123, 165, 128, 166, 109, 122, 147, 100, 54] replaced with maximums sums starting row 13.
number row 13: 71
index number 1 row 14 below row 13: 164
index number 2 row 14 below row 13: 102
maximum number between index numbers 1 and 2: 164
Replace listOfLists[rownumber][rownumbercompare] listOfLists[12][1] with 71 + 164 = 235
Row 14 below row 13 [125, 164, 102, 95, 112, 123, 165, 128, 166, 109, 122, 147, 100, 54] replaced with maximums sums starting row 13.
number row 13: 52
index number 2 row 14 below row 13: 102
index number 3 row 14 below row 13: 95
maximum number between index numbers 2 and 3: 102
Replace listOfLists[rownumber][rownumbercompare] listOfLists[12][2] with 52 + 102 = 154
Row 14 below row 13 [125, 164, 102, 95, 112, 123, 165, 128, 166, 109, 122, 147, 100, 54] replaced with maximums sums starting row 13.
number row 13: 38
index number 3 row 14 below row 13: 95
index number 4 row 14 below row 13: 112
maximum number between index numbers 3 and 4: 112
Replace listOfLists[rownumber][rownumbercompare] listOfLists[12][3] with 38 + 112 = 150
Row 14 below row 13 [125, 164, 102, 95, 112, 123, 165, 128, 166, 109, 122, 147, 100, 54] replaced with maximums sums starting row 13.
number row 13: 17
index number 4 row 14 below row 13: 112
index number 5 row 14 below row 13: 123
maximum number between index numbers 4 and 5: 123
Replace listOfLists[rownumber][rownumbercompare] listOfLists[12][4] with 17 + 123 = 140
Row 14 below row 13 [125, 164, 102, 95, 112, 123, 165, 128, 166, 109, 122, 147, 100, 54] replaced with maximums sums starting row 13.
number row 13: 14
index number 5 row 14 below row 13: 123
index number 6 row 14 below row 13: 165
maximum number between index numbers 5 and 6: 165
Replace listOfLists[rownumber][rownumbercompare] listOfLists[12][5] with 14 + 165 = 179
Row 14 below row 13 [125, 164, 102, 95, 112, 123, 165, 128, 166, 109, 122, 147, 100, 54] replaced with maximums sums starting row 13.
number row 13: 91
index number 6 row 14 below row 13: 165
index number 7 row 14 below row 13: 128
maximum number between index numbers 6 and 7: 165
Replace listOfLists[rownumber][rownumbercompare] listOfLists[12][6] with 91 + 165 = 256
Row 14 below row 13 [125, 164, 102, 95, 112, 123, 165, 128, 166, 109, 122, 147, 100, 54] replaced with maximums sums starting row 13.
number row 13: 43
index number 7 row 14 below row 13: 128
index number 8 row 14 below row 13: 166
maximum number between index numbers 7 and 8: 166
Replace listOfLists[rownumber][rownumbercompare] listOfLists[12][7] with 43 + 166 = 209
Row 14 below row 13 [125, 164, 102, 95, 112, 123, 165, 128, 166, 109, 122, 147, 100, 54] replaced with maximums sums starting row 13.
number row 13: 58
index number 8 row 14 below row 13: 166
index number 9 row 14 below row 13: 109
maximum number between index numbers 8 and 9: 166
Replace listOfLists[rownumber][rownumbercompare] listOfLists[12][8] with 58 + 166 = 224
Row 14 below row 13 [125, 164, 102, 95, 112, 123, 165, 128, 166, 109, 122, 147, 100, 54] replaced with maximums sums starting row 13.
number row 13: 50
index number 9 row 14 below row 13: 109
index number 10 row 14 below row 13: 122
maximum number between index numbers 9 and 10: 122
Replace listOfLists[rownumber][rownumbercompare] listOfLists[12][9] with 50 + 122 = 172
Row 14 below row 13 [125, 164, 102, 95, 112, 123, 165, 128, 166, 109, 122, 147, 100, 54] replaced with maximums sums starting row 13.
number row 13: 27
index number 10 row 14 below row 13: 122
index number 11 row 14 below row 13: 147
maximum number between index numbers 10 and 11: 147
Replace listOfLists[rownumber][rownumbercompare] listOfLists[12][10] with 27 + 147 = 174
Row 14 below row 13 [125, 164, 102, 95, 112, 123, 165, 128, 166, 109, 122, 147, 100, 54] replaced with maximums sums starting row 13.
number row 13: 29
index number 11 row 14 below row 13: 147
index number 12 row 14 below row 13: 100
maximum number between index numbers 11 and 12: 147
Replace listOfLists[rownumber][rownumbercompare] listOfLists[12][11] with 29 + 147 = 176
Row 14 below row 13 [125, 164, 102, 95, 112, 123, 165, 128, 166, 109, 122, 147, 100, 54] replaced with maximums sums starting row 13.
number row 13: 48
index number 12 row 14 below row 13: 100
index number 13 row 14 below row 13: 54
maximum number between index numbers 12 and 13: 100
Replace listOfLists[rownumber][rownumbercompare] listOfLists[12][12] with 48 + 100 = 148


TRUE ROW NUMBER 12 [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
Row 13 below row 12 [255, 235, 154, 150, 140, 179, 256, 209, 224, 172, 174, 176, 148] replaced with maximums sums starting row 13.
number row 12: 70
index number 0 row 13 below row 12: 255
index number 1 row 13 below row 12: 235
maximum number between index numbers 0 and 1: 255
Replace listOfLists[rownumber][rownumbercompare] listOfLists[11][0] with 70 + 255 = 325
Row 13 below row 12 [255, 235, 154, 150, 140, 179, 256, 209, 224, 172, 174, 176, 148] replaced with maximums sums starting row 13.
number row 12: 11
index number 1 row 13 below row 12: 235
index number 2 row 13 below row 12: 154
maximum number between index numbers 1 and 2: 235
Replace listOfLists[rownumber][rownumbercompare] listOfLists[11][1] with 11 + 235 = 246
Row 13 below row 12 [255, 235, 154, 150, 140, 179, 256, 209, 224, 172, 174, 176, 148] replaced with maximums sums starting row 13.
number row 12: 33
index number 2 row 13 below row 12: 154
index number 3 row 13 below row 12: 150
maximum number between index numbers 2 and 3: 154
Replace listOfLists[rownumber][rownumbercompare] listOfLists[11][2] with 33 + 154 = 187
Row 13 below row 12 [255, 235, 154, 150, 140, 179, 256, 209, 224, 172, 174, 176, 148] replaced with maximums sums starting row 13.
number row 12: 28
index number 3 row 13 below row 12: 150
index number 4 row 13 below row 12: 140
maximum number between index numbers 3 and 4: 150
Replace listOfLists[rownumber][rownumbercompare] listOfLists[11][3] with 28 + 150 = 178
Row 13 below row 12 [255, 235, 154, 150, 140, 179, 256, 209, 224, 172, 174, 176, 148] replaced with maximums sums starting row 13.
number row 12: 77
index number 4 row 13 below row 12: 140
index number 5 row 13 below row 12: 179
maximum number between index numbers 4 and 5: 179
Replace listOfLists[rownumber][rownumbercompare] listOfLists[11][4] with 77 + 179 = 256
Row 13 below row 12 [255, 235, 154, 150, 140, 179, 256, 209, 224, 172, 174, 176, 148] replaced with maximums sums starting row 13.
number row 12: 73
index number 5 row 13 below row 12: 179
index number 6 row 13 below row 12: 256
maximum number between index numbers 5 and 6: 256
Replace listOfLists[rownumber][rownumbercompare] listOfLists[11][5] with 73 + 256 = 329
Row 13 below row 12 [255, 235, 154, 150, 140, 179, 256, 209, 224, 172, 174, 176, 148] replaced with maximums sums starting row 13.
number row 12: 17
index number 6 row 13 below row 12: 256
index number 7 row 13 below row 12: 209
maximum number between index numbers 6 and 7: 256
Replace listOfLists[rownumber][rownumbercompare] listOfLists[11][6] with 17 + 256 = 273
Row 13 below row 12 [255, 235, 154, 150, 140, 179, 256, 209, 224, 172, 174, 176, 148] replaced with maximums sums starting row 13.
number row 12: 78
index number 7 row 13 below row 12: 209
index number 8 row 13 below row 12: 224
maximum number between index numbers 7 and 8: 224
Replace listOfLists[rownumber][rownumbercompare] listOfLists[11][7] with 78 + 224 = 302
Row 13 below row 12 [255, 235, 154, 150, 140, 179, 256, 209, 224, 172, 174, 176, 148] replaced with maximums sums starting row 13.
number row 12: 39
index number 8 row 13 below row 12: 224
index number 9 row 13 below row 12: 172
maximum number between index numbers 8 and 9: 224
Replace listOfLists[rownumber][rownumbercompare] listOfLists[11][8] with 39 + 224 = 263
Row 13 below row 12 [255, 235, 154, 150, 140, 179, 256, 209, 224, 172, 174, 176, 148] replaced with maximums sums starting row 13.
number row 12: 68
index number 9 row 13 below row 12: 172
index number 10 row 13 below row 12: 174
maximum number between index numbers 9 and 10: 174
Replace listOfLists[rownumber][rownumbercompare] listOfLists[11][9] with 68 + 174 = 242
Row 13 below row 12 [255, 235, 154, 150, 140, 179, 256, 209, 224, 172, 174, 176, 148] replaced with maximums sums starting row 13.
number row 12: 17
index number 10 row 13 below row 12: 174
index number 11 row 13 below row 12: 176
maximum number between index numbers 10 and 11: 176
Replace listOfLists[rownumber][rownumbercompare] listOfLists[11][10] with 17 + 176 = 193
Row 13 below row 12 [255, 235, 154, 150, 140, 179, 256, 209, 224, 172, 174, 176, 148] replaced with maximums sums starting row 13.
number row 12: 57
index number 11 row 13 below row 12: 176
index number 12 row 13 below row 12: 148
maximum number between index numbers 11 and 12: 176
Replace listOfLists[rownumber][rownumbercompare] listOfLists[11][11] with 57 + 176 = 233


TRUE ROW NUMBER 11 [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
Row 12 below row 11 [325, 246, 187, 178, 256, 329, 273, 302, 263, 242, 193, 233] replaced with maximums sums starting row 13.
number row 11: 53
index number 0 row 12 below row 11: 325
index number 1 row 12 below row 11: 246
maximum number between index numbers 0 and 1: 325
Replace listOfLists[rownumber][rownumbercompare] listOfLists[10][0] with 53 + 325 = 378
Row 12 below row 11 [325, 246, 187, 178, 256, 329, 273, 302, 263, 242, 193, 233] replaced with maximums sums starting row 13.
number row 11: 71
index number 1 row 12 below row 11: 246
index number 2 row 12 below row 11: 187
maximum number between index numbers 1 and 2: 246
Replace listOfLists[rownumber][rownumbercompare] listOfLists[10][1] with 71 + 246 = 317
Row 12 below row 11 [325, 246, 187, 178, 256, 329, 273, 302, 263, 242, 193, 233] replaced with maximums sums starting row 13.
number row 11: 44
index number 2 row 12 below row 11: 187
index number 3 row 12 below row 11: 178
maximum number between index numbers 2 and 3: 187
Replace listOfLists[rownumber][rownumbercompare] listOfLists[10][2] with 44 + 187 = 231
Row 12 below row 11 [325, 246, 187, 178, 256, 329, 273, 302, 263, 242, 193, 233] replaced with maximums sums starting row 13.
number row 11: 65
index number 3 row 12 below row 11: 178
index number 4 row 12 below row 11: 256
maximum number between index numbers 3 and 4: 256
Replace listOfLists[rownumber][rownumbercompare] listOfLists[10][3] with 65 + 256 = 321
Row 12 below row 11 [325, 246, 187, 178, 256, 329, 273, 302, 263, 242, 193, 233] replaced with maximums sums starting row 13.
number row 11: 25
index number 4 row 12 below row 11: 256
index number 5 row 12 below row 11: 329
maximum number between index numbers 4 and 5: 329
Replace listOfLists[rownumber][rownumbercompare] listOfLists[10][4] with 25 + 329 = 354
Row 12 below row 11 [325, 246, 187, 178, 256, 329, 273, 302, 263, 242, 193, 233] replaced with maximums sums starting row 13.
number row 11: 43
index number 5 row 12 below row 11: 329
index number 6 row 12 below row 11: 273
maximum number between index numbers 5 and 6: 329
Replace listOfLists[rownumber][rownumbercompare] listOfLists[10][5] with 43 + 329 = 372
Row 12 below row 11 [325, 246, 187, 178, 256, 329, 273, 302, 263, 242, 193, 233] replaced with maximums sums starting row 13.
number row 11: 91
index number 6 row 12 below row 11: 273
index number 7 row 12 below row 11: 302
maximum number between index numbers 6 and 7: 302
Replace listOfLists[rownumber][rownumbercompare] listOfLists[10][6] with 91 + 302 = 393
Row 12 below row 11 [325, 246, 187, 178, 256, 329, 273, 302, 263, 242, 193, 233] replaced with maximums sums starting row 13.
number row 11: 52
index number 7 row 12 below row 11: 302
index number 8 row 12 below row 11: 263
maximum number between index numbers 7 and 8: 302
Replace listOfLists[rownumber][rownumbercompare] listOfLists[10][7] with 52 + 302 = 354
Row 12 below row 11 [325, 246, 187, 178, 256, 329, 273, 302, 263, 242, 193, 233] replaced with maximums sums starting row 13.
number row 11: 97
index number 8 row 12 below row 11: 263
index number 9 row 12 below row 11: 242
maximum number between index numbers 8 and 9: 263
Replace listOfLists[rownumber][rownumbercompare] listOfLists[10][8] with 97 + 263 = 360
Row 12 below row 11 [325, 246, 187, 178, 256, 329, 273, 302, 263, 242, 193, 233] replaced with maximums sums starting row 13.
number row 11: 51
index number 9 row 12 below row 11: 242
index number 10 row 12 below row 11: 193
maximum number between index numbers 9 and 10: 242
Replace listOfLists[rownumber][rownumbercompare] listOfLists[10][9] with 51 + 242 = 293
Row 12 below row 11 [325, 246, 187, 178, 256, 329, 273, 302, 263, 242, 193, 233] replaced with maximums sums starting row 13.
number row 11: 14
index number 10 row 12 below row 11: 193
index number 11 row 12 below row 11: 233
maximum number between index numbers 10 and 11: 233
Replace listOfLists[rownumber][rownumbercompare] listOfLists[10][10] with 14 + 233 = 247

...

TRUE ROW NUMBER 3 [17, 47, 82]
Row 4 below row 3 [704, 801, 853, 792] replaced with maximums sums starting row 13.
number row 3: 17
index number 0 row 4 below row 3: 704
index number 1 row 4 below row 3: 801
maximum number between index numbers 0 and 1: 801
Replace listOfLists[rownumber][rownumbercompare] listOfLists[2][0] with 17 + 801 = 818
Row 4 below row 3 [704, 801, 853, 792] replaced with maximums sums starting row 13.
number row 3: 47
index number 1 row 4 below row 3: 801
index number 2 row 4 below row 3: 853
maximum number between index numbers 1 and 2: 853
Replace listOfLists[rownumber][rownumbercompare] listOfLists[2][1] with 47 + 853 = 900
Row 4 below row 3 [704, 801, 853, 792] replaced with maximums sums starting row 13.
number row 3: 82
index number 2 row 4 below row 3: 853
index number 3 row 4 below row 3: 792
maximum number between index numbers 2 and 3: 853
Replace listOfLists[rownumber][rownumbercompare] listOfLists[2][2] with 82 + 853 = 935


TRUE ROW NUMBER 2 [95, 64]
Row 3 below row 2 [818, 900, 935] replaced with maximums sums starting row 13.
number row 2: 95
index number 0 row 3 below row 2: 818
index number 1 row 3 below row 2: 900
maximum number between index numbers 0 and 1: 900
Replace listOfLists[rownumber][rownumbercompare] listOfLists[1][0] with 95 + 900 = 995
Row 3 below row 2 [818, 900, 935] replaced with maximums sums starting row 13.
number row 2: 64
index number 1 row 3 below row 2: 900
index number 2 row 3 below row 2: 935
maximum number between index numbers 1 and 2: 935
Replace listOfLists[rownumber][rownumbercompare] listOfLists[1][1] with 64 + 935 = 999


TRUE ROW NUMBER 1 [75]
Row 2 below row 1 [995, 999] replaced with maximums sums starting row 13.
number row 1: 75
index number 0 row 2 below row 1: 995
index number 1 row 2 below row 1: 999
maximum number between index numbers 0 and 1: 999
Replace listOfLists[rownumber][rownumbercompare] listOfLists[0][0] with 75 + 999 = 1074
'''
