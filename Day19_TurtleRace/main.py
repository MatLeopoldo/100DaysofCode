
from turtle import Turtle, Screen
import random as rd

NUM_TURTLES = 6
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400

def initialize_turtles():
    turtles = []
    colors = ["blue", "yellow", "green", "black", "red", "orange"]

    for index in range(NUM_TURTLES):
        turtles.append(Turtle(shape="turtle"))
        turtles[index].color(colors[index])
        turtles[index].penup()
        turtles[index].setpos(10 - int(SCREEN_WIDTH / 2), index * 40 - int(SCREEN_HEIGHT / 4))
    
    return turtles


def initialize_screen():
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    return screen


def move_turtles(turtles_racers):
    
    for turtle in turtles_racers:
        turtle.forward(rd.randint(1, 10))


def is_there_winner(turtle_racers, user_turtle):

    for turtle in turtle_racers:
        pos_x, _ = turtle.pos()
        if pos_x >= SCREEN_WIDTH / 2:
            if turtle.pencolor() == user_turtle:
                print("Congratulations! Your turtle wins!")
            else:
                print(f"You lose :( {turtle.pencolor().title()} turtle wins.")
            return True
    
    return False


if __name__ == "__main__":
    screen = initialize_screen()
    turtles = initialize_turtles()
    user_turtle = screen.textinput(title="Turtle Race Game", prompt="Please, choose one turtle by the color: ").lower()

    while not is_there_winner(turtles, user_turtle):
        move_turtles(turtles)

    screen.exitonclick()
