"""
Day 7 - Hangman

This program consists in a Hangman Game.
"""
import hangman_art as art
from random import choice

num_lives = 6

words_list = ['cat', 'dog', 'fish', 'turtle', 'shark', 'monkey', 'elephant', 'giraffe', 
              'mouse', 'bird', 'pig', 'pigeon', 'lion', 'tiger', 'dolphin', 'snake', 
              'bear', 'duck', 'deer', 'scorpion', 'crab', 'whale', 'zebra', 'panda', 
              'eagle', 'squrril', 'spider', 'rabbit', 'rhino', 'camel']

chosen_word = choice(words_list)

display = ['_' for _ in range(len(chosen_word))]

print(art.logo, end='\n\n')

end_game = False
while not end_game:
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = letter
    else:    
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        num_lives -= 1
    
    print(f"{' '.join(display)}")
    print(art.stages[num_lives])

    if '_' not in display:
        end_game = True
        print("You win.")
    elif num_lives == 0:
        end_game = True
        print(f"The word was '{chosen_word}'. You lose.")



