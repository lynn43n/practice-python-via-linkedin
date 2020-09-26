#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print(timedelta(365,5,0,0,4))

# print today's date

now= datetime.now()
print("the time now is: "+ str(now))
# print today's date one year from now

now= datetime.now()
print("the time in one year will be: "+ str(now+timedelta(days=365)))


# create a timedelta that uses more than one argument

now= datetime.now()
print("the time in one year will be: "+ str(now+timedelta(days=365, minutes=5)))


# calculate the date 1 week ago, formatted as a string

now= datetime.now()
print("the time in one year will be: "+ str(now-timedelta(days=7)))



### How many days until April Fools' Day?
today = date.today()
aprilFools= date(year=2020,month=4,day=1)

if( aprilFools<today): 
    print("april fools already pass by %d days ago" % (today-aprilFools).days)
else:
    print("num of day till april fools: ", (aprilFools-today).days )

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year


# Now calculate the amount of time until April Fool's Day  


