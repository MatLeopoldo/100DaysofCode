import tkinter as ttk
from tkinter import messagebox
import os
import csv
import random as rd

APP_PADDING = 50
CANVAS_SQUARE_LENGTH = 330
WEBSITE_ENTRY_LENGTH = 40
USER_ENTRY_LENGTH = 40
PASSWORD_ENTRY_LENGTH = 20
PASSWORD_BUTTON_LENGTH = 16
ADD_BUTTON_LENGTH = 37
WIDGETS_PADX = 5
WIDGETS_PADY = 2
LOGO_COORDINATES = {'x': CANVAS_SQUARE_LENGTH / 2, 'y': CANVAS_SQUARE_LENGTH / 2}
LOGO_PATHNAME = "Day29_PasswordManager/logo.png"
PASSWORD_FILE_PATHNAME = "Day29_PasswordManager/passwords_list.csv"
USER_ENTRY_DEFAULT_VALUE = "my_email@gmail.com"
PASSWORD_FILE_COLUMNS_NAMES = ["Website", "User", "Password"]

letters = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+']


class PasswordApp(ttk.Tk):

    def __init__(self):
        super().__init__()
        self.__initialize_window()
        self.__initialize_widgets()
        self.__create_csv_file()


    def __initialize_window(self):
        self.title("Password Manager")
        self.config(padx=APP_PADDING, pady=APP_PADDING, background="white")
        self.canvas = ttk.Canvas(self, width=CANVAS_SQUARE_LENGTH, height=CANVAS_SQUARE_LENGTH, background="white", highlightthickness=0)
        self.app_logo = ttk.PhotoImage(file=LOGO_PATHNAME)
        self.canvas.create_image(LOGO_COORDINATES['x'], LOGO_COORDINATES['y'], image=self.app_logo)
        self.canvas.grid(row=0, column=0, columnspan=3, padx=WIDGETS_PADX, pady=WIDGETS_PADY)


    def __initialize_widgets(self):
       self.__initialize_website_widgets()
       self.__initialize_user_widgets()
       self.__initialize_password_widgets()
       self.__initialize_add_button()

        
    def __initialize_website_widgets(self):
        self.website_label = ttk.Label(text="Website:", background="white")
        self.website_label.grid(row=1, column=0, sticky='e', padx=WIDGETS_PADX, pady=WIDGETS_PADY)

        self.website_entry = ttk.Entry(width=WEBSITE_ENTRY_LENGTH)
        self.website_entry.grid(row=1, column=1, columnspan=2, sticky='w', pady=WIDGETS_PADY)
        self.website_entry.focus()


    def __initialize_user_widgets(self):
        self.user_label = ttk.Label(text="Email/Username:", background="white")
        self.user_label.grid(row=2, column=0, sticky='e', padx=WIDGETS_PADX, pady=WIDGETS_PADY)

        self.user_entry = ttk.Entry(width=USER_ENTRY_LENGTH)
        self.user_entry.grid(row=2, column=1, columnspan=2, sticky='w', pady=WIDGETS_PADY)
        self.user_entry.insert(0, USER_ENTRY_DEFAULT_VALUE)


    def __initialize_password_widgets(self):
        self.password_label = ttk.Label(text="Password:", background="white")
        self.password_label.grid(row=3, column=0, sticky='e', padx=WIDGETS_PADX, pady=WIDGETS_PADY)

        self.password_entry = ttk.Entry(width=PASSWORD_ENTRY_LENGTH)
        self.password_entry.grid(row=3, column=1, sticky='w', pady=WIDGETS_PADY)

        self.gen_password_button = ttk.Button(text="Generate Password", background="white", 
                                              command=self.__generate_password, width=PASSWORD_BUTTON_LENGTH)
        self.gen_password_button.grid(row=3, column=2, sticky='w', padx=WIDGETS_PADX, pady=WIDGETS_PADY)

    
    def __initialize_add_button(self):
        self.add_button = ttk.Button(text="Save", background="white", command=self.__save_data, width=ADD_BUTTON_LENGTH)
        self.add_button.grid(row=4, column=1, columnspan=2, sticky='w', pady=WIDGETS_PADY)


    def __save_data(self):
        website = self.website_entry.get()
        user = self.user_entry.get()
        password = self.password_entry.get()

        if website != "" and user != "" and password != "":
            if messagebox.askokcancel(title=website, message=self.__create_info_text(user, password)):
                with open(PASSWORD_FILE_PATHNAME, 'a') as psw_file:
                    csv_writer = csv.writer(psw_file)
                    csv_writer.writerow([website, user, password])
            
                self.website_entry.delete(0, ttk.END)
                self.password_entry.delete(0, ttk.END)
        else:
            messagebox.showwarning(title="Empty field(s)", message="Please, make sure all fields are filled.")
    

    def __generate_password(self):
        letter_list = [rd.choice(letters) for _ in range(rd.randint(8, 10))]
        number_list = [rd.choice(digits) for _ in range(rd.randint(2, 4))]
        symbol_list = [rd.choice(symbols) for _ in range(rd.randint(2, 4))]
        password_list = letter_list + number_list + symbol_list
        rd.shuffle(password_list)
        self.password_entry.delete(0, ttk.END)
        self.password_entry.insert(0, ''.join(password_list))
        

    def __create_csv_file(self):
        if not os.path.isfile(PASSWORD_FILE_PATHNAME):
            with open(PASSWORD_FILE_PATHNAME, 'a') as psw_file:
                csv_writer = csv.writer(psw_file)
                csv_writer.writerow(PASSWORD_FILE_COLUMNS_NAMES)

    
    def __create_info_text(self, user, password):
        info_text = "These are the details entered:\n"
        user_text = "Username/Email: " + user + "\n"
        password_text = "Password: " + password + "\n"
        question_text = "Is it ok to save?"
        return info_text + user_text + password_text + question_text


if __name__ == "__main__":
    app = PasswordApp()
    app.mainloop()