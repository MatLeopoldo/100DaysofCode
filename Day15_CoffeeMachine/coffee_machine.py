"""
Day 15 - Coffee Machine

This program aims to simulate some features of a coffee machine as can be seen below:

    - Coins processing
    - Transaction checking
    - Resources Management
"""
import coffee_machine_data as cm


def get_machine_initial_resources():
    return {'coffee': 100, 'milk': 200, 'water': 300, 'cash': 0}


def print_report(machine_resources):
    print(f"Water: {machine_resources['water']} ml")
    print(f"Milk: {machine_resources['milk']} ml")
    print(f"Coffee: {machine_resources['coffee']} g")
    print(f"Money: ${machine_resources['cash']}", end='\n\n')


def check_resources(order, machine_resources):

    for resource in machine_resources.keys():
        if resource != 'cash':
            if machine_resources[resource] < cm.coffee_recipes[order][resource]:
                print(f"Sorry, there's not enough {resource}.", end='\n\n')
                return False

    return True


def process_money():
    print("Please, insert coins.")
    total_inserted = 0

    for coin in cm.coins_values.keys():
        num_coin = int(input(f"How many {coin}? "))
        total_inserted += num_coin * cm.coins_values[coin]
    
    return total_inserted


def make_coffee(order, cash, machine_resources):

    for resource in machine_resources.keys():
        if resource == 'cash':
            machine_resources[resource] += cm.coffee_prices[order]
        else:
            machine_resources[resource] -= cm.coffee_recipes[order][resource]

    print(f'Here is ${round(cash - cm.coffee_prices[order], 2)} in charge.')
    print(f'Here is your {order}. Enjoy!', end='\n\n')

    return machine_resources

    
def process_order(order, machine_resources):
    if check_resources(order, machine_resources):
        money_inserted = process_money()

        if money_inserted > cm.coffee_prices[order]:
            machine_resources = make_coffee(order, money_inserted, machine_resources)
        else:
            print("Sorry, that's not enough money. Money refunded!", end='\n\n')
        
    return machine_resources


def coffee_machine():
    machine_resources = get_machine_initial_resources()
    coffee_machine_ON = True
    
    while coffee_machine_ON:
        user_order = input("What do you like? (espresso/latte/cappuccino): ").lower()
    
        if user_order == "report":
            print_report(machine_resources)
        elif user_order == "off":
            print("The machine will be turned off.")
            coffee_machine_ON = False
        elif user_order == 'espresso' or user_order == 'latte' or user_order == 'cappuccino':
            process_order(user_order, machine_resources)
        else:
            print("Unknown command. Please, try again.")


if __name__ == "__main__":
    coffee_machine()
    
        
