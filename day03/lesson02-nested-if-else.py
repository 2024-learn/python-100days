# Nested if/else
# if condition:
#   if another condition:
#     do this
#   else: condition:
#   do this
# else:
#   do this

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("you can ride the rollercoaster.")
  age = int(input("what is your age? "))
  if age <= 18:
    print("Please pay $7")
  else:
    print("please pay $12")
else:
  print("sorry, you have to be a bit taller to ride.")


# add a price tier:
# < 12 = $5
# 12-18 = $7
# >18 = $12
  
if height >= 120:
  print("you can ride the rollercoaster.")
  age = int(input("what is your age? "))
  if age < 12:
    print("Please pay $5")
  elif age <= 18:
    print("please pay $ 7")
  else:
    print("please pay $12")
else:
  print("sorry, you have to be a bit taller to ride.")
