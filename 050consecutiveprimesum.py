#https://projecteuler.net/problem=50 Consecutive Prime Sum
#https://projecteuler.net/thread=50
#The prime 41, can be written as the sum of six consecutive primes:  41 = 2 + 3 + 5 + 7 + 11 + 13
#This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.  RM:  953=89+83+79+73+71+67+61+59+53+47+43+41+37+31+29+23+19+17+13+11+7
#Which prime, below one-million, can be written as the sum of the most consecutive primes?
from itertools import combinations
import time
startime = time.clock()
def checkifprime(n): #n must be greater than one
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

#upload prime numbers up to 10,000 in a list from primenumbersupto10000.txt
with open("primenumbersupto10000.txt","r") as fileobject:
    contents = fileobject.read()
    contents = contents.replace("\t",",")
    contents = contents.replace("\n",",")
    primenumberlist = list((map(int,contents.split(","))))

mostconsecutive = 0
mostconsecutivesum = 0
answers = {}
#for loop check each consecutive primes
for start in range(0,len(primenumberlist)-1):
    #if consecutive prime length less than most consecutive prime length, break
    if len(primenumberlist[start::]) < mostconsecutive:
        break
    #if consecutive prime length greater than or equal most consecutive prime length, sum all consecutive prime lengths
    if len(primenumberlist[start::]) >= mostconsecutive:
        partialprimenumberlist = primenumberlist[start::]
        for n in range(1,len(partialprimenumberlist)):
            sumpartialprimenumberlist = sum(partialprimenumberlist[n::-1])
            #if sum consecutive prime length is prime number and less than 1000000, save to answers dictionary consecutive prime length is key and sum consecutive prime length is value
            if checkifprime(sumpartialprimenumberlist) == True and sumpartialprimenumberlist < 1000000:           
                consecutive = len(partialprimenumberlist[n::-1])
                answers[consecutive] = sumpartialprimenumberlist
print(max(zip(answers.keys(), answers.values()))) #answer is (543, 997651)
endtime = time.clock()
print((endtime-startime),"seconds") #print 7.026 seconds
print((round(endtime-startime)),"seconds") #print 7 seconds

#RM:  another way more written code slower response
#for loop check each consecutive primes
# for start in range(0,len(primenumberlist)-1):
#     #if consecutive prime length less than most consecutive prime length, break
#     if len(primenumberlist[start::]) < mostconsecutive:
#         break
#     #if consecutive prime length greater than or equal most consecutive prime length, sum all consecutive prime lengths
#     if len(primenumberlist[start::]) >= mostconsecutive:
#         partialprimenumberlist = primenumberlist[start::]        
#         for n in range(1,len(partialprimenumberlist)):
#             # if len(partialprimenumberlist[n::-1]) < mostconsecutive:
#             #     break
#             sumpartialprimenumberlist = sum(partialprimenumberlist[n::-1])
#             if sumpartialprimenumberlist in primenumberlist and sumpartialprimenumberlist < 1000000:
#                 consecutive = len(partialprimenumberlist[n::-1])
#                 answers[consecutive] = sumpartialprimenumberlist
#             elif checkifprime(sumpartialprimenumberlist) == True and sumpartialprimenumberlist < 1000000:
#                 consecutive = len(partialprimenumberlist[n::-1])
#                 answers[consecutive] = sumpartialprimenumberlist
# print(max(sorted(zip(answers.keys(), answers.values())))) #answer is (543, 997651)
# endtime = time.clock()
# print((endtime-startime),"seconds") #print 17.834168 seconds
# print((round(endtime-startime)),"seconds") #print 18 seconds

#rtng https://projecteuler.net/thread=50;page=7
# def is_prime(a):
#     if a == 1:
#         return False
#     for b in range(2, round(a ** 0.5) + 1):
#         if a % b == 0:
#             return False
#     return True
# def result(n):
#     global final_result, j
#     prime_sum_list = [0, 2]
#     new_prime    = 3
#     prime_length = 0
#     temporary    = 0
#     while prime_sum_list[-1] + new_prime < n:
#         if is_prime(new_prime):
#             prime_sum_list.append(prime_sum_list[-1] + new_prime)
#         new_prime += 2
#     list_length = len(prime_sum_list)
#     for i in range(list_length):
#         for j in range(list_length):
#             if is_prime(prime_sum_list[-i - 1] - prime_sum_list[j]):
#                 temporary = list_length - j
#                 break
#         if temporary > prime_length:
#             prime_length = temporary
#             final_result = prime_sum_list[-i - 1] - prime_sum_list[j]
#         if list_length - i < prime_length:
#             return final_result
# print(result(1000000))