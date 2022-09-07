from turtle import Turtle
import random as rd

POS_X_BOUNDARY = 270
POS_Y_BOUNDARY = 270

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.speed("fastest")
        self.refresh()
        
        
    def refresh(self):
        pos_x = rd.randint(-POS_X_BOUNDARY, POS_X_BOUNDARY)
        pos_y = rd.randint(-POS_Y_BOUNDARY, POS_Y_BOUNDARY)
        self.goto(pos_x, pos_y)