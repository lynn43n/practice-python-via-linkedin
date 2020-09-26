#
# Example file for working with classes
#
class myClass():
  def method1(self):
    print("myClass method1")

  def method2(self, string):
    print("myClass method2 "+string)

class anotherClass(myClass):
  def method1(self):
    myClass.method1(self)
    print("anotherClass method1")

  def method2(self, string):
    myClass.method2(self, string)
    print("anotherClasse method2 "+ string) 

def main():
  c= myClass()
  c.method1()
  c.method2("hi hi")
  c2=anotherClass()
  c2.method1()
  c2.method2("hi hi 2")  

if __name__ == "__main__":
  main()
