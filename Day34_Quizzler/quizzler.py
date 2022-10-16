import tkinter as ttk
from tkinter import messagebox
import html
import requests
import time

APP_TITLE = "Quizzler"
BLUE_COLOR = "#4C6793"
WHITE_COLOR = "#F9F9F9"
GREEN_COLOR = "#38E54D"
RED_COLOR = "#DD5353"

WINDOW_PAD = 20
WIDGETS_PADY = 10

SCORE_TEXT_FONT = ("Arial", 16, "bold")

QUESTION_BOARD_WIDTH =  500
QUESTION_BOARD_HEIGHT = 200
QUESTION_TEXT_MAX_WIDTH = QUESTION_BOARD_WIDTH - 10
QUESTION_TEXT_FONT = ("Arial", 22, "normal")
QUESTION_TEXT_POS = {'x': QUESTION_BOARD_WIDTH / 2, 'y': QUESTION_BOARD_HEIGHT / 2}

TRUE_BUTTON_IMAGE_PATHNAME = "Day34_Quizzler/images/true_button.png"
FALSE_BUTTON_IMAGE_PATHNAME = "Day34_Quizzler/images/false_button.png"

QUESTIONS_REQUEST_URL = "https://opentdb.com/api.php"
QUESTIONS_REQUEST_PARAMETERS = {"amount": 10, "type": "boolean"}

CHANGE_QUESTION_DELAY_MS = 500


class QuizApp:

    def __init__(self) -> None:
        self.score = 0
        self.question_number = 1
        self.__initialize_window()
        self.__initialize_widgets()
        self.__load_questions()
        self.__goto_next_question()
        self.window.mainloop()

    
    def __initialize_window(self) -> None:
        self.window = ttk.Tk()
        self.window.title(APP_TITLE)
        self.window.config(padx=WINDOW_PAD, pady=WINDOW_PAD, bg=BLUE_COLOR)


    def __initialize_widgets(self) -> None:
        self.__intialize_score_label()
        self.__initialize_canvas()
        self.__initialize_buttons()


    def __intialize_score_label(self) -> None:
        self.score_label = ttk.Label(text=f"Score: {self.score} / {self.question_number - 1}", 
                                    bg=BLUE_COLOR, fg=WHITE_COLOR, font=SCORE_TEXT_FONT)
        self.score_label.grid(row=0, column=1, pady=WIDGETS_PADY, sticky='e')


    def __initialize_canvas(self) -> None:
        self.question_board = ttk.Canvas(width=QUESTION_BOARD_WIDTH, height=QUESTION_BOARD_HEIGHT, bg=WHITE_COLOR)
        self.question_text = self.question_board.create_text(QUESTION_TEXT_POS['x'], QUESTION_TEXT_POS['y'], 
                                                            width=QUESTION_TEXT_MAX_WIDTH, text="", justify="left", 
                                                            font=QUESTION_TEXT_FONT, fill=BLUE_COLOR)
        self.question_board.grid(row=1, column=0, columnspan=2, pady=WIDGETS_PADY)


    def __initialize_buttons(self) -> None:
        self.true_button_image = ttk.PhotoImage(file=TRUE_BUTTON_IMAGE_PATHNAME)
        self.true_button = ttk.Button(image=self.true_button_image, bg=BLUE_COLOR, activebackground=BLUE_COLOR,
                                      highlightthickness=0, borderwidth=0, command=self.__on_true_button_pressed)
        self.true_button.grid(row=2, column=0)

        self.false_button_image = ttk.PhotoImage(file=FALSE_BUTTON_IMAGE_PATHNAME)
        self.false_button = ttk.Button(image=self.false_button_image, bg=BLUE_COLOR, activebackground=BLUE_COLOR,
                                      highlightthickness=0, borderwidth=0, command=self.__on_false_button_pressed)
        self.false_button.grid(row=2, column=1)


    def __on_true_button_pressed(self) -> None:
        self.check_answer("True")
        self.__update_label()
        self.window.after(ms=CHANGE_QUESTION_DELAY_MS, func=self.__goto_next_question)
        

    def __on_false_button_pressed(self) -> None:
        self.check_answer("False")
        self.__update_label()
        self.window.after(ms=CHANGE_QUESTION_DELAY_MS, func=self.__goto_next_question)


    def __load_questions(self) -> None:
        response = requests.get(url=QUESTIONS_REQUEST_URL, params=QUESTIONS_REQUEST_PARAMETERS)
        response.raise_for_status()
        self.questions_database = response.json()['results']
        self.num_questions = len(self.questions_database)
    

    def __goto_next_question(self) -> None:
        self.question_board.configure(bg=WHITE_COLOR)

        if self.__are_there_questions():
            self.question = self.questions_database.pop(0)
            self.question_board.itemconfig(self.question_text, text= f"Q.{self.question_number}) " +
                                           html.unescape(self.question["question"]))
            self.question_number += 1
        else:
            self.__finish_app()

    
    def __update_label(self) -> None:
        self.score_label.configure(text=f"Score: {self.score} / {self.question_number - 1}")

    
    def check_answer(self, answer: str) -> None:
        if answer == self.question["correct_answer"]:
            self.score += 1
            self.question_board.configure(bg=GREEN_COLOR)
        else:
            self.question_board.configure(bg=RED_COLOR)


    def __are_there_questions(self) -> bool:
        if len(self.questions_database) > 0:
            return True
        else:
            return False


    def __finish_app(self) -> None:
        messagebox.showinfo(title="Quiz Finished!", message=f"Final score: {self.score} / {self.num_questions}")
        self.window.destroy()


if __name__ == "__main__":
    app = QuizApp()
