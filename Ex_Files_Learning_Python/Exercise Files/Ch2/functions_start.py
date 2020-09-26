#
# Example file for working with functions
#

# define a basic function
def func1():
    print("i am a function")

# function that takes arguments
def func2(arg1, arg2):
    print(arg1," ",arg2)

# function that returns a value
def cube(x):
    return x*x*x

# function with default value for an argument
def pow(number, x=1):
    result= 1
    for i in range(x):
        result=result*number
    return result    
#function with variable number of arguments
def multiadd(*args):
    result=0
    for x in args:
        result = result+x
    return result    

#func1()
#print(func1())
#print(func1)

func2(10, 20)
print(func2(10,20))
print(cube(3))

print(pow(2))
print(pow(2,3))

print(multiadd(1,2,3))