# RECEIVE number1 FROM (INTEGER) KEYBOARD
number1 = int(input("Enter number 1: "))

# RECEIVE number2 FROM (INTEGER) KEYBOARD
number2 = int(input("Enter number 2: "))

# SET result1 TO number1 / number2
result1 = number1 / number2

# SEND result1 TO DISPLAY
print('Result 1:', result1)

# SET result2 TO number1 MOD number2
result2 = number1 % number2

# SEND result2 TO DISPLAY
print('Result 2:', result2)

# SET result3 TO number1 DIV number2
result3 = number1 // number2

# SEND result3 TO DISPLAY
print('Result 3:', result3)
