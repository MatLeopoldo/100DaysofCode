from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 10
SEGMENT_SIZE = 20
RIGHT_DIRECTION = 0
UP_DIRECTION = 90
LEFT_DIRECTION = 180
DOWN_DIRECTION = 270


class Snake():

    def __init__(self, screen):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.configure_movements(screen)
    

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)
            
    
    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment) 

    def update_size(self):
        self.add_segment(self.segments[-1].pos())


    def move_forward(self):
        for index in range(len(self.segments) - 1, 0, -1):
            self.segments[index].goto(self.segments[index - 1].pos())
        self.head.forward(MOVE_DISTANCE)


    def move_up(self):
        if self.head.heading() != DOWN_DIRECTION:
            self.head.setheading(UP_DIRECTION)


    def move_down(self):
        if self.head.heading() != UP_DIRECTION:
            self.head.setheading(DOWN_DIRECTION)


    def move_left(self):
        if self.head.heading() != RIGHT_DIRECTION:
            self.head.setheading(LEFT_DIRECTION)


    def move_right(self):
        if self.head.heading() != LEFT_DIRECTION:
           self.head.setheading(RIGHT_DIRECTION)

    
    def configure_movements(self, screen):
        screen.onkey(key="Up", fun=self.move_up)
        screen.onkey(key='Down', fun=self.move_down)
        screen.onkey(key='Left', fun=self.move_left)
        screen.onkey(key='Right', fun=self.move_right)
        screen.listen()
