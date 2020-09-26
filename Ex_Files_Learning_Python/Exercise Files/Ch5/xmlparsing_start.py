# 
# Example file for parsing and processing XML
#
import xml.dom.minidom
import os
from os import path

def main():
  # use the parse() function to load and parse an XML file
  if (path.exists("samplexml.xml")):
    print("hi lynn")
  doc = xml.dom.minidom.parse("samplexml.xml")
  
  # print out the document node and the name of the first child tag
  print(doc.nodeName)
  
  # get a list of XML tags from the document and print each one

    
  # create a new XML tag and add it into the document

  

if __name__ == "__main__":
  main()

