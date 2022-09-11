from turtle import Turtle
import random as rd

BALL_MOVE_DIST = 10


INITIAL_ANGLES = [45, 135, -45, -135]

class Ball(Turtle):

    def __init__(self):
        super().__init__(shape='circle')
        self.penup()
        self.color("white")
        self.restart_game()

    
    def restart_game(self):
        self.home()
        self.setheading(rd.choice(INITIAL_ANGLES))


    def move(self):
        self.forward(BALL_MOVE_DIST)


    def bounce_x(self):
        if (self.heading() < 90 and self.heading() > 0) or (self.heading() < 270 and self.heading() > 180):
            self.setheading(self.heading() + 90)
        elif (self.heading() < 180 and self.heading() > 90) or (self.heading() < 360 and self.heading() > 270):
            self.setheading(self.heading() - 90)
        else:
            self.setheading(self.heading() + 180)

    
    def bounce_y(self):
        self.setheading(-self.heading())
        



