number_of_hurdles = 6
while number_of_hurdles > 0:
  jump()
  number_of_hurdles -=1
  print(number_of_hurdles)

# while loop syntax:
# while something_is_true:
#   Do this
#   then do this
#   then do this
  

# Hurdles race 2
# Reeborg has entered a hurdle race, but he does not know in advance how long the race is. 
# Make him run the course, following a path similar to the one shown, but stopping at the only flag 
# that will be shown after the race has started.
# What you need to know
# The functions move() and turn_left().
# The condition at_goal() and its negation.
# How to use a while loop.
# Your program should also be valid for world Hurdles 1.
  
def turn_right():
  turn_left()
  turn_left()
  turn_left()
    
def jump():
  move()
  turn_left()
  move()
  turn_right()
  move()
  turn_right()
  move()
  turn_left()
    
while at_goal() != True:
  jump()

# Alternatively:
while not at_goal():
  jump()


# When to use for loops and when to use while loops
  # use a for loop if you need to iterate over some things and need to do something with each item. 
  # a while loop is better when you do not care where you are in the sequence, the items you are iterating over in a list and you 
  # just want to carry out some sort of functionality until the condition is met
  # NOTE: with for loops the items being iterated over are already set, which is not the case with while loops, 
  # so you have to be careful with while loops, they continue until the condition has been met.
  # if the condition never becomes false, then you are stuck in an infinite loop
  # e.g. 
  # while 5 > 3:  
  #   do something 


# Hurdles 3:
# What you need to know
# The functions move() and turn_left().
# The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
# How to use a while loop and an if statement.
def turn_right():
  turn_left()
  turn_left()
  turn_left()
    
def jump():
  turn_left()
  move()
  turn_right()
  move()
  turn_right()
  move()
  turn_left()
    
while at_goal() != True:
  if wall_in_front():
      jump()
  elif front_is_clear():
      move()


# Hurdle 4: Variable Heights - The position, the height and the number of hurdles changes each time this world is reloaded.
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    
    while wall_on_right():
        move()
        
    turn_right()
    move()
    turn_right()
    
    while front_is_clear():
        move()
        
    turn_left()
    
while at_goal() != True:
    if wall_in_front():
        jump()
    else:
        move()


# Lost in a maze
# Reeborg was exploring a dark maze and the battery in its flashlight ran out.

# Write a program using an if/elif/else statement so Reeborg can find the exit. 
# The secret is to have Reeborg follow along the right edge of the maze, turning right if it can, 
# going straight ahead if it can’t turn right, or turning left as a last resort.

# What you need to know
# The functions move() and turn_left().
# Either the test front_is_clear() or wall_in_front(), right_is_clear() or wall_on_right(), and at_goal().
# How to use a while loop and if/elif/else statements.
# It might be useful to know how to use the negation of a test (not in Python).
def turn_right():
  turn_left()
  turn_left()
  turn_left()

while front_is_clear != True:
   move()
turn_left()

while at_goal() != True:
  if right_is_clear():
    turn_right()
    move()
  elif front_is_clear():
     move()
  else:
     turn_left()