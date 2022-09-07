"""
Day 16 - Coffee Machine (OOP)

This program aims to simulate some features of a coffee machine as can be seen below:

    - Coins processing
    - Transaction checking
    - Resources Management

The difference of this project in comparison with the previous project is that this one was developed using OOP paradigm.
"""
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == "__main__":
    coffee_machine = CoffeeMaker()
    money_machine = MoneyMachine()
    menu_machine = Menu()

    machine_off = False
    while not machine_off:
        user_order = input(f"What do you like? ({menu_machine.get_items()}): ").lower()
        
        if user_order == 'report':
            coffee_machine.report()
            money_machine.report()
        elif user_order == 'off':
            print("The machine will be turned off.")
            machine_off = True
        else:
            drink_ordered = menu_machine.find_drink(user_order)

            if drink_ordered != None:
                if coffee_machine.is_resource_sufficient(drink_ordered):
                    if money_machine.make_payment(drink_ordered.cost):
                        coffee_machine.make_coffee(drink_ordered)

        

