# Instructions
# Prime numbers are numbers that can only be cleanly divided by themselves and 1.

# https://en.wikipedia.org/wiki/Prime_number

# You need to write a function that checks whether if the number passed into it is a prime number or not.

# e.g. 2 is a prime number because it's only divisible by 1 and 2.

# But 4 is not a prime number because you can divide it by 1, 2 or 4.
# Example Input 1
# 73
# Example Output 1
# It's a prime number.
# Example Input 2
# 75
# Example Output 2
# It's not a prime number.

# Write your code below this line 👇

def prime_checker(number):
  prime = True
  for i in range(2,number):
    if number % i == 0:
      prime = False
  if prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Pleae print a number between 1 and 100 to check if it is prime:\n")) # Check this number
prime_checker(number=n)