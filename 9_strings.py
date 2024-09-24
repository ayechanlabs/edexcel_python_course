"""
In this exercise, we are going to learn about Python strings.
In order to define a string in python, we can use both single quotes
and double quotes to define a string.

What is a string?
String is a collection of characters.
"""

mesg = 'Python for Beginners'
print(mesg)

mesg2 = "Python for Beginners"
print(mesg)

# playing with python strings
msg = "Python's Course of Begineers"
print(msg)

msg2 = 'Python for "Beginners"'
print(msg2)

"""
But there are times you have to use a specific form.
Normally, we use single/double quote(s) to define a string but what if
we want to write or make a string of multiple lengths.
Like a message that we use it to send in email, then we can use triple
quotes.
"""
long_msg = '''Hi John,
Here is our first long message.
I hope it is working.
'''
print(long_msg)

long_msg2 = """
Hi Alex,
Here is our first email to you.
Thank you,
The support team
"""
print(long_msg2)

# In string, we can not only store data in it but also we can also get
# each character from the string.
# In python, we can use square brackets to get the index of the string
# or character of the string.
course = 'Python for IGCSE'
print(course[0]) # index of the 1st character is zero
print(course[-1]) # index of the last character
print(course[-2]) # index of the second last character
print(course[0:3]) # it will generate a string (sub-string) from a string
print(course[:]) # it has default value of start (zero) and end (length of character) index
print(course[0:]) # it will start from zero up to length of characters
print(course[1:]) # it will start from one up to length of characters
print(course[:5]) # it will start from zero up to index of 5.
