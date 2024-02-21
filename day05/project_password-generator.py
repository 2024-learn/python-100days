import random

print("Welcome to the PyPassword Generator!")
letters_desired = input("How many letters would you like in your password?\n")
numbers_desired = input("How many numbers would you like in your password?\n")
symbols_desired = input("How many symbols would you like in your password?\n")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '~', '`', '?', '/', '<', '>']

# my solution: 😁

password_letters = random.choices(letters, k=int(letters_desired))
password_symbols = random.choices(symbols, k=int(symbols_desired))
password_numbers = random.choices(numbers, k=int(numbers_desired))

password_combined = password_letters + password_symbols + password_numbers
password_shuffled = random.sample(password_combined, len(password_combined))
password = ''.join(password_shuffled)

print(f"Here is your suggested password: {password}")


#  Alternate solution 1:
# Easy level:

password = ""

for char in range(1, int(letters_desired) + 1):
  password += random.choice(letters)
for char in range(1, int(numbers_desired) + 1):
  password += random.choice(numbers)
for char in range(1, int(symbols_desired) + 1):
  password += random.choice(symbols)

print(password)

#Alternate solution 2:
# Hard Level:
password_list = []

for char in range(1, int(letters_desired) + 1):
  password_list += random.choice(letters)
for char in range(1, int(numbers_desired) + 1):
  password_list += random.choice(numbers)
for char in range(1, int(symbols_desired) + 1):
  password_list += random.choice(symbols)

# print(password_list)
random.shuffle(password_list)
# print(password_list)

password = ""
for char in password_list:
  password += char
print(f"Here is you recommended password: {password}")