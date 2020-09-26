#
# Example file for working with date information
#
from datetime import date
from datetime import datetime
from datetime import time

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today= datetime.today()
  print("this is a the date today ",today)

  # print out the date's individual components
  print("date components ", today.month, today.day, today.year)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print("the weekday is ", today.weekday())
  days=["mon","tues","wed","thur", "fri", "sat","sun"]
  print("today is :", days[today.weekday()])
  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  today=datetime.now()
  print("today date and time", today)

  # Get the current time
  t=datetime.time(datetime.now())
  print("the time is ", t)

  
if __name__ == "__main__":
  main()
  