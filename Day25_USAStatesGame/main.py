from turtle import Screen
from states import USAStates

BG_PICTURE_PATH = "Day25_USAStatesGame/blank_states_img.gif" 
SCREEN_WIDTH = 725
SCREEN_HEIGHT = 500
GAME_TITLE = "The USA States Game"

def initialize_screen():
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.title(GAME_TITLE)
    screen.bgpic(BG_PICTURE_PATH)
    return screen


if __name__ == "__main__":
    game_screen = initialize_screen()
    usa_states = USAStates()

    game_is_finished = False
    while not game_is_finished:
        window_title = usa_states.get_current_score() + "States Correct"
        answer = game_screen.textinput(title=window_title, prompt="What's another state name?").title()

        if usa_states.check_answer(answer):
            usa_states.update_game(answer)

        if usa_states.all_states_discovered():
            game_is_finished = True
            usa_states.game_finished()
            
    game_screen.exitonclick()
