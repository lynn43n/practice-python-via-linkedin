#
# Example file for working with Calendars
#

# import the calendar module
import calendar

# create a plain text calendar
c= calendar.TextCalendar(calendar.SUNDAY)
st= c.formatmonth(2020, 9, 0,0)
print(st)
# create an HTML formatted calendar
hc= calendar.HTMLCalendar(calendar.SUNDAY)
hs=hc.formatmonth(2020, 9)
#print(hs)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month

#for i in c.itermonthdays(2020,9):
 #   print(i)

    
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms

#for i in calendar.month_name:
#   print(i)

#for i in calendar.day_name:
 #   print(i)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:

for m in range(1,13):
    cal= calendar.monthcalendar(2021, m)
    week1= cal[0]
    week2=cal[1] 
    if(week1[calendar.FRIDAY]==0):
        meetday= week2[calendar.FRIDAY]
    else:
        meetday =week1[calendar.FRIDAY]   
    print("the meetday: %d/%d" %(meetday, m) )

    