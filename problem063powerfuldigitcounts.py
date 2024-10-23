#Project Euler Problem 63 Powerful Digit Counts
#Project Euler Problem 63： Powerful Digit Counts [09FqJLTBMv4]
#The 5-digit number, 16807=7^5, is also a fifth power.  Similarily, the 9-digit number, 134217728=8^9, is a ninth power.  How many n-digit positive integers exist which are also an nth power?
print(7**5) #print 16807
print(len(str(7**5))) #print 5
print(8**9) #print 134217728
print(len(str(8**9))) #print 9
print("\n")
print(1**1) #print 1
print(len(str(1**1))) #print 1
print(4**2) #print 16
print(len(str(4**2))) #print 2
print(5**3) #print 125
print(len(str(5**3))) #print 3
print(6**4) #print 1296
print(len(str(6**4))) #print 4
print(7**6) #print 117649
print(len(str(7**6))) #print 6
print(8**7) #print 2097152
print(len(str(8**7))) #print 7
print(9**10) #print 3486784401
print(len(str(9**10))) #print 10
print(9**11) #print 31381059609
print(len(str(9**11))) #print 11
print("\n")
print(10**11) #print 100000000000
print(len(str(10**11))) #print 12
print(10**12) #print 1000000000000
print(len(str(10**12))) #print 13
print(11**9) #print 2357947691
print(len(str(11**9))) #print 10
print(11**10) #print 25937424601
print(len(str(11**10))) #print 11
print(11**11) #print 285311670611
print(len(str(11**11))) #print 12
print(12**7) #print 35831808
print(len(str(12**7))) #print 8
print(12**8) #print 429981696
print(len(str(12**8))) #print 9
print(12**9) #print 5159780352
print(len(str(12**9))) #print 10
print(12**10) #print 61917364224
print(len(str(12**10))) #print 11
print(12**11) #print 743008370688
print(len(str(12**11))) #print 12
print(12**12) #print 8916100448256
print(len(str(12**12))) #print 13

counter = 1 #Automatically add 1 to counter because any exponent raising a number one is always a 1-digit number 1.
for number in range(2, 101): #Can't start number range at all exponents raising number one is always a 1-digit number 1.
    #print("first for loop number", number)
    for power in range(1, 101):
        answer = number**power
        length = len(str(answer))
        if length == power:
            print("number", number, "power", power, "answer", answer, "length", length)
            '''
            number 2 power 1 answer 2 length 1
            number 3 power 1 answer 3 length 1
            number 4 power 1 answer 4 length 1
            number 4 power 2 answer 16 length 2
            number 5 power 1 answer 5 length 1
            number 5 power 2 answer 25 length 2
            number 5 power 3 answer 125 length 3
            number 6 power 1 answer 6 length 1
            number 6 power 2 answer 36 length 2
            number 6 power 3 answer 216 length 3
            number 6 power 4 answer 1296 length 4
            number 7 power 1 answer 7 length 1
            number 7 power 2 answer 49 length 2
            number 7 power 3 answer 343 length 3
            number 7 power 4 answer 2401 length 4
            number 7 power 5 answer 16807 length 5
            number 7 power 6 answer 117649 length 6
            number 8 power 1 answer 8 length 1
            number 8 power 2 answer 64 length 2
            number 8 power 3 answer 512 length 3
            number 8 power 4 answer 4096 length 4
            number 8 power 5 answer 32768 length 5
            number 8 power 6 answer 262144 length 6
            number 8 power 7 answer 2097152 length 7
            number 8 power 8 answer 16777216 length 8
            number 8 power 9 answer 134217728 length 9
            number 8 power 10 answer 1073741824 length 10
            number 9 power 1 answer 9 length 1
            number 9 power 2 answer 81 length 2
            number 9 power 3 answer 729 length 3
            number 9 power 4 answer 6561 length 4
            number 9 power 5 answer 59049 length 5
            number 9 power 6 answer 531441 length 6
            number 9 power 7 answer 4782969 length 7
            number 9 power 8 answer 43046721 length 8
            number 9 power 9 answer 387420489 length 9
            number 9 power 10 answer 3486784401 length 10
            number 9 power 11 answer 31381059609 length 11
            number 9 power 12 answer 282429536481 length 12
            number 9 power 13 answer 2541865828329 length 13
            number 9 power 14 answer 22876792454961 length 14
            number 9 power 15 answer 205891132094649 length 15
            number 9 power 16 answer 1853020188851841 length 16
            number 9 power 17 answer 16677181699666569 length 17
            number 9 power 18 answer 150094635296999121 length 18
            number 9 power 19 answer 1350851717672992089 length 19
            number 9 power 20 answer 12157665459056928801 length 20
            number 9 power 21 answer 109418989131512359209 length 21
            '''
            counter += 1
print(counter) #print 49
