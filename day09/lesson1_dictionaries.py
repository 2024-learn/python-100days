# Dictionaries:
# Dictionaries allow us to group and tag different pieces of related information

# syntax:
dictionary = {
  "key": "value",
  "key": "value",
  "key": "value",
  "key": "value",
}

# Extracting items from a  list:
# provide the key. NOTE: spell the key correctly when trying to retrieve the item from the dictionary. 
  # If it does not match with a key in the dictionary, it will return a KeyError
# Make sure to use the quotation marks unless it is an already defined variable or a data type that is not a string like numbers, 
  # otherwise, the program will not run
bug = ""
favorite_animals = {
  "dogs": "Alaskan Malamute",
  "spiders": "Absolutely none, thank you very much...Australia!",
  "snakes": "Seriously, Australia?!",
  bug : "This variable is already defined outside the dictionary and therefore does not need quotes",
  123: "This is a number"
}
favorite_animals["dogs"]
print(favorite_animals[bug])
print(favorite_animals[123])

# Adding new items to dictionary
favorite_animals["big mammals"] = "Elephants"
print(favorite_animals)

# create an empty dictionary: 
# NOTE: You can also wipe the contents of a dictionary with the same:
empty_dictionary = {}

# Edit an item in a dictionary:
favorite_animals[bug] = "No, but can we talk about it? Why is everything in Australia trying to kill you?"
print(favorite_animals)

# Loop through a dictionary
# *** If you loop through a dictionary like you do in a list, it will return only the keys 
# and if you have a variable (defined outside the dictionary), like 'bug' in our case is a part of the keys, it returns an empty string
for animal in favorite_animals:
  print(animal)
    # dogs
    # spiders
    # snakes

    # 123
    # big mammals

# to get the value from a dictionary:
for animal in favorite_animals:
  print(favorite_animals[animal])
