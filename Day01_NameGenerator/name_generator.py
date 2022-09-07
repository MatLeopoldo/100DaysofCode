"""
Day 1 - Band Name Generator

This program aims to generate a name for your band based on the name 
of your birth city and your first pet.
"""

print("Welcome to the Band Name Generator.")

birth_city = input("What's the name of your birth city?\n")
pet_name = input("What's your first pet's name?\n")

print(f"Your band name could be {birth_city.title()} {pet_name.title()}.")

