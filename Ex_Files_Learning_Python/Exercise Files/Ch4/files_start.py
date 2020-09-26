#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  f= open("lynch.txt", "w")

  # Open the file for appending text to the end
  f=open("lynch.txt","a")
  f.write("hola")
  f.close()
  # write some lines of data to the file
 
  #f= open("lynch.txt", "w")
  #f.write("hello Lynn")
  f= open("lynch.txt", "r")
  print(f.read())  


  
  # close the file when done

  f.close()
  # Open the file back up and read the contents

    
if __name__ == "__main__":
  main()
