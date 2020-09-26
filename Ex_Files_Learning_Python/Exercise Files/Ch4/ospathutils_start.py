#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
  # Print the name of the OS
  print(os.name)

  # Check for item existence and type
  print ("item exist:", str(os.path.exists("lynch.txt")))
  
  # Work with file paths
  print("file path is: ", str(os.path.realpath("lynch.txt")))
  print("file path is: ", str(os.path.split(path.realpath("lynch.txt"))))

  # Get the modification time
  t= time.ctime(path.getmtime("lynch.txt"))
  print("last mod of file: ",t)
  
  # Calculate how long ago the item was modified
  timenow= datetime.datetime.now()
  timemod=datetime.datetime.fromtimestamp(path.getmtime("lynch.txt"))
  print("time since last mod: ", str((timenow-timemod)))

  
if __name__ == "__main__":
  main()
