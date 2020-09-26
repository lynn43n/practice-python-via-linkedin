#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
  # make a duplicate of an existing file
  if path.exists("newfile.txt"):
    # get the path to the file in the current directory
    src = path.realpath("newfile.txt")

    
    # let's make a backup copy by appending "bak" to the name
    dst=src+".bak"
    
    # copy over the permissions, modification times, and other info
    #shutil.copy(src,dst) #only copies the content of the file
    #shutil.copystat(src,dst) #copies the metadata of the file

    # rename the original file
#    os.rename(src,  "newfile.txt")
    
    # now put things into a ZIP archive
    rootdir, tail = path.split(src)

    print(rootdir)
    print(tail)
    shutil.make_archive("archive","zip",rootdir)

    # more fine-grained control over ZIP files
    with ZipFile("tezt.zip", "w" ) as newzip:
      newzip.write("newfile.txt")
      newzip.write("lynch.txt.bak")
      
if __name__ == "__main__":
  main()
