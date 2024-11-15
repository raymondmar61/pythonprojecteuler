#65： Convergents of e - Project Euler [iQ1KT8W-Y6U]
#Project Euler Problem 65： Convergents of e [XLcpLjtNtFs]
'''
The square root of 2 can be written as an infinite continued fraction.  The infinite continued fraction can be written, square root of 2 = [1;(2)],(2) indicates that 2 repeats ad infinitum. In a similar way, square root of 23 = [4;(1,3,1,8)].

It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations. Let us consider the convergents for the square root of 2.  Hence the sequence of the first ten convergents for the square root of 2 are 1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, . . . .

What is most surprising is that the important mathematical constant, e = [2;1,2,1,1,4,1,1,6,1,...,1,2k,1,...].  The first ten terms in the sequence of convergents for e are: 2/1, 3/1, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, . . . .  The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17 which is the 1457/536.  Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.

RM:  YouTuber found e for the first 100 is [2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 1, 1, 12, 1, 1, 14, 1, 1, 16, 1, 1, 18, 1, 1, 20, 1, 1, 22, 1, 1, 24, 1, 1, 26, 1, 1, 28, 1, 1, 30, 1, 1, 32, 1, 1, 34, 1, 1, 36, 1, 1, 38, 1, 1, 40, 1, 1, 42, 1, 1, 44, 1, 1, 46, 1, 1, 48, 1, 1, 50, 1, 1, 52, 1, 1, 54, 1, 1, 56, 1, 1, 58, 1, 1, 60, 1, 1, 62, 1, 1, 64, 1, 1, 66, 1, 1]
'''
import decimal
limit = 100
period = [2, 1] #YouTuber discovered 2 is the first number and 1 is the second number.  All numbers thereafter are a pattern.
remremainder = 2

while len(period) < limit:
    period.append(remremainder)
    period.append(1)
    period.append(1)
    remremainder += 2
numnumerator = 1
dendenominator = period[limit - 1]
for i in range(limit - 2, 0, -1):
    print(f"numnumerator / dendenominator = {numnumerator} / {dendenominator}")
    addvalue = period[i] * dendenominator
    temp = numnumerator + addvalue
    numnumerator = dendenominator
    dendenominator = temp

numnumerator = numnumerator + (period[0] * dendenominator)
context = decimal.Context(prec=100)
print(f"period = {period}") #print period = [2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 1, 1, 12, 1, 1, 14, 1, 1, 16, 1, 1, 18, 1, 1, 20, 1, 1, 22, 1, 1, 24, 1, 1, 26, 1, 1, 28, 1, 1, 30, 1, 1, 32, 1, 1, 34, 1, 1, 36, 1, 1, 38, 1, 1, 40, 1, 1, 42, 1, 1, 44, 1, 1, 46, 1, 1, 48, 1, 1, 50, 1, 1, 52, 1, 1, 54, 1, 1, 56, 1, 1, 58, 1, 1, 60, 1, 1, 62, 1, 1, 64, 1, 1, 66, 1, 1]
print(f"{limit}th convergent = {numnumerator} / {dendenominator} = {context.divide(numnumerator, dendenominator)}") #print 100th convergent = 6963524437876961749120273824619538346438023188214475670667 / 2561737478789858711161539537921323010415623148113041714756 = 2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427
print(f"sum of numnumerator = {sum([int(d) for d in [*str(numnumerator)]])}") #print sum of numnumerator = 272
