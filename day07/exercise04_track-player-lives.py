# https://replit.com/@appbrewery/Day-7-Hangman-5-Start#main.py
import random
import hangman_art
import hangman_words
# from hangman_art import logo, stages (alternative)

# step 4
print(hangman_art.logo)

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_words.word_list)
lives = len(chosen_word)
end_of_game = False

# TODO 1: create a variable called 'lives' to keep track of the number of lives left
display = []
for letter in chosen_word:
  display.append("_")  # or display += "_"
# print(display)

while not end_of_game:
  guess = input("Guess a letter: ").lower()

  # TODO 6 - if the user has entered a letter that they'v already guessed, print the letter and let them know.
  
  # check guessed letter:
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
      if guess in display:
        print(f"You have already guessed {guess}")

  # TODO 2: If guess is not a letter in the chosen_word, then reduce 'lives' by 1, 
  # if lives gets to 0, and display still has "_", the game should stop and it should print "You lose"
  if guess not in chosen_word:
    lives -= 1
    print(f"You guessed {guess}, that's not in the chosen word. You lose a life.")
    if lives == 0:
      end_of_game = True
      print("You lose.")

  # TODO 3: join all the elements in the string and turn it into a string
  print(f"{' '.join(display)}")
  # print(display)

  if "_" not in display:
    end_of_game = True
    print("You win!")

  # TODO 4: Print the ASCII art from 'stages' that corresponds to the current number of 'lives' remaining.
  print(hangman_art.stages[lives])
print(f"The chosen word is {chosen_word}")



