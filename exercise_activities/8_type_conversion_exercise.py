# METHOD 1
# birthYear = input('Enter Birth Year: ')
# print(type(birthYear)) # string

# age = 2024 - int(birthYear) # convert string to integer
# print('Your age is', age)

# METHOD 2 
# import datetime
#
# current = datetime.datetime.now() # current date (year, month, day, time[hr:min:sec:msec])
# print(current)

from datetime import datetime

current = datetime.now()

currYear = current.year # 2024
birthYear = int(input("Enter your Birth Year: "))

age = currYear - birthYear
print('Age:', age)

