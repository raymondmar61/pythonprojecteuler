#https://projecteuler.net/problem=27 Quadratic primes
#https://projecteuler.net/thread=27
#Considering quadratics of the form:
#n^2+an+b, where |a|<1000 and |b|<=1000 where |n| is the modulus/absolute value of n; e.g. |11| = 11and |−4| = 4
#Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
def factornum(num):
	if num > 1:
	   # check for factors
	   for i in range(2,num):
	       if (num % i) == 0:
	           #print(num,"is not a prime number")
	           #print(i,"times",num//i,"is",num)
	           return "no"
	           break
	   else:
	       #print(num,"is a prime number")
	       return "yes"
	# if input number is less than
	# or equal to 1, it is not prime
	else:
	   #print(num,"is not a prime number")
	   return "no"
# for n in range(0,45):
# 	#print(n,":",(n**2)+n+41)
# 	#print(factornum((n**2)+n+41))
# 	if factornum((n**2)+n+41) == "no":
# 		print(n,"stop here first non prime number:",(n**2)+n+41)
# 		break
# for o in range(0,85):
# 	if factornum((o**2)-(79*o)+1601) == "no":
# 		print(o,"stop here first non prime number:",(o**2)-(79*o)+1601)
# 		break
maximumprimecounter = 0
maximuma = 0
maximumb = 0
for a in range(-1000,1000):
	for b in range(-1001,1001):
		n=0
		while True:
			#print(a,b,n,":",(n**2)+(a*n)+b)
			if factornum((n**2)+(a*n)+b) == "no":
				if n >= maximumprimecounter:
					maximuma = a
					maximumb = b
					maximumprimecounter = n
				break
			n+=1
print(maximuma, maximumb, maximumprimecounter)
print(maximuma * maximumb) #answer is -59231

# loga = []
# logb = []
# logn = []
# for a in range(-1001,1001):
# 	for b in range(-1001,1001):
# 		n=0
# 		while True:
# 			#print(a,b,n,":",(n**2)+(a*n)+b)
# 			if factornum((n**2)+(a*n)+b) == "no":
# 				loga.append(a)
# 				logb.append(b)
# 				logn.append(n)
# 				break
# 			n+=1
# # print(loga)
# # print(logb)
# # print(logn)
# print("max",max(logn))
# # print("index",logn.index(max(logn)))
# maxindex = (logn.index(max(logn)))
# print("product a",loga[maxindex]) #-61
# print("product b",logb[maxindex]) #971
# print(loga[maxindex]*logb[maxindex]) #answer is -59231
# # allthree = zip(loga, logb, logn)
# # for x, y, z in allthree:
# # 	if z == max(logn):
# # 		print(x,y,z)