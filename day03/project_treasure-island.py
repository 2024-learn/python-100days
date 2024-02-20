# https://ascii.co.uk/art
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/[TomekK]
# *******************************************************************************

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
choice1 = input('You are at a cross road. Where do you want to go? Left or Right: ').lower()

if choice1 == "left":
  print("You come to a lake. There is an island in the middle of the lake.\n")
  wait_or_swim = input('Type "wait" to wait for a boat. type "swim" to swim across.\n').lower()
  if wait_or_swim == "wait":
    print("You arrive at the island unharmed.\n")
    door = input("There is a house with three doors. One red, one yellow and one blue. Which color do you choose?\n").lower()
    if door == "blue":
      print("You enter a room full of beasts. Game Over!")
    elif door == "yellow":
      print("You Win!")
    elif door == "red":
      print("Sorry, the gators hate red. Game Over!")
    else:
      print("Door doesn\'t exist. Game Over")
  else:
    print("uh-oh! Sharks in the water! Game Over!")
else:
  print("Oh no! You jumped off a cliff ... Game Over!")