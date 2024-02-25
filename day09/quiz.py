# Question 1:
# Which line of code will change the starting_dictionary to the final_dictionary?

starting_dictionary = {
    "a": 9,
    "b": 8,
}


# final_dictionary = {
#     "a": 9,
#     "b": 8,
#     "c": 7,
# }

# Solution:
starting_dictionary["c"] = 7
final_dictionary = starting_dictionary
print(final_dictionary)

# Question2:
# Which line of code will print "Steak"?

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak", "gravy"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
print(order["main"][2][0])