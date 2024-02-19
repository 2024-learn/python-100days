# subscripting: the process of pulling elements from a string.

print("Hello"[-1])
print("Hello"[0:-1])
print("Hello"[0:-1])
print("Hello"[0])
print("Hello"[:])
print("Hello"[:-1])

# large numbers:
# with large numbers such as 123,456,789, in python, you can replace the comma with an underscore: 123_456_789

# Integers: whole positive and negative numbers
# Boolean: True or False
# Floats: numbers with decimal points

# Type error, type checking and type conversion
# when you try to concatenate a string and a float or integer, it will result in a type error

# you can chack the type of data with:
print(type("123"))
print(type(123))
print(type(123.4))

# type conversion/ type casting: changing data from one type to another
num_char = len(input("what is your name?"))

print("your name has " + str(num_char) + " characters")

new_num_char = str(num_char)
print("your name has " + new_num_char + " characters")

print(str(70) + str(100.5))

