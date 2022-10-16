import tkinter as ttk
import pandas as pd
import random as rd
import os.path

WINDOW_PAD_VALUE = 50
CARD_WIDTH = 800
CARD_HEIGHT = 526
GREEN_COLOR = "#C6EBC5"
WHITE_COLOR = "#FFFFFF"
BLACK_COLOR = "#000000"
CARD_FRONT_PATHNAME = "Day31_FlashCard/images/card_front.png"
CARD_BACK_PATHNAME = "Day31_FlashCard/images/card_back.png"
OK_ICON_PATHNAME = "Day31_FlashCard/images/ok_icon.png"
NOT_OK_ICON_PATHNAME = "Day31_FlashCard/images/not_ok_icon.png"
ENGLISH_WORDS_PATHNAME = "Day31_FlashCard/Data/english_words.csv"
WORDS_TO_LEARN_PATHNAME = "Day31_FlashCard/Data/words_to_learn.csv"
LANGUAGE_FONT_STYLE = ("Arial", 40, "italic")
LANGUAGE_LABEL_POSITION = {'x': CARD_WIDTH / 2, 'y': 150}
WORD_FONT_STYLE = ("Arial", 55, "bold")
WORD_LABEL_POSITION = {'x': CARD_WIDTH / 2, 'y': 263}
CANVAS_ICON_DIMENSIONS = {'x': 100, 'y': 100}
CARD_POSITION_COORDS = {'x': CARD_WIDTH / 2, 'y': CARD_HEIGHT / 2}
LANGUAGES = ["Inglês", "Português"]


class FlashCardApp:
    
    def __init__(self):
        self.__load_words_database()
        self.__initialize_window()
        self.__initialize_card()
        self.__initialize_buttons()
        self.window.mainloop()


    def __load_words_database(self):
        if os.path.exists(WORDS_TO_LEARN_PATHNAME):
            self.words = pd.read_csv(WORDS_TO_LEARN_PATHNAME).to_dict('records')
        else:
            self.words = pd.read_csv(ENGLISH_WORDS_PATHNAME).to_dict('records')
        self.language = LANGUAGES[0]
        self.__choose_random_word()
        

    def __choose_random_word(self):
        self.word_displayed = rd.choice(self.words)

    
    def __change_language(self):
        if self.language == LANGUAGES[0]:
            self.language = LANGUAGES[1]
        else:
            self.language = LANGUAGES[0]


    def __initialize_window(self):
        self.window = ttk.Tk()
        self.window.title("Flash Card")
        self.window.config(padx=WINDOW_PAD_VALUE, pady=WINDOW_PAD_VALUE, background=GREEN_COLOR)

    
    def __initialize_card(self):
        self.card_front_image = ttk.PhotoImage(file=CARD_FRONT_PATHNAME)
        self.card_back_image = ttk.PhotoImage(file=CARD_BACK_PATHNAME)
        self.card_canvas = ttk.Canvas(width=CARD_WIDTH, height=CARD_HEIGHT, bg=GREEN_COLOR, highlightthickness=0)
        self.card_image = self.card_canvas.create_image(CARD_POSITION_COORDS['x'], CARD_POSITION_COORDS['y'], 
                                                        image=self.card_front_image)
        self.card_language = self.card_canvas.create_text(LANGUAGE_LABEL_POSITION['x'], LANGUAGE_LABEL_POSITION['y'], 
                                                          font=LANGUAGE_FONT_STYLE, text=self.language)
        self.card_word = self.card_canvas.create_text(WORD_LABEL_POSITION['x'], WORD_LABEL_POSITION['y'], 
                                                     font=WORD_FONT_STYLE, text=self.word_displayed[self.language])
        self.card_canvas.bind("<Button-1>", func=self.__on_card_clicked)
        self.card_canvas.grid(row=0, column=0, columnspan=2, pady=20)
    

    def __initialize_buttons(self):
        self.ok_image = ttk.PhotoImage(file=OK_ICON_PATHNAME)
        self.ok_button = ttk.Button(image=self.ok_image, bg=GREEN_COLOR, activebackground=GREEN_COLOR,
                                    highlightthickness=0, borderwidth=0, command=self.__on_ok_button_pressed)
        self.ok_button.grid(row=1, column=1)

        self.not_ok_image = ttk.PhotoImage(file=NOT_OK_ICON_PATHNAME)
        self.not_ok_button = ttk.Button(image=self.not_ok_image, bg=GREEN_COLOR, activebackground=GREEN_COLOR,
                                        highlightthickness=0, borderwidth=0, command=self.__on_not_ok_button_pressed)
        self.not_ok_button.grid(row=1, column=0)


    def __on_ok_button_pressed(self):
        self.__change_card()
        self.words.remove(self.word_displayed)
        words_dataframe = pd.DataFrame(self.words)
        words_dataframe.to_csv(WORDS_TO_LEARN_PATHNAME, index=False)

    
    def __on_not_ok_button_pressed(self):
        self.__change_card()
    

    def __change_card(self):
        self.language = LANGUAGES[0]
        self.__choose_random_word()
        self.__update_card()

    
    def __on_card_clicked(self, event):
        self.__change_language()
        self.__update_card()
    
    def __update_card(self):
        if self.language == LANGUAGES[0]:
            font_color = BLACK_COLOR
            card_image = self.card_front_image
        else:
            font_color = WHITE_COLOR
            card_image = self.card_back_image

        self.card_canvas.itemconfig(self.card_image, image=card_image)
        self.card_canvas.itemconfig(self.card_word, text=self.word_displayed[self.language], fill=font_color)
        self.card_canvas.itemconfig(self.card_language, text=self.language, fill=font_color)


if __name__ == "__main__":
    app = FlashCardApp()

