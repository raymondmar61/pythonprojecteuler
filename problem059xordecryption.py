#okay to delete yes
#YouTube Project Euler Problem 59： XOR Decryption [164NQ_ruxew]
#The encryption key consists of three lower case characters. Using 0059_cipher.txt, a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
print(chr(42)) #print *
print(ord("A")) #print 65
print(chr(65)) #print A

import csv
from string import ascii_lowercase
from itertools import combinations

#Import text file as a list
cipherlist = []
for cipherfile in csv.reader(open("0059_cipher.txt", newline=""), delimiter=","):
    for eachcipherfile in cipherfile:
        cipherlist.append(int(eachcipherfile))
#print(cipherlist) #print [36, 22, 80, 0, 0, 4, 23, 25, 19, 17, 88, 4, 4, 19, 21, 11, 88, 22, 23, 23, 29, 69, 12, 24, 0, 88, 25, 11, 12, 2, 10, 28, 5, 6, 12, 25, 10, 22, 80, 10, . . . ]

#Prepare alphabet using ascii_lower from string module
print(ascii_lowercase) #print abcdefghijklmnopqrstuvwxyz
# print(type(ascii_lowercase)) #print <class 'str'>
# print(*ascii_lowercase) #print a b c d e f g h i j k l m n o p q r s t u v w x y z
# print(*list(ascii_lowercase)) #print a b c d e f g h i j k l m n o p q r s t u v w x y z
# print([*"abcdefghijklmnopqrstuvwxyz"]) #print ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# print([*ascii_lowercase]) #print ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(list(ascii_lowercase)) #print ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet = list(ascii_lowercase)
possiblekeys = list(combinations(alphabet * 3, 3)) #keys to decrypt message
# print(possiblekeys) #print [. . . ('w', 'x', 'y'), ('w', 'x', 'z'), ('w', 'y', 'z'), ('x', 'y', 'z')]

#Each ASCII code number perform XOR function to decrypt text file
for eachpossiblekeys in possiblekeys:
    #print(eachpossiblekeys) #print ('e', 'x', 'p')
    keycodedecrypt = [ord(asciicodenumber) for asciicodenumber in eachpossiblekeys]
    #print(keycodedecrypt) #print [101, 120, 112]
    keyindex = 0
    decryptedcipherfile = []
    for i in range(len(cipherlist)):
        #print("keycodedecrypt", keycodedecrypt[keyindex]) #print keycodedecrypt 112
        #print("cipherlist", cipherlist[i]) #print cipherlist 94
        xor = keycodedecrypt[keyindex] ^ cipherlist[i]
        #print("xor", xor) #print 46.  Prints an ascii number represeting a character string.
        decryptedcipherfile.append(xor)
        keyindex += 1
        if keyindex >= len(keycodedecrypt):
            keyindex = 0
    #Convert decrypted message in integers back to characters or a string
    decryptedmessage = ''.join([chr(asciicharacter) for asciicharacter in decryptedcipherfile])
    #print(decryptedmessage) #print \o*xy~o`ii!~|jos!long=ubx!csuxre~ucro*rg*roo=nl=Dqdx:r*pnyi!ixmoskidn=qkmdxn-*?Eo=rplcn!yxscxsp!xxbcmse~`xhl(=ZEs!~ud*ntgn!e{!yxscxr*rg*oditqxrbkqrW'!C=ikkd*odixo~qx*{nse&=ptuo=tdxyzxb~xefd-*|o*xmoz`di!oeqxxrytnd=geo!~ud*xo~tso=rp!e{!~uhy=roohon!;=**,.>=**,.3=**,.;+!!=d~~/&=vbtbb=eomddyr*ro*iio=p|ex|uod*rg*iio=bcobfx-*nn*iiki!c{!~ud*isx!yhl*rg*iicn!yxscxr*tr*rc~|hdxe&=gxrl*tu*|u*roix!~ud*ltkyskitxx!e{!~ud*~hx~mo=geqmejr$=Okpdfd-*T!b|wo=gehon=ub|u*iio=rp!e{!~uhy=roohon!cn!k=rceub=qkou*rg*iio=r{h`xx!e{!~ud*mdxtloidx=nl=ubx!itsiqd*jiend*yhkpd~xs*tr*,:*rs*x*mt~ihdz!~ud*ntg=nl=ubtr*ndxtdy=d{h`f=ue=r&=h~=ikn!~ud*o`~tn*npxi)<4!ghm~tqftdn=cs=r*in*,!e{!~ud*mdxtloidx=ue=ubx!nt`gxuoo/*T!}tmf=rero*niej!~u`~=ubx!yhl*rg*iicn!yxscxr*in*d*|qzonrtlkidfd!;37>)89)1<+9>/3<)2<):*|on=gxrl*ptfihzqxcsf*iicn!dhlhxs*x*nhr1!kse*iios!~|jcsf*iio=r{h`xx!xrn~1!~ud*stgdx=2$,5;(88+49(93*89/22=hy=hdydoy!zonnhboy-*jic~i*xyzodyndy=ubx!zxscpd~xs*rg*|!itsiqd*jiend*yhkpd~xs*tr*,/*[nfqn}tom=`m|hd=ubx!y|lo=r~xqy=cs=vbtbb=H*u`n=`xoh|xe*|u*iicn!yhl&=H*u`|x!ntrirwoodn=ub|u*iio=rp!e{!~ud*ndxtdy=0*6!;20<=**,.2,!!=0%/4<=**,.</4*6!oib$=`fnn*ydzxonn!es!~ud*ltkyskitxx!e{!~ud*~hx~mo3!D|loqx&=ubx!yhl*rg*iicn!ghm~tqftdn=cs=8:=fckdy=ubx!htp|ex|uo=)lrtxii*mn}xs#=nl=ubx!itsihllxsosbo=nl=ubx!zxscpd~xs*rg*|!itsiqd*jiend*yhkpd~xs*tr*,/*\on=cs=rcphf|s*odknndtom=H*u`|x!ftjojhyx!hxdd=`hqd*in*yd~xsgtoo=ubx!yhly=nl=ubx!yhcyxpxo~=roohon!cs!}uhiu!~ud*xyzroosuy=`xx!okdd=opcoor$
    #Stop the decryption when the most common words in the English language are found.  Searched Wikipedia for the most common words in English.
    if ("the" in decryptedmessage and "and" in decryptedmessage and "be" in decryptedmessage and "to" in decryptedmessage and "of" in decryptedmessage and "that" in decryptedmessage):
        print(f"Used eachpossiblekey {eachpossiblekeys} as the key.") #print Used eachpossiblekey ('e', 'x', 'p') as the key
        print(decryptedmessage) #print An extract taken from the introduction of one of Euler's most celebrated papers, "De summis serierum reciprocarum" [On the sums of series of reciprocals]: I have recently found, quite unexpectedly, an elegant expression for the entire sum of this series 1 + 1/4 + 1/9 + 1/16 + etc., which depends on the quadrature of the circle, so that if the true sum of this series is obtained, from it at once the quadrature of the circle follows. Namely, I have found that the sum of this series is a sixth part of the square of the perimeter of the circle whose diameter is 1; or by putting the sum of this series equal to s, it has the ratio sqrt(6) multiplied by s to 1 of the perimeter to the diameter. I will soon show that the sum of this series to be approximately 1.644934066842264364; and from multiplying this number by six, and then taking the square root, the number 3.141592653589793238 is indeed produced, which expresses the perimeter of a circle whose diameter is 1. Following again the same steps by which I had arrived at this sum, I have discovered that the sum of the series 1 + 1/16 + 1/81 + 1/256 + 1/625 + etc. also depends on the quadrature of the circle. Namely, the sum of this multiplied by 90 gives the biquadrate (fourth power) of the circumference of the perimeter of a circle whose diameter is 1. And by similar reasoning I have likewise been able to determine the sums of the subsequent series in which the exponents are even numbers.
        break
print(sum(decryptedcipherfile)) #print 129448
print(112 ^ 94)
