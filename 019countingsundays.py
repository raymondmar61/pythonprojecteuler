#https://projecteuler.net/problem=19 Counting Sundays
#https://projecteuler.net/thread=19
#You are given the following information, but you may prefer to do some research for yourself.
#1 Jan 1900 was a Monday.
#Thirty days has September, April, June and November.
#All the rest have thirty-one,
#Saving February alone, Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#RM:  I'm counting the number of Sunday *month* 1, *year* or each month begins with a Sunday.  The beginning of the month is a Sunday.

import datetime
import calendar
date1 = datetime.date(1900, 1, 1) #set the date .date(year,month,day)
print(date1)
print('format(%a %b %d %Y): {:%a %b %d %Y}'.format(date1))

count = 0
for eachyear in range(1901,2001):
	for eachmonth in range(1,13):		
		for eachday in range(1,8):
			date1 = datetime.date(eachyear, eachmonth, eachday) #set the date .date(year,month,day)
			#print(date1) #print 2000-10-07
			#print('format(%a %b %d %Y): {:%a %b %d %Y}'.format(date1)) #print format(%a %b %d %Y): Tue Nov 07 2000
			#print('{:%a}'.format(date1),'{:%d}'.format(date1)) #print Wed 02
			if (('{:%a}'.format(date1)) == "Sun") and (('{:%d}'.format(date1)) == "01"):
				count = count + 1
print(count) #answer is 171

#prints number of days per month in a range of years
# for eachyear in range(1990,2001):
# 	for eachmonth in range(1,13):
# 		days = calendar.monthrange(eachyear,eachmonth)[1]
# 		print(eachmonth,eachyear,days) #e.g. 1 1996 31\n 2 1996 29\n 3 1996 31

# for eachyear in range(2000,2002):
# 	for eachmonth in range(1,13):
# 		# d = datetime.date(eachyear,eachmonth)
# 		# print({"%b"}.format(d))
# 		#print(calendar.month_name[eachmonth])
# 		print(calendar.month_name[eachmonth],eachyear,calendar.monthrange(eachyear,eachmonth)[1]) #print December 2001 31
# 		days = calendar.monthrange(eachyear,eachmonth)[1]
# 		print("days",days) #print days 31