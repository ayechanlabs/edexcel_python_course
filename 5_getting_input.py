# So, far we have learnt about to give a value to a variable but in
# real program, we ask the input from user.
# So, in this exercise we will learn about getting inputs from user.

"""
Both input() and print() are the functions that is built-in inside
a python.
In python, we've a bunch of function for common tasks such as
printing messages, receiving input and so on.

In order to get input from user, we'll use 'input()' function to get
input from user.
We can also check the data type of a variable based on the value inside
a variable.
"""

name = input("What is your name? ")
print('Hello ' + name)
print(type(name)) # string
