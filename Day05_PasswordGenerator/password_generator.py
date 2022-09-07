"""
Day 5 - Password Generator

This program consists in a password generator based on the desired 
number of letters, symbols and numbers provided by the user.
"""
from random import choice, shuffle

letters = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+' ]

print("Welcome to the PyPassword Generator!")

num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

password_list = []

for _ in range(num_letters):
    password_list.append(choice(letters))

for _ in range(num_symbols):
    password_list.append(choice(symbols))

for _ in range(num_numbers):
    password_list.append(choice(digits))

shuffle(password_list)

password = ''
for char in password_list:
    password += char

print(f"Your password is: {password}")