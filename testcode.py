import sys
import datetime

today = datetime.datetime.today()
print (today.strftime("%Y-%m-%d"))

thismonth = datetime.datetime(today.year, today.month, 1)
print (thismonth.strftime("%Y-%m-%d"))

lastmonth = thismonth + datetime.timedelta(days=-1)
print (lastmonth)

print (lastmonth.strftime("%Y-%m"))
#testtest