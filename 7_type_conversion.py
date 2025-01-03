"""
Sometimes the data type of a variable gets changed during program
execution. This is known as 'type coercion' or 'type conversion'.

In programming, there are 2 types of type conversion-
- implicit casting: which changes the data types automatically.
- explicit casting: the data type has to changed manually.
"""

# IMPLICIT CASTING
a = 5 # int
b = 4.6 # float

print(type(a))
print(type(b))

# in here, we add 2 different data type
# a which holds a integer value
# b which holds a float value
# but the result is in float
c = a + b # float = int + float: we called this as implicit casting: memory[float] > [int]
print(c) # 9.6
print(type(c))

# EXPLICIT CASTING
firstNum = input("Enter 1st Number: ")
secondNum = input("Enter 2nd Number: ")

# before type conversion
print("Original Data Type")
print(type(firstNum))
print(type(secondNum))

# after type conversion
firstNum = int(firstNum) # explicit
secondNum = int(secondNum) # explicit
print("After Data Conversion")
print(type(firstNum))
print(type(secondNum))

total = firstNum + secondNum # total = int(firstNum) + int(secondNum)
# print('Total', total)
print("Total: " + str(total))

"""
When we use input(), we will be asking the user to input the data.
but we will receive the input as as a string data type even if the input
data are numbers.

In other word, the input() method takes the input as a string.
So when we write 2024 in terminal, input() method takes it as '2024'
like a string.
When we are doing calculation with string and integer, (in most of
programming) doesn't know it how to do it.
In order to make calculation, we will convert string to integer data
type.
That's what we call it as type conversion, means we will be converting
our original datatype to another data type.

In python, there are 4 types of type conversion -
- str(): converting to string
- int(): converting to integer
- float(): converting to float
- bool(): converting to boolean
"""
