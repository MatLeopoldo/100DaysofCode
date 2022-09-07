"""
Day 4 - Rock Paper Scissors

This program aims to simulate a Rock Paper Scissors game.
"""
from random import randint

rock_draw = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_draw = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors_draw = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_draws = [rock_draw, paper_draw, scissors_draw]
signals = ['Rock', 'Paper', 'Scissors']

print("Welcome to the Rock Paper Scissors Game.\n")

user_signal = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(f"You chose {signals[user_signal]}:\n{game_draws[user_signal]}\n")

computer_signal = randint(0, 2)
print(f"Computer chose {signals[computer_signal]}:\n{game_draws[computer_signal]}\n")

if signals[user_signal] == 'Rock':

    if signals[computer_signal] == 'Rock':
        print("It's a draw.\n")
    elif signals[computer_signal] == 'Paper':
        print("You lose\n")
    else:
        print("You win.\n")

elif signals[user_signal] == 'Paper':
    
    if signals[computer_signal] == 'Paper':
        print("It's a draw.\n")
    elif signals[computer_signal] == 'Scissors':
        print("You lose\n")
    else:
        print("You win.\n")

else:

    if signals[computer_signal] == 'Scissors':
        print("It's a draw.\n")
    elif signals[computer_signal] == 'Rock':
        print("You lose\n")
    else:
        print("You win.\n")