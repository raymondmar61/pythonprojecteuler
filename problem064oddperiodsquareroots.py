#Project Euler Problem 64 Odd Period Square Roots
#Project Euler Problem 64： Odd Period Square Roots [ySnqwNeaBdY]
'''
YouTuber Googled "how to find continued fraction of square root".  Didn't help him.
YouTuber searched on WolframAlpha "what is the continued fraction for square foot of 139"
YouTuber Googled "list of periodic continued fractions for square foot"
'''
#All square roots are periodic when written as continued fractions and can be written in the form:  a0+(1/a1+(1/a2+(1/a3+(1/a4+(1/a5+(1/a6+(1/a7+(1/a8 . . . . The process can be summarized.  It can be seen that the sequence is repeating.  The first ten continued fraction representations of (irrational) square roots are 2, 3, 5, 6, 7, 8, 10, 11, 12, and 13 RM:  the numbers repeat indefinitely.  For example, 2 is 1;(2) one repeat.  5 is 2;(4) one repeat.  7 is 2;(1,1,1,4) four repeats.  11 is 3;(3,6) two repeats.  13 is 3;(1,1,1,1,6) five repeats.
#0, 1, 4, 9 is an odd period when n is between 0 and 13 inclusive.
#How many continued fractions between 0 and 10,000 inclusive have an odd period.
import math
import decimal
context = decimal.Context(prec=300)

limit = 10000
count = 0
#calculate continued fraction period
for n in range(2, limit + 1):
    print("\n")
    print(f"n = {n}") #print n = 7
    period = []
    # rootsquareroot = n**0.5
    rootsquareroot = context.sqrt(decimal.Decimal(n))
    a0 = int(rootsquareroot)
    #print(f"The integer square root of the {n} which is a0 = {a0}") #print The integer square root of the 7 which is a0 = 2
    if a0 == rootsquareroot:
        continue
    # a = 1 / (rootsquareroot - a0)
    a = context.divide(1, context.subtract(rootsquareroot, a0))
    if n == 7:
        print("The reciprical of the rootsquarefoot which is a =", a) #print The reciprical of the rootsquarefoot which is a = 1.54858377035486353016720525121308680857008639436081672678944481973368960774342787592013096215818120353835485944616582103191450996287573826147579685196003590757238357657610796409989653162169575356699268473457460934123864703344731303866719284186543531524701171746560090546912459969134719383996813449144
    #find continued fraction representations
    while True:
        an = int(a) #an variable is a of n.  Integer variable a.
        if n == 7:
            print(f"n = {n} found a = {a} for an = {an}")
            '''
            n = 7 found a = 1.54858377035486353016720525121308680857008639436081672678944481973368960774342787592013096215818120353835485944616582103191450996287573826147579685196003590757238357657610796409989653162169575356699268473457460934123864703344731303866719284186543531524701171746560090546912459969134719383996813449144 for an = 1
            n = 7 found a = 1.82287565553229529525080787681963021285512959154122509018416722960053441161514181388019644323727180530753228916924873154787176494431360739221369527794005386135857536486416194614984479743254363035048902710186191401185797055017096955800078926279815297287051757619840135820368689953702079075995220173716 for an = 1
            n = 7 found a = 1.21525043702153019683387191787975347523675306102748339345611148640035627441009454258679762882484787020502152611283248769858117662954240492814246351862670257423905024324277463076656319828836242023365935140124127600790531370011397970533385950853210198191367838413226757213579126635801386050663480115811 for an = 1
            n = 7 found a = 4.64575131106459059050161575363926042571025918308245018036833445920106882323028362776039288647454361061506457833849746309574352988862721478442739055588010772271715072972832389229968959486508726070097805420372382802371594110034193911600157852559630594574103515239680271640737379907404158151990440347424 for an = 4
            '''
        # print("an:", an)
        period.append(an)
        if an == (2 * a0):
            if n == 7:
                print(f"Break.  n = {n} found a = {a} for an = {an}.  {a0} doubled is {2*a0}.") #print Break.  n = 7 found a = 4.64575131106459059050161575363926042571025918308245018036833445920106882323028362776039288647454361061506457833849746309574352988862721478442739055588010772271715072972832389229968959486508726070097805420372382802371594110034193911600157852559630594574103515239680271640737379907404158151990440347424 for an = 4.  2 doubled is 4.
            break
        # a = 1 / (a - an)
        a = context.divide(1, context.subtract(a, an))
    #if period list variable is odd length, increment count by one
    if len(period) % 2 != 0:
        count += 1
    if n == 7:
        print(f"period for sqrt({n}):  {period}") #print period for sqrt(7):  [1, 1, 1, 4]
print(count) #print 1322
