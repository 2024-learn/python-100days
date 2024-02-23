# <https://docs.python.org/3/library/functions.html> 


# making custom functions:
# def my_function():
#   do this
#   then do this
#   finally do this
# my_function()

def my_function():
  print("Hello!")
  print("Good Bye!")

my_function() # you have to call/invoke the function

# Reeborg's world:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json
# move reeborg in a square:
def turn_around():
	turn_left()
	turn_left()
    
def turn_right():
	turn_left()
	turn_left()
	turn_left()
    
def robo_move():
	move()
	turn_right()
	
turn_left()
robo_move()
robo_move()
robo_move()
move()
turn_around()

# Hurdle 1
# Hurdles race
# Reeborg has entered a hurdles race. Make him run the course, following the path shown.
# What you need to know
# The functions move() and turn_left().
# Difficulty level

# More advanced
# You may have noticed that your solution has some repeated patterns. 
# If you know how to define functions, define a function named jump() and use it to simplify your program.
def turn_right():
	turn_left()
	turn_left()
	turn_left()
    
def hurdle():
	move()
	turn_left()
	move()
	turn_right()
	move()
	turn_right()
	move()
	turn_left()
    
hurdle()
hurdle()
hurdle()
hurdle()
hurdle()
hurdle()

# or:
for hurdle in range(6):
    hurdle()
