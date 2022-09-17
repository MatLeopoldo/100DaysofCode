from turtle import Turtle
import random as rd
import turtle

NUMBER_OF_CARS = 25
AXIS_X_EDGE = 20
AXIS_Y_EDGE = 50
CAR_MOVE_INCREMENT = 10
MIN_DIST_COLLISION = 20


def random_color():
    turtle.colormode(255)
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    return (r, g, b)


class CarManagement():

    def __init__(self, screen_dimensions):
        self.cars = []
        self.car_speed = CAR_MOVE_INCREMENT
        self.x_value_limit = screen_dimensions[0] / 2 - AXIS_X_EDGE
        self.y_value_limit = screen_dimensions[1] / 2 - AXIS_Y_EDGE

    
    def create_car(self):
        if rd.randint(1, 6) == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random_color())
            new_car.penup()
            
            random_pos_y = rd.randint(-self.y_value_limit, self.y_value_limit)
            new_car.goto(self.x_value_limit, random_pos_y)
            new_car.setheading(180)

            self.cars.append(new_car)


    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

            if car.xcor() < -(self.x_value_limit + AXIS_X_EDGE):
                self.cars.remove(car)
                car.hideturtle()


    def check_collision(self, player):
        for car in self.cars:
            if car.distance(player) < MIN_DIST_COLLISION:
                return True
        return False

    
    def level_up(self):
        self.car_speed += CAR_MOVE_INCREMENT