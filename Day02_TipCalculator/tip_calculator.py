"""
Day 2 - Tip Calculator

This program aims to calculate the amount that each person has to pay in a lunch 
or dinner with friends (e.g), taking account the value of the bill and the tip.
"""

print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill?\n$"))
num_people = int(input("How many people to split the bill?\n"))
tip_percentage = int(input("What percentage tip would you like to give?\n"))

print(f"Each person should pay ${round(total_bill * (1 + tip_percentage / 100) / num_people, 2)}.")
