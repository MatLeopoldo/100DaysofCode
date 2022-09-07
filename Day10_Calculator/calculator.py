"""
Day 10 - Calculator

This program works as a calculator.
"""
import os
from time import sleep
from art import logo

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

if __name__ == "__main__":

    while True:
        finish_calc = False
        print(logo)
        n1 = float(input("What's the first number? "))        

        for symbol in operations.keys():
            print(symbol)
        
        while not finish_calc:
            operator = input("Pick an operation: ")

            if operator in operations.keys():
                n2 = float(input("What's the next number? "))
                result = operations[operator](n1, n2)
                print(f"{n1} {operator} {n2} = {result}")
            else:
                print("Invalid operation chosen.")
                sleep(1)
                break

            user_option = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        
            if user_option == 'y':
                n1 = result
            else:
                os.system("clear")
                finish_calc = True



            