#Functions are defined identically to procedures, using the def keyword, a name and parameters.
#The only difference is the use of the return keyword that is used to output the value.
#functions are reusable.
def greet(firstname, lastname):
    return f"Hello {firstname} {lastname}"
print(greet("Steve Rogers"))

#Inputs For Functions - the use of print() and input() should be done outside of the function
def greet(name):
    return f"Hello {name}"

name = input("What is your name? ")
print(greet(name))

#it is done differently for procedure
def greet():
    name = input("What is your name? ")
    print(f"Hello {name}")

greet()

#If we want to allow for flexibility in our function, we could make use of default values that are assigned to parameters when arguments are not specified.