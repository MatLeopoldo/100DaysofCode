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
        
        data_csv = pd.read_csv(STATES_CSV_PATHNAME)
        self.states = {row.state: {'x': row.x, 'y': row.y} for (_, row) in data_csv.iterrows()}
        self.num_states = len(self.states)


    def get_current_score(self):
        return f"{self.score}/{self.num_states} "

    
    def check_answer(self, answer):
        if answer in self.states.keys():
            return True
        else:
            return False


    def update_score(self):
        self.score += 1


    def write_state(self, answer):
        self.goto(self.states[answer]['x'], self.states[answer]['y'])
        self.write(answer, align=TEXT_ALIGNMENT, font=GAME_FONT)

    
    def remove_state_from_list(self, answer):
        self.states.pop(answer)


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