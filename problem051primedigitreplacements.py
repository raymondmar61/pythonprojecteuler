#YouTube Project Euler Problem 51： Prime Digit Replacements [eqLcm2UAf00].  RM:  incorrect code.  Get's answer correctly.
#YouTube Project Euler： Problem 51 (C⧸C++) [XAl7p3DL8H4].  A family is defined as set of primes which can be formed by starting with a particular prime number and picking a particular digit or digits in the particular prime number and replacing the digit or digits with other digit or digits to form another prime number.  All of the new primes composed with the initial prime number is the family.  From numbers 10 to 99, 13, 23, 43, 53, 73, and 83 is a family because the first digit is replaced and the second digit is a 3 not changed.  56003, 56113, 56333, 56443, 56663, 56773, and 56993 is a seven prime family for which 56003 is the first family member.
#Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
#RM:  the print samples before the Python code print("family list",family) are for howmanynumbers = 100 and familytargetnumber = 8
from datetime import datetime
import math

print(datetime.now().strftime("%H:%M:%S"))
howmanynumbers = 100000
familytargetnumber = 7
isprime = [True] * (howmanynumbers+1) #create a isprime list its index numbers is the list of numbers initial set to True.  All numbers are prime numbers initially.
#print(isprime) #print [True, True, True, True, , . . ., True]
isprime[0] = isprime[1] = False #0 and 1 are not prime numbers.  Set to False
#print(isprime) #print [False, False, True, True, . . ., True]

#check number is prime
upperlimitiloop = int(math.sqrt(howmanynumbers)+1)
#print("i range upper limit",upperlimitiloop) #print i range upper limit 11
for i in range(2, int(math.sqrt(howmanynumbers)+1)):
    #print(i) #print 2
    if isprime[i]==True:
        #print("prime number",i) #print prime number 2
        #print("prime number True",isprime[i]) #print prime number True True
        kwhileloop = i * i
        #print("kwhileloop is i*i=",kwhileloop) #print kwhileloop is i*i= 4
        #while loop set the number or the index number in isprime list to False because it's not a prime number
        while kwhileloop <= howmanynumbers:
            isprime[kwhileloop] = False
            kwhileloop+=i
            # print("kwhileloop=kwhileloop+i",kwhileloop)
            '''
            kwhileloop=kwhileloop+i 6
            kwhileloop=kwhileloop+i 8
            kwhileloop=kwhileloop+i 10
            kwhileloop=kwhileloop+i 12
            kwhileloop=kwhileloop+i 14
            ...
            '''

#return prime numbers which is the isprime list index number
# for index, value in list(enumerate(isprime)):
#     if value == True:
#         print("prime number",index)
#         '''
#         prime number 2
#         prime number 3
#         prime number 5
#         prime number 7
#         prime number 11
#         prime number 13
#         ...
#         '''

family = []
for i in range(howmanynumbers):
    if isprime[i] == True:
        #find the other numbers in family
        stringi = str(i)
        numberofprimes = 0
        for eachdigitstringi in stringi:
            numberofprimes = 0
            family = []
            for digit in range(0,10):
                checknumber = int(stringi.replace(eachdigitstringi,str(digit)))
                if checknumber >= i:
                    family.append(checknumber)
            #count how many are primes numbers and break if match familytargetnumber
            for eachfamily in family:
                if isprime[eachfamily]:
                    numberofprimes+=1
            if numberofprimes == familytargetnumber:
                break
        if numberofprimes == familytargetnumber:
            break

print("family list",family) #print family list [121313, 222323, 323333, 424343, 525353, 626363, 727373, 828383, 929393]
print("familytargetnumber number",familytargetnumber) #print familytargetnumber number 8
print(datetime.now().strftime("%H:%M:%S"))