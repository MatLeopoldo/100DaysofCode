"""
Automated Birthday Wisher
"""
import pandas as pd
import datetime as dt
import random as rd
import smtplib

BIRTHDAY_LIST_FILENAME = "Day32_ABWProject/birthdays.csv"
LETTER_1_FILENAME = "Day32_ABWProject/letter_templates/letter_1.txt"
LETTER_2_FILENAME = "Day32_ABWProject/letter_templates/letter_2.txt"
LETTER_3_FILENAME = "Day32_ABWProject/letter_templates/letter_3.txt"
LETTERS_LIST = [LETTER_1_FILENAME, LETTER_2_FILENAME, LETTER_3_FILENAME]

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
MY_EMAIL = "my_email@gmail.com"
MY_PASSWORD = "my_password"


def load_birthday_list(filepath):
    try:
        birthdays_csv = pd.read_csv(filepath)
    except FileNotFoundError:
        return []
    else:
        return [{"name": row['name'], "email": row["email"], "day": row["day"], 
                 "month": row["month"]} for _,row in birthdays_csv.iterrows()] 


def get_birthday_text(birthday_person):
    letter_text = ""
    try:
        with open(rd.choice(LETTERS_LIST), 'r') as letter_file:
            letter_text = letter_file.read().replace('[NAME]', birthday_person)
    except FileNotFoundError:
        print("Letter file not found.")
    finally:
        return letter_text


def send_email(message, to_email):
    try:
        connection = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.send_message(from_addr=MY_EMAIL, to_addrs=to_email, message=message)
        connection.close()
    except smtplib.SMTPServerDisconnected as error:
        print("It was not possible to connect: " + str(error))


def check_birthday_list(birthday_list):
    today_date = dt.datetime.now()
    for person in birthday_list:
        if person["day"] == today_date.day and person["month"] == today_date.month:
            email_message = "Subject: Happy Birthday\n\n" + get_birthday_text(person['name'])
            send_email(email_message, person['email'])


if __name__ == "__main__":
    birthday_list = load_birthday_list(BIRTHDAY_LIST_FILENAME)
    check_birthday_list(birthday_list)