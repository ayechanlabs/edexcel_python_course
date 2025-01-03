"""
Ask a user their weight (in pounds), convert it to kilograms and print
on the terminal. 1 lb = 0.45 kg
"""

# METHOD 1
# weight_lbs = input("Enter the weight in pounds: ")
# weight_kg = int(weight_lbs) * 0.45

# print("Total Weight in Kgs: ", weight_kg)

# METHOD 2
weightLbs = float(input("Enter weight in pounds(lbs): ")) # explicit -> 160.0
weightKgs = weightLbs * 0.45 # implicit

print("Weight in Kgs: " + str(weightKgs)) # explicit
