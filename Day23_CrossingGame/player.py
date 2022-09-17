from turtle import Turtle, Screen

PLAYER_INITIAL_POS = (0, -280)
AXIS_Y_LIMIT_VAL = 280
PLAYER_MOVE_DIST = 20

class Player(Turtle):

    def __init__(self, screen):
        super().__init__(shape="turtle")
        self.color("green")
        self.penup()
        self.configure_movement(screen)
        self.setheading(90)
        self.goto_initial_pos()


    def goto_initial_pos(self):
        self.goto(PLAYER_INITIAL_POS)

    
    def crossed_the_map(self):
        if self.ycor() >= AXIS_Y_LIMIT_VAL:
            return True
        else:
            return False


    def move_forward(self):
        self.forward(PLAYER_MOVE_DIST)
    

    def configure_movement(self, screen):
        screen.onkey(key="Up", fun=self.move_forward)
        screen.listen()