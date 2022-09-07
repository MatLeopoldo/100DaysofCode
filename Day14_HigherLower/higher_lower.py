"""
Day 14 - NHigher Lower 

This program aims to simulate a Higher Lower game comparing 
the number of followers on Instagram.
"""
from art import logo, versus_symbol
from database import data_list
from random import choice
import os

def print_top_screen():
    os.system("clear")
    print(logo)


def print_options(option_A, option_B):
    print(f"Option A: {option_A['owner']}, {option_A['description']} from {option_A['nationality']}.")
    print(versus_symbol)
    print(f"Option B: {option_B['owner']}, {option_B['description']} from {option_B['nationality']}.")


def get_random_instagram():
    return choice(data_list)


def check_answer(option_A, option_B, user_answer):
    
    if user_answer == 'A':
        if option_A["followers"] >= option_B["followers"]:
            return True
        else:
            return False
    elif user_answer == 'B':
        if option_B["followers"] >= option_A["followers"]:
            return True
        else:
            return False
    else:
        print("An invalid option was chosen.")
        return False


if __name__ == "__main__":

    end_game = False
    while not end_game:
        score = 0
        end_round = False
        print_top_screen()

        participant_A = get_random_instagram()
        participant_B = get_random_instagram()

        while not end_round:
            print_options(participant_A, participant_B)

            answer = input("Who has more followers? Type 'A' or 'B': ").upper()
            got_it_right = check_answer(participant_A, participant_B, answer)
            print_top_screen()

            if got_it_right:
                score += 1
                print(f"You're right! Your current score: {score}.")
                participant_A = participant_B
                participant_B = get_random_instagram()
            else:
                print(f"Sorry, that's wrong. Your final score: {score}.")
                end_round = True

        if input("Do you want to play again? Type 'y' or 'n': ").lower() == 'n':
            end_game = True
