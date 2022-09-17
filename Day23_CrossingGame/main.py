from turtle import Screen
from player import Player
from level import LevelBoard
from car_management import CarManagement
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_DIMENSIONS = (SCREEN_WIDTH, SCREEN_HEIGHT)

def initialize_screen():
    screen = Screen()
    screen.title("Turtle Crossing Game")
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.tracer(0)
    return screen


if __name__ == "__main__":
    game_screen = initialize_screen()
    turtle_player = Player(game_screen)
    level_board = LevelBoard()
    car_traffic = CarManagement(SCREEN_DIMENSIONS)

    game_is_over = False
    while not game_is_over:

        time.sleep(0.1)
        game_screen.update()
        
        car_traffic.create_car()
        car_traffic.move_cars()

        if car_traffic.check_collision(turtle_player):
            game_is_over = True
            level_board.game_over()
            continue

        if turtle_player.crossed_the_map():
            level_board.update_level()
            car_traffic.level_up()
            turtle_player.goto_initial_pos()
        
    game_screen.exitonclick()