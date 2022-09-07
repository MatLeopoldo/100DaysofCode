"""
Day 12 - Number Guessing

This program aims to simulate a number guessing game.
"""
from art import logo
from random import randint
import os

NUM_ATTEMPTS_HARD = 5
NUM_ATTEMPTS_EASY = 10

def set_difficulty():
    if input("Choose a difficulty. Type 'easy' or 'hard': ") == 'hard':
        return NUM_ATTEMPTS_HARD
    else:
        return NUM_ATTEMPTS_EASY


def check_answer(guess, answer, attempts):
    if guess == answer:
        print(f"You got it. The answer was {answer}.")
    elif guess > answer:
        print("Too high.")
        return attempts - 1
    else:
        print("Too low.")
        return attempts - 1


if __name__ == "__main__":

    finish_game = False
    while not finish_game:
        os.system("clear")
        print(logo)
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        number_chosen = randint(1, 100)
        num_attempts = set_difficulty()        

        while num_attempts > 0:
            print(f"You have {num_attempts} attempt(s) remaining to guess the number.")
            user_guess = int(input("Make a guess: "))
            
            num_attempts = check_answer(user_guess, number_chosen, num_attempts)

            if num_attempts == 0:
                print(f"You lose :( The answer was {number_chosen}.")
            elif user_guess != number_chosen:
                print("Guess again.")
            else:
                break                
            
        if input("Do you want to play again? Type 'y' or 'n': ") == 'n':
            finish_game = True

