#Project Euler Problem 62： Cubic Permutations [-5oVgz4zaA8].mp4
'''
Cubic Permutations
Problem 62

The cube, 41063625 345^3 can be permuted to produce two other cubes: 56623104 384^3 and 66430125 405^3.  In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''
cubesdictionary = {}
findcube = 0
#Find the cubes or raise numbers to the third power
for findcube in range(1, 10000):
    cube = findcube**3
    permutationarray = [*str(cube)]
    #print(findcube, cube, permutationarray)
    '''
    1 1 ['1']
    2 8 ['8']
    3 27 ['2', '7']
    4 64 ['6', '4']
    5 125 ['1', '2', '5']
    6 216 ['2', '1', '6']
    7 343 ['3', '4', '3']
    8 512 ['5', '1', '2']
    9 729 ['7', '2', '9']
    10 1000 ['1', '0', '0', '0']
    ...
    '''
    permutationarray.sort() #sort permutationarray each number ascending or from lowest to highest because want to find the smallest cube permutation.  The smallest permutation of 512 is 125.  1000 is 0001.
    smallestpermutation = "".join(permutationarray)
    #print("smallestpermutation", smallestpermutation) #print 1 8 27 46 125 126 334 125 279 0001
    data = (cube, 1)
    #print("cubesdictionary", cubesdictionary) #print {'1': (1, 1), '8': (8, 1), '27': (27, 1), '46': (64, 1), '125': (125, 2), '126': (216, 1), '334': (343, 1), '279': (729, 1)}
    #If statement check if a sorted permutation is already in cubes dictionary; for example 8**3 is 512.  Sort 512 is 125.  125 is 5**3.  If yes, the add 1 to the counter.  The counter is the second index entry in the tuple variable data.  125 appears twice.  Tuple data variable is (125, 2).
    if smallestpermutation in cubesdictionary:
        #print(smallestpermutation, "is in", cubesdictionary) #print 125 is in {'1': (1, 1), '8': (8, 1), '27': (27, 1), '46': (64, 1), '125': (125, 1), '126': (216, 1), '334': (343, 1)}
        data = cubesdictionary[smallestpermutation]
        #print(data) #print(125, 1)
        data = (data[0], data[1] + 1)
        #print(data) #print #print(125, 2)
    #print("data", data) #print (1, 1) (8, 1) (27, 1) (64, 1) (125, 1) (216, 1) (343, 1) (729, 1) (1000, 1) RM:  No (512, 1) from 8**3
    #print(data) #print (1, 1) (8, 1) (27, 1) (64, 1) (125, 1) (216, 1) (343, 1) (125, 2) (729, 1) (1000, 1)
    cubesdictionary[smallestpermutation] = data #Add current data to cubesdictionary
    #print(cubesdictionary) #print {'1': (1, 1), '8': (8, 1), '27': (27, 1), '46': (64, 1), '125': (125, 2), '126': (216, 1), '334': (343, 1), '279': (729, 1), '0001': (1000, 1)}

#Find the smallest cube with five permutations of its digits are cube.
smallestcube = 10000000000000000000000000
for data in cubesdictionary.values():
    if data[1] == 5 and data[0] < smallestcube:
        print(data) #print (127035954683, 5).  There are five permutations in 127035954683.  127035954683 is the smallest cube in the permutation.
        smallestcube = data[0]
print(smallestcube) #print 127035954683