"""
Day 9 - Blind Auction

This program simulates a simple blind auction.
"""
import os
from art import logo

print(logo, end='\n\n')
print("Welcome to the secret auction program.")

bidding = {}
bidding_finished = False
while not bidding_finished:
    name = input("What is your name?: ").title()
    bid = int(input("What is your bid?: $"))
    bidding[name] = bid

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()

    if should_continue == 'yes':
        os.system('clear')
    else:
        print('Bidding finished.\n')
        bidding_finished = True

highest_bid = 0
bidding_winner = ''
for participant in bidding.keys():
    if bidding[participant] > highest_bid:
        bidding_winner = participant
        highest_bid = bidding[participant]

print(f"The winner is {bidding_winner} with a bid of ${highest_bid}.")





