from operator import truediv
from turtle import Screen
from time import sleep
import paddle
import score
import ball

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
NUM_PLAYERS = 2
BALL_AXIS_Y_LIMT = (SCREEN_HEIGHT / 2) - 20 
BALL_AXIS_X_LIMIT = (SCREEN_WIDTH / 2) - 70
BALL_PADDLE_MIN_DIST = 50
PLAYERS_POS = [(50 - (SCREEN_WIDTH / 2), 0), ((SCREEN_WIDTH / 2) - 50, 0)]
PLAYERS_KEYS = [["w", "s"], ["Up", "Down"]]

def initialize_screen():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.title("Pong Game")
    screen.tracer(0)
    return screen


def initialize_players(game_screen):
    players = [] 
    for index in range(NUM_PLAYERS):
        new_player = paddle.Paddle(PLAYERS_POS[index])
        new_player.configure_movement(screen=game_screen, user_keys=PLAYERS_KEYS[index])
        players.append(new_player)

    return players


def check_wall_collision(ball):
    if ball.ycor() >= BALL_AXIS_Y_LIMT or ball.ycor() <= -BALL_AXIS_Y_LIMT:
        return True
    else:
        return False


def check_paddles_collision(ball, paddles):
    if (ball.xcor() > BALL_AXIS_X_LIMIT and ball.distance(paddles[1]) < BALL_PADDLE_MIN_DIST) or \
       (ball.xcor() < -BALL_AXIS_X_LIMIT and ball.distance(paddles[0]) < BALL_PADDLE_MIN_DIST):
        return True
    else:
        return False


def check_goal(ball, score_board):
    if ball.xcor() < PLAYERS_POS[0][0]:
        score_board.right_player_goal()
        return True
    elif ball.xcor() > PLAYERS_POS[1][0]:
        score_board.left_player_goal()
        return True
    else:
        return False
        

if __name__ == "__main__":
    game_screen = initialize_screen()
    players = initialize_players(game_screen)
    score_board = score.ScoreBoard(SCREEN_HEIGHT)
    pong_ball = ball.Ball()

    game_is_over = False
    while not game_is_over:
        sleep(0.05)
        game_screen.update()
        pong_ball.move()

        if check_wall_collision(pong_ball):
            pong_ball.bounce_y()

        if check_paddles_collision(pong_ball, players):
            pong_ball.bounce_x()

        if check_goal(pong_ball, score_board):
            score_board.update_score()
            pong_ball.restart_game()
        
    game_screen.exitonclick()