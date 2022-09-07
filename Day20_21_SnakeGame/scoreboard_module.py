from turtle import Turtle

BOARD_STYLE = ("Courier", 16, "normal")
ALIGNMENT = "center"
SCORE_POS_X = 0
SCORE_POS_Y = 270

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(SCORE_POS_X, SCORE_POS_Y)
        self.write_score()
    

    def write_score(self):
        self.clear()
        self.write(f"Score:  {self.score}", align=ALIGNMENT,font=BOARD_STYLE)

    
    def update_score(self):
        self.score += 1
        self.write_score()

    
    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=BOARD_STYLE)
