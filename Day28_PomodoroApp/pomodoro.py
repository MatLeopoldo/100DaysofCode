from itertools import count
from pydoc import text
import tkinter as ttk
import time

YELLOW_CODE = "#F8EDE3"
GREEN_CODE = "#90B77D"
RED_CODE = "#FA7070"
WHITE_CODE = "#F9F9F9"
IMAGE_FILEPATH = "Day28_PomodoroApp/tomato.png"
TIME_TEXT_STYLE = ("Courier", 24, "bold")
CHECK_TEXT_STYLE = ("Courier", 26, "bold")
TITLE_TEXT_STYLE = ("Courier", 40, "bold")
TEXT_COLOR = "white"
BUTTON_COLLOR = "white"
WINDOW_APP_PAD = {'x': 100, 'y': 50}
CANVAS_DIMENSIONS = {'x': 200, 'y': 224}
IMAGE_POS = {'x': CANVAS_DIMENSIONS['x'] / 2, 'y': CANVAS_DIMENSIONS['y'] / 2}
TEXT_POS = {'x': CANVAS_DIMENSIONS['x'] / 2, 'y': CANVAS_DIMENSIONS['y'] / 2 + 20}
WORK_TIME_SECONDS = 25 * 60
SHORT_BREAK_SECONDS = 5 * 60
LONG_BREAK_SECONDS = 20 * 60
NUM_CHECKS_CYCLE = 4
RESET_STATE = 0
WORK_STATE = 1
SHORT_BREAK_STATE = 2
LONG_BREAK_STATE = 3
BUTTON_DISABLED = "disabled"
BUTTON_ENABLED = "normal"


class PomodoroApp:

    def __init__(self):
        super().__init__()
        self.num_checks = 1
        self.state = RESET_STATE
        self.config_window()
        self.config_widgets()
        self.window.mainloop()
    

    def config_window(self):
        self.window = ttk.Tk()
        self.window.title("Pomodoro App")
        self.window.config(padx=WINDOW_APP_PAD['x'], pady=WINDOW_APP_PAD['y'], bg=YELLOW_CODE)


    def config_canvas(self):
        self.canvas = ttk.Canvas(width=CANVAS_DIMENSIONS['x'], height=CANVAS_DIMENSIONS['y'], bg=YELLOW_CODE, highlightthickness=0)
        self.tomato_image = ttk.PhotoImage(file=IMAGE_FILEPATH)
        self.canvas.create_image(IMAGE_POS['x'], IMAGE_POS['y'], image=self.tomato_image)
        self.timer_text = self.canvas.create_text(TEXT_POS['x'], TEXT_POS['y'], text="00:00", fill=TEXT_COLOR, font=TIME_TEXT_STYLE)
        self.canvas.grid(row=1, column=1)


    def config_widgets(self):
        self.config_canvas()

        self.state_label = ttk.Label(text='Timer', fg=GREEN_CODE, bg=YELLOW_CODE, font=TITLE_TEXT_STYLE)
        self.state_label.grid(row=0, column=1)

        self.start_button = ttk.Button(text="Start", bg=WHITE_CODE, command=self.start_command, highlightthickness=0)
        self.start_button.grid(row=2, column=0)

        self.reset_button = ttk.Button(text="Reset", bg=WHITE_CODE, command=self.reset_command, highlightthickness=0)
        self.reset_button.grid(row=2, column=2)
        self.reset_button["state"] = BUTTON_DISABLED

        self.check_label = ttk.Label(text="", fg=GREEN_CODE, bg=YELLOW_CODE, font=CHECK_TEXT_STYLE)
        self.check_label.grid(row=3, column=1)


    def count_down(self):

        if self.state != RESET_STATE:
            self.canvas.itemconfig(self.timer_text, text=self.get_timer_string())

            if self.time_sec > 0:
                self.time_sec -= 1
            else:
                self.change_state()

            self.timer_id = self.window.after(1000, self.count_down)


    def start_command(self):
        self.state = WORK_STATE
        self.state_label.config(text='Study', fg=GREEN_CODE)
        self.time_sec = WORK_TIME_SECONDS
        self.start_button["state"] = BUTTON_DISABLED
        self.reset_button["state"] = BUTTON_ENABLED
        self.count_down()


    def reset_command(self):
        self.state = RESET_STATE
        self.window.after_cancel(self.timer_id)
        self.start_button["state"] = BUTTON_ENABLED
        self.reset_button["state"] = BUTTON_DISABLED
        self.state_label.config(text='Timer')
        self.check_label.config(text="")
        self.time_sec = 0
        self.canvas.itemconfig(self.timer_text, text=self.get_timer_string())


    def get_timer_string(self):
        return "{:02}".format(self.time_sec // 60) + ":" + "{:02}".format(self.time_sec % 60)
    

    def change_state(self):
        if self.state == WORK_STATE:
            self.check_label.config(text=self.num_checks * "✓")
            
            if self.num_checks < NUM_CHECKS_CYCLE:
                self.state = SHORT_BREAK_STATE
                self.time_sec = SHORT_BREAK_SECONDS
                self.num_checks += 1
            else:
                self.state = LONG_BREAK_STATE
                self.time_sec = LONG_BREAK_SECONDS
                self.num_checks = 1

            self.state_label.config(text='Break', fg=RED_CODE)            
        else:
            if self.state == LONG_BREAK_STATE:
                self.check_label.config(text='')

            self.state = WORK_STATE
            self.time_sec = WORK_TIME_SECONDS
            self.state_label.config(text='Study', fg=GREEN_CODE)


if __name__ == "__main__":
    app = PomodoroApp()