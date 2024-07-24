#https://zach.se/project-euler-solutions/26/
def recurringdecimalcycle(numerator, denominator):
    #solve 10^start % denominator == 10^(start+length) % denominator
    for length in range(1, denominator):
        # print("length:", length)
        # print((10**length) % denominator)
        if 1 == (10**length) % denominator:
            return length
    return 0


longestrecurring = []
for i in range(2, 1001):
    # print("i", i)
    longestrecurring.append(recurringdecimalcycle(1, i))
    # print("\n")
longestrecurring.sort()
print(longestrecurring) #print [0, 0, 0, 0, 0, 0, . . ., 862, 886, 936, 940, 952, 970, 976, 982]
print(max(longestrecurring)) #print 982
largestrecurringdecimaldenominator = max(longestrecurring)
# print(largestrecurringdecimaldenominator) #print 982
for i in range(2, 1001):
    if recurringdecimalcycle(1, i) == largestrecurringdecimaldenominator:
        denominatorwithlargestrecurringdecimal = i
        print(i) #print 983