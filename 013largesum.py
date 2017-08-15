#https://projecteuler.net/problem=13 Large sum
#https://projecteuler.net/thread=13
#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

# number = "37107287533902102798797998220837590246510135740250"
# n = 0
# for eachnumber in number:
#     n = n + int(eachnumber)
# print(n) #print 214
#RM:  The question is adding each line of 50-digit numbers.  The question is not adding each digit in the one-hundred 50-digit numbers.

with open("013largesum.txt","r") as file_object:
    lines3 = file_object.readlines()    
print(lines3)
print(len(lines3))
print(type(lines3))
n = 0
for eachlines3 in lines3:
    print(n)
    n = n + int(eachlines3)
print("\n")
print(n) #print 5537376230390876637302048746832985971773659831892672
print(str(n)[0:10]) #print 5537376230
