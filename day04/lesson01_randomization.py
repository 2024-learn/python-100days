# random module
# <https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences>

# module: a section of code that is added in as a whole or is designed for easy reusability.
import random
import my_module

# returns a random integer, between a and b(both inclusive). This also raises a ValueError if a > b
# random_integer = random.randint(a, b)

random_integer = random.randint(1, 10)  
print(random_integer)

print(my_module.pi)

random_float = random.random()
print(random_float)

random_float_int = random_integer + random_float
print(random_float_int)

print(random_float * 5)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")