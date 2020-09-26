import html.parser
from html.parser import HTMLParser

# create a subclass of HTMLParser and override the handler methods
class MyHTMLParser(HTMLParser):
  def handle_comment(self, data):
    print("encountered comment: ", data )
    pos=self.getpos()
    print("at line: ", pos[0], " at row: ", pos[1] )

def main():
  # instantiate the parser and feed it some HTML
  parser = MyHTMLParser()
    
  # open the sample HTML file and read it
  f = open("samplehtml.html")
  if f.mode == "r":
    contents = f.read() # read the entire file
    parser.feed(contents)

if __name__ == "__main__":
  main()
  