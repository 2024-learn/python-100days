# syntax:
fruits = ["cherry", "apple", "pear", "banana"]

# retrieving items from a list by the index:
print(fruits[0])  # first item in the list
print(fruits[-1]) # last item in the list

# change the items on the list:
fruits[0] = "cheery"
print(fruits)

# add a single item to the end of the list
fruits.append("orange")
print(fruits)

# docs.python.org/3/tutorial/datastructures.html

# add multiple items:
fruits.extend(["mango", "gooseberry", "guava"])
print(fruits)


#we can directly convert a string into a list by separating out the commas using str.split(',') eg.
string_input = "Hello,from,the,other,side"
op = string_input.split(',')
print(op)
    #  ['Hello', 'from', 'the', 'other', 'side']

# Python Random Choice() method: returns a random element from a list:
import random
my_list = ["apple", "banana", "cherry"]
print(random.choice(my_list))