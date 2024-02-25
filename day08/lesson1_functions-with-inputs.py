# syntax:

# something = 123 
# parameter :  argument

# def my_function(something):
  # Do this with something
  # then do this
  # finally do this
# my_function()

def greet():
  print("Hello there!")
  print("Please come again")
  print("So long!\n")
greet()

def greet_with_name(name):
  print(f"Hello, {name}!")
  print(f"Good bye, {name}!\n")

greet_with_name("phyllis")

# Functions with more than one input - positional arguments
# positional arguments are not mapped to a parameter so you need to pay attention to the order you type them in. 
# In case they get switched around, they will change the meaning of the whole function
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is the weather like in {location}?\n")

greet_with("Phyllis", "Austin") 


# Functions with more than one input - Keyword arguments
# with keyword arguments, they are mapped to a parameter, so in case the oder gets switched around, the function will still make sense
# def my_function(a, b , c):
  # Do this with a
  # then do this with b
  # finally do this with c
# my_function(a=1, b=2, c=3)

def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is the weather like in {location}?\n")

greet_with(location="Austin", name="Phyllis") 