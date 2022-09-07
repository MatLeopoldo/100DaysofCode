"""
Day 11 - Blackjack

This program aims to simulate a Blackjack game.
"""
from art import logo
from random import choice
import os

NUM_INITIAL_CARDS = 2
MIN_COMPUTER_SCORE = 17
BLACKJACK_SCORE = 21

deck_of_cards = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'J': 10, 'Q': 10, 'K': 10}

def deal_card():
    return choice(list(deck_of_cards.keys()))


def initialize_hands():
    user_hand = []
    computer_hand = []

    for _ in range(NUM_INITIAL_CARDS):
        user_hand.append(deal_card())
        computer_hand.append(deal_card())
    
    return user_hand, computer_hand


def calculate_score(player_hand):
    score = 0

    for card in player_hand:
        score += deck_of_cards[card]
    
    # Ace card can be 1 or 11
    if score > BLACKJACK_SCORE and 'A' in player_hand:
        score -= player_hand.count('A') * 10
    
    return score


def show_game_situation(user_hand, computer_hand, user_score):
    print(f"Your cards: {user_hand}, current score: {user_score}")
    print(f"Computer's first card: {computer_hand[0]}")


def verify_natural_blackjack(user_hand, computer_hand):
    user_score = calculate_score(user_hand)
    computer_score = calculate_score(computer_hand)

    if len(user_hand) == NUM_INITIAL_CARDS and len(computer_hand) == NUM_INITIAL_CARDS:
        if user_score == BLACKJACK_SCORE and computer_score != BLACKJACK_SCORE:
            print(f"Your hand: {user_hand}")
            print("OMG, you got a Blackjack! You win :)")
            return True
        elif user_score != BLACKJACK_SCORE and computer_score == BLACKJACK_SCORE:
            print(f"Computer's hand: {computer_hand}")
            print("Computer got a Blackjack! You lose :(")
            return True
    
    return False


def complete_computer_hand(current_hand):
    filled_hand = current_hand
    current_score = calculate_score(filled_hand)

    while current_score < MIN_COMPUTER_SCORE:
        filled_hand.append(deal_card())
        current_score = calculate_score(filled_hand)

    return filled_hand, current_score


def get_winner(user_score, computer_score):
    
    if user_score == computer_score:
        return "It's a draw."
    elif user_score == BLACKJACK_SCORE:
        return "OMG, you got a Blackjack! You win :)"
    elif computer_score == BLACKJACK_SCORE:
        return "Computer got a Blackjack! You lose :("
    elif computer_score > BLACKJACK_SCORE:
        return "Computer went over. You win!"
    elif user_score > computer_score:
        return "Congratulations, you win!"
    else:
        return "You lose"


if __name__ == "__main__":
    
    finish_game = False
    while not finish_game:
        os.system('clear')
        print(logo)
        user_hand, computer_hand = initialize_hands()
        finish_round = verify_natural_blackjack(user_hand, computer_hand)

        while not finish_round:
            user_score = calculate_score(user_hand)
            show_game_situation(user_hand, computer_hand, user_score)

            if user_score > BLACKJACK_SCORE:
                print("You went over. You lose :(")
                finish_round = True
            elif user_score == BLACKJACK_SCORE:
                computer_hand, computer_score = complete_computer_hand(computer_hand)
                print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
                print(get_winner(user_score, computer_score))
                finish_round = True
            else:
                if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                    user_hand.append(deal_card())
                else:
                    computer_hand, computer_score = complete_computer_hand(computer_hand)
                    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
                    print(get_winner(user_score, computer_score))
                    finish_round = True

        if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'n':
            finish_game = True

