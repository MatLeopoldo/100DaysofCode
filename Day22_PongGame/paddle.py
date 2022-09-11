from turtle import Turtle, Screen

PADDLE_WIDTH = 1
PADDLE_HEIGHT = 5
PADDLE_MOVE_DIST = 20

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__(shape="square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_HEIGHT)
        self.setheading(90)
        self.goto(position)


    def move_up(self):
        self.forward(PADDLE_MOVE_DIST)


    def move_down(self):
        self.backward(PADDLE_MOVE_DIST)


    def configure_movement(self, screen, user_keys):
        screen.onkey(key=user_keys[0], fun=self.move_up)
        screen.onkey(key=user_keys[1], fun=self.move_down)
        screen.listen()
