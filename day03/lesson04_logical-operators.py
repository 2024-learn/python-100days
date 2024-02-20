# if condition1 & condition2 & condition3:
#   do this
# else:
#   do this

# Logical Operators:
# A and B -   both A and B have to be true, otherwise the condition evaluates to false
# C or D -    if either C or D can be true, the condition evaluates to true
# not E  -    if the condition is false, it evaluates to true

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0
if height >= 120:
  print("you can ride the rollercoaster.")
  age = int(input("what is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $ 7")
  elif age >= 45 and age <= 55:
    bill = 0
    print("Seniors ride for free.")
  else:
    bill = 12
    print("Adult tickets are $12")

  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
    print(f"Your final bill is ${bill}")
  
else:
  print("sorry, you have to be a bit taller to ride.")