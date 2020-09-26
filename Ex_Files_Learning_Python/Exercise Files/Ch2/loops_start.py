#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  while(x<5):
    print(x)
    x=x+1    

  # define a for loop
  for x in range(5,10):
    print(x)
    #x=x+1   
  # use a for loop over a collection
#  days=["sunday","mon","tue","wed"]
 # for d in days:
  #  print(d)
 
  # use the break and continue statements
  for y in range(5,10):
    #if(y==7):break
    if(y%2==0):continue
    print(y)

  #using the enumerate() function to get index 
  days=["sunday","mon","tue","wed"]
  for i,d in enumerate(days):
    print(i,d)


if __name__ == "__main__":
  main()
