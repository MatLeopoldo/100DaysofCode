from turtle import Turtle
import pandas as pd

STATES_CSV_PATHNAME = "Day25_USAStatesGame/50_states.csv"
GAME_FONT = ("Arial", 8, "normal")
TEXT_ALIGNMENT = "center"


class USAStates(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        
        self.data_csv = pd.read_csv(STATES_CSV_PATHNAME)
        self.states = self.data_csv["state"].to_list()
        self.num_states = len(self.states)


    def get_current_score(self):
        return f"{self.score}/{self.num_states} "

    
    def check_answer(self, answer):
        if answer in self.states:
            return True
        else:
            return False


    def update_score(self):
        self.score += 1


    def write_state(self, answer):
        pos_x = int(self.data_csv[self.data_csv["state"] == answer]['x'])
        pos_y = int(self.data_csv[self.data_csv["state"] == answer]['y'])
        self.goto(pos_x, pos_y)
        self.write(answer, align=TEXT_ALIGNMENT, font=GAME_FONT)

    
    def remove_state_from_list(self, answer):
        self.states.remove(answer)


    def update_game(self, answer):
        self.write_state(answer)
        self.remove_state_from_list(answer)
        self.update_score()

    
    def game_finished(self):
        self.home()
        self.pencolor("blue")
        self.write("Congratulations, you win!", align=TEXT_ALIGNMENT, font=("Arial", 28, "normal"))


    def all_states_discovered(self):
        if self.score == self.num_states:
            return True
        else:
            return False