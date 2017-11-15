#https://projecteuler.net/problem=31 Coin Sums
#https://projecteuler.net/thread=31
#In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation: 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#It is possible to make £2 in the following way: 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#How many different ways can £2 be made using any number of coins?

#Remember add +1 for 200p
count = 0
for p1 in range(0, 201,1):
	for p2 in range(0, 201,2):
		for p5 in range(0,201,5):
			for p10 in range(0,201,10):
				for p20 in range(0,201,20):
					for p50 in range(0,201,50):
						for p100 in range(0,201,100):
							if (p1) + (p2) + (p5) + (p10) + (p20) + (p50) + (p100) == 200:
									count += 1
print(count) #print 73681 (+1 for 200p) for total count 73682

# Too slow
# count = 0
# for p1 in range(0, 201):
# 	for p2 in range(0, 101):
# 		for p5 in range(0,41):
# 			for p10 in range(0,21):
# 				for p20 in range(0,11):
# 					for p50 in range(0,5):	
# 						for p100 in range(0,3):
# 							for p200 in range(0,2):
# 								if (p1*1) + (p2*2) + (p5*5) + (p10*10) + (p20*20) + (p50*50) + (p100*100) + (p200*200) == 200:
# 									count = count + 1
# print(count) #print 73682

# #recursion
# import time
# start = time.time()
# vals = [200, 100, 50, 20, 10, 5, 2, 1]
# def countit(coin,total):
#     while True:
#         if total == 200: # jackpot
#             global counter
#             counter += 1
#             break
#         elif total > 200:
#             break
#         else:
#             if vals[coin] > 1:  # i.e, not the base case
#                 countit(coin + 1, total)
#             total += vals[coin]
# counter = 0
# countit(0,0)
# finish = time.time()
# print(counter)
# print(finish-start)

# #recursion 2
# def variations(coins, goal):
#     if len(coins) == 1: return 1          #you can always get to the goal with ones
#     v = 0                                 #counts the variations
#     while goal > 0:
#         v += variations(coins[1:], goal)  #recursion with coins without the first
#         goal -= coins[0]                  #step towards the goal by adding another of the current coin
#     return v + 1 if goal == 0 else v      #if we reached the goal this is also a valid variation

# solution = variations([200,100,50,20,10,5,2,1], 200)  #coin values count back
# print(solution)