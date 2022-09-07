from turtle import Screen
from snake_module import Snake
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600 

def initialize_screen():
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    return screen


if __name__ == "__main__":
    game_screen = initialize_screen()
    snake = Snake(game_screen)
    
    while(1):
        snake.move_forward()
        time.sleep(0.1)
        game_screen.update()

    game_screen.exitonclick()