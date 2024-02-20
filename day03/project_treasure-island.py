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


