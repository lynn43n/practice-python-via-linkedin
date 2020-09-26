# 
# Example file for variables
#

# Declare a variable and initialize it
l=0
print(l)

# # re-declaring the variable works
l="abc"
print(l)

# # ERROR: variables of different types cannot be combined
print("this is a string"+ str(123))

# Global vs. local variables in functions
def a_func():
    l='hi'
    print(l)

a_func()
print(l)