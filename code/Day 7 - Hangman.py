# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Step 5

import random
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
import hangman_words
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
import hangman_art
print(hangman_art.logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

already_guess = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in already_guess:
      print(f"You have already guess {guess}, try another word")
      continue
    else:
      already_guess.append(guess)

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print(f"The word {guess} is not in the chosen_word, your lives has reduced to {lives}.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    import hangman_art
    print(hangman_art.stages[lives])