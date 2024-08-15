#YouTube Project Euler Problem 57： Square Root Convergents [i-sTFAqEcj4]
#It is possible to show that the square root of two can be expressed as an infinite continued fraction.
#YouTuber found the pattern denominator do first.  Add the previous fraction numerator interation and previous fraction denominator interation becomes the denominator for the next iteration.
#YouTuber found the pattern numerator do second.  Add the previous fraction denominator interation and next denominator interation becomes the numerator for the next iteration.  It's confusing.  In other words, sum the current denominator and the previous denominator for the current numerator.
#Any fraction under a numerator of one is the inverse fraction or upside down of the denominator.  For example, 1/(5/2) = 2/5 = 0.4.  1/(10/1) = 1/10 = 0.1.
#Each expansion of x is x=(num+den+den) of x-1/(num+den) of x-1
limit = 1001
numerator = 3
denominator = 2
count = 0
for i in range(2,limit):
    newdenominator = numerator + denominator
    newnumerator = newdenominator + denominator
    numerator = newnumerator
    denominator = newdenominator
    if len(str(numerator)) > len(str(denominator)):
        count+=1
print(count) #print 153

#My solution
xnumeratorprevious = 3
ydenominatorprevious = 2
counter = 0
numeratorgreaterdenominatorcounter = 0
while counter < 1000:
    ydenominatorcurrent = xnumeratorprevious + ydenominatorprevious
    xnumeratorcurrent = ydenominatorprevious + ydenominatorcurrent
    print(xnumeratorcurrent,"/",ydenominatorcurrent)
    '''
    7 / 5
    17 / 12
    41 / 29
    99 / 70
    239 / 169
    577 / 408
    1393 / 985
    3363 / 2378
    ...
    '''
    if len(str(xnumeratorcurrent)) > len(str(ydenominatorcurrent)):
        numeratorgreaterdenominatorcounter += 1
    ydenominatorprevious = ydenominatorcurrent
    xnumeratorprevious = xnumeratorcurrent
    counter+=1
print(numeratorgreaterdenominatorcounter) #print 153


