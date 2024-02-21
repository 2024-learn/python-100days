# For loop with range:
# Syntax:
# for number in range(a, b): #(b not inclusive)
#   print(number)

for number in range(1,10):  # 10 not included
  print(number)


print("\n")
# The default step is 1 (number to increment with). 
# You can change this behavior by adding a third number in the range to mederate the step behavior
for number in range(0, 100, 3): 
  print(number)
  
# find the sum of all numbers  between 1 and 100:
total = 0
for i in range(1, 101):
  total += i
print(total)