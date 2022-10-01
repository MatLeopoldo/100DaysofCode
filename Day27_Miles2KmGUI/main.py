import tkinter as ttk
from unittest import result

WINDOW_MIN_WIDTH = 270
WINDOW_MIN_HEIGHT = 100
WINDOW_PADX = 20
WINDOW_PADY = 20
WINDOW_TITLE = "Mile to Km Converter"


def initialize_window():
    window = ttk.Tk()
    window.minsize(width=WINDOW_MIN_WIDTH, height=WINDOW_MIN_HEIGHT)
    window.title(WINDOW_TITLE)
    window.config(padx=WINDOW_PADX, pady=WINDOW_PADY)
    return window


def convert_miles_to_km():
    miles_val = float(miles_entry.get())
    result_label.config(text=f"{miles_val * 1.60934}")
    

if __name__ == "__main__":
    app_window = initialize_window()
    
    miles_entry = ttk.Entry(width=10)
    miles_entry.grid(row=0, column=1)

    miles_label = ttk.Label(text="Miles")
    miles_label.grid(row=0, column=2)

    is_equal_label = ttk.Label(text="is equal to ")
    is_equal_label.grid(row=1, column=0)

    result_label = ttk.Label(text="0")
    result_label.grid(row=1, column=1)

    kilometers_label = ttk.Label(text="Km")
    kilometers_label.grid(row=1, column=2)

    calculate_button = ttk.Button(text="Calculate", command=convert_miles_to_km)
    calculate_button.grid(row=2, column=1)

    app_window.mainloop()