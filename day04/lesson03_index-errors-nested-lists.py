# Index errors and and Working with Nested Lists
# One of the most common errors in Python is "IndexError: list index out of range"
#  the last item on the list is always one less than the length of the list: len(list) - 1
fruits = ["cherry", "apple", "pear", "banana", "mango", "gooseberry", "guava"]
num_fruits = (len(fruits))
# the list is 7 items long and the last item on the list is at index 6. If you provide an index larger than 6, then you will get an index error
print(fruits[num_fruits - 1]) # will get the last item on the list without being out of range

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# nested lists: lists within a list
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(dirty_dozen[1][1])