# create a program that will calculate how much everyone needs to pay plus tip
print("Welcome to the tip calculator.\nWhat was the total bill?")
bill = float(input())
print("What percentage tip wpuld you like to give? 10, 12, or 15?")
tip = float(input())/100
print("How many people will be splitting the bill?")
people = int(input())
bill_per_person = (bill + (bill * tip))/people
print(f"Each person should pay: ${round(bill_per_person,2)}")

# Alternatively, you can format it to round to 2 places, where it displays the last zero
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")