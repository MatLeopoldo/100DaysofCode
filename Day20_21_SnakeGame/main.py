from turtle import Screen
from snake_module import Snake
from food_module import Food
from scoreboard_module import ScoreBoard
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600 
FOOD_MIN_DIST = 15
TAIL_MIN_DIS = 5
WALL_BOUNDARY = 280

def initialize_screen():
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    return screen


def tail_collision_detected(snake):
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < TAIL_MIN_DIS:
                return True
        return False

    
def wall_collision_detected(snake):
    if snake.head.xcor() > WALL_BOUNDARY or snake.head.xcor() < -WALL_BOUNDARY or \
       snake.head.ycor() > WALL_BOUNDARY or snake.head.ycor() < -WALL_BOUNDARY:
       return True
    else:
        return False


def food_was_eaten(snake, food):
    if snake.head.distance(food) < FOOD_MIN_DIST:
        return True
    else:
        return False


if __name__ == "__main__":
    game_screen = initialize_screen()
    score_board = ScoreBoard()
    snake = Snake(game_screen)
    food = Food()
    
    game_finished = False
    while not game_finished:
        game_screen.update()
        snake.move_forward()
        time.sleep(0.05)
        
        # Detect collision with food
        if food_was_eaten(snake, food):
            food.refresh()
            snake.update_size()
            score_board.update_score()

        if wall_collision_detected(snake) or tail_collision_detected(snake):
            game_finished = True
            score_board.game_over()

    game_screen.exitonclick()