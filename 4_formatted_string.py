# In this exercise, we will learn about formatted string
# Formatted String is a way of making a string without the need of
# data type conversion which is easy to visualize.

name = 'Alex Brown'
age = '25'

message = "Hello, My name is " + name + ". I'm " + age + " years old."
print(message)

# formatted string: we can use f"" (double quotes) or f'' (single quotes)
format_str = f"Hello, My name is {name}. I'm {age} years old."
print(format_str)
