"""
Day 3 - Island Adventure

This program aims to tell a story based on user's choices. If you choose wisely your actions, 
you'll find the treasure. Otherwise, you'll fail.
"""

# Treasure Drawing
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____/__
*******************************************************************************''')

# Introduction
print('Welcome to Treasure Island.')
print('Your mission is to find the treasure.')

# Story
direction = input('You are at a cross road. Where do you want to go? Type "left" or "right"\n').lower()

if direction == 'left':
    action = input('You have come to a lake. There is an island in the middle of the lake. ' + \
                   'Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    
    if action == 'wait':
        door = input('You arrive at the island unharmed. There is a house with 3 doors. ' + \
                     'One red, one yellow and one blue. Which colour do you choose?\n').lower()

        if door == 'yellow':
            print('You found the treasure! You Win!')
        elif door == 'red':
            print('It is a room full of fire. Game Over.')
        elif door == 'blue':
            print('You enter a room of beasts. Game Over.')
        else:
            print('You chose a door that does not exist. Game Over.')
    else:
        print('You get attacked by an angry trout. Game Over.')

else:
    print("You fell into a hole. Game Over.")