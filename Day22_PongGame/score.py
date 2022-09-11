from turtle import Turtle

DASH_LENGTH = 20
DASH_WIDTH = 10
SCORE_OFFSET_X = 100
SCORE_OFFSET_Y = 100
FONT_STYLE = ('Courier', 48, 'bold')
ALIGNMENT = 'center'


class ScoreBoard(Turtle):

    def __init__(self, screen_height):
        super().__init__()
        self.left_player_score = 0
        self.right_player_score = 0
        self.screen_height = screen_height
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.draw_center_line()
        self.print_score()


    def draw_center_line(self):
        self.penup()
        self.goto(0, -self.screen_height / 2)
        self.setheading(90)
        self.pensize(width=DASH_WIDTH)
        
        for _ in range(0, self.screen_height, DASH_LENGTH):
            if self.isdown():
                self.penup()
            else:
                self.pendown()
            
            self.forward(DASH_LENGTH)
        
    
    def print_score(self):
        pos_y = self.screen_height / 2 - SCORE_OFFSET_Y
        pos_x = SCORE_OFFSET_X
        self.penup()
        
        self.goto(-pos_x, pos_y)
        self.write(self.left_player_score, font=FONT_STYLE, align=ALIGNMENT)
        self.goto(pos_x, pos_y)
        self.write(self.right_player_score, font=FONT_STYLE, align=ALIGNMENT)

    
    def update_score(self):
        self.clear()
        self.draw_center_line()
        self.print_score()



