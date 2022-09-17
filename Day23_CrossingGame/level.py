from turtle import Turtle

LEVEL_BOARD_POS = (-280, 260)
BOARD_TEXT_FONT = ('Courier', 20, 'normal')
BOARD_TEXT_ALIGN = 'left'

class LevelBoard(Turtle):

    def __init__(self) :
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(LEVEL_BOARD_POS)
        self.write_level()

    
    def write_level(self):
        self.write(f"Level: {self.level}", font=BOARD_TEXT_FONT, align=BOARD_TEXT_ALIGN)

    
    def update_level(self):
        self.level += 1
        self.clear()
        self.write_level()


    def game_over(self):
        self.home()
        self.write(f"GAME OVER", font=BOARD_TEXT_FONT, align="center")