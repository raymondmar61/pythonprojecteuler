#https://projecteuler.net/problem=22 Names Scores
#https://projecteuler.net/thread=22
#Using 022namesscores.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#What is the total of all the name scores in the file?

letterscore = {"A": 1,"B": 2,"C": 3,"D": 4,"E": 5,"F": 6,"G": 7,"H": 8,"I": 9,"J": 10,"K": 11,"L": 12,"M": 13,"N": 14,"O": 15,"P": 16,"Q": 17,"R": 18,"S": 19,"T": 20,"U": 21,"V": 22,"W": 23,"X": 24,"Y": 25,"Z": 26}
with open("022namesscores.txt") as fileobject:
	contents = fileobject.read()
	nameslist = (contents.split(","))
nameslist = (sorted(nameslist))
supersum = 0
for eachnameslist in nameslist:
	name = eachnameslist.replace('"','')
	print(name)
	lettersum = 0
	namemultiplier = (nameslist.index(eachnameslist))+1
	for eachname in name:
		lettersumnow = letterscore[eachname]
		lettersum = lettersum + lettersumnow
	namescore = lettersum*namemultiplier
	supersum = supersum + namescore
print(supersum) #871198282

# letterscore = {"A": 1,"B": 2,"C": 3,"D": 4,"E": 5,"F": 6,"G": 7,"H": 8,"I": 9,"J": 10,"K": 11,"L": 12,"M": 13,"N": 14,"O": 15,"P": 16,"Q": 17,"R": 18,"S": 19,"T": 20,"U": 21,"V": 22,"W": 23,"X": 24,"Y": 25,"Z": 26}
# with open("022namesscores10.txt") as fileobject:
# 	contents = fileobject.read()
# 	#print(contents)
# 	nameslist2 = (contents.split(","))
# #print(nameslist2)
# #print(sorted(nameslist2))
# nameslist3 = (sorted(nameslist2))
# supersum = 0
# for eachnameslist3 in nameslist3:
# 	#print(eachnameslist3.replace('"',''))
# 	ui = eachnameslist3.replace('"','')
# 	print(ui)
# 	#print(len(ui))
# 	lettersum = 0
# 	namemultiplier = (nameslist3.index(eachnameslist3))+1
# 	for eachui in ui:
# 		#print(eachui)
# 		#print(letterscore[eachui])
# 		#print(nameslist3.index(eachnameslist3))
# 		lettersumnow = letterscore[eachui]
# 		lettersum = lettersum + lettersumnow
# 		#print(lettersum)
# 	print(lettersum)
# 	print(lettersum*namemultiplier)
# 	supersum = supersum + lettersum*namemultiplier
# print(supersum)

# with open("022namesscores10.txt") as fileobject:
# 	#contents = fileobject.readlines()
# 	contents = fileobject.read()
# 	print(contents)
# 	#nameslist2 = contents
# 	#contents.strip('"')
# 	nameslist2 = (contents.split(","))
# # 	for eachcontents in contents:
# # 		nameslist.append(eachcontents)
# # print(nameslist)
# print(nameslist2)
# print(type(nameslist2))
# print(sorted(nameslist2))
# print(nameslist2[0])
# print(len(nameslist2[0]))
# print(nameslist2[0].replace('"',''))
# ui = nameslist2[0].replace('"','')
# print(len(ui))
