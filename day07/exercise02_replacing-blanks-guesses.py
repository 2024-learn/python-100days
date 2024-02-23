import random

# step 2
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f"The chosen word is {chosen_word}")


# # TODO-1 - Create an empty list called display.
# - For each letter in the chosen word, add a "-" to display
# - so if the chosen_word is "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess
display = []
for letter in chosen_word:
  display.append("_")  # or display += "_"
print(display)


# TODO-2 - Loop through each position in the chosen_word; if the letter at the positiom matches 'guess',
# then reveal that letter in the display at that position.
# e.g if the user guessed "p" and the chosen word was apple, then the display should be ["_", "p", "p", "_", "_"].
guess = input("Guess a letter: ").lower()

for position in range(len(chosen_word)):
  letter = chosen_word[position]
  if letter == guess:
    display[position] = letter
  

# TODO- 3 -Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_"
    # Hint: Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)

