import datetime as dt
import time
import smtplib
import requests


SUNSET_SUNRISE_URL = "https://api.sunrise-sunset.org/json"
MY_LATITUDE = -23.179140
MY_LONGITUDE = -45.887241
REQUEST_PARAMETERS = {"lat": MY_LATITUDE, "lng": MY_LONGITUDE, "formatted": 0}

ISS_POSITION_URL = "http://api.open-notify.org/iss-now.json"
MAX_LAT_LONG_DIFF = 5.0


SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587
MY_EMAIL = "my_email@gmail.com"
MY_PASSWORD = "my_password"
EMAIL_MESSAGE = "Subject:Look up!\n\nThe ISS is above in the sky!"

DELAY_IN_SECONDS = 60


def get_ISS_position():
    response = requests.get(url=ISS_POSITION_URL)
    response.raise_for_status()
    latitude = float(response.json()["iss_position"]["latitude"])
    longitude = float(response.json()["iss_position"]["longitude"])
    return (latitude, longitude)


def get_sunrise_sunset_hour():
    response = requests.get(url=SUNSET_SUNRISE_URL, params=REQUEST_PARAMETERS)
    response.raise_for_status()
    sunrise_time = response.json()["results"]["sunrise"].split("T")[1]
    sunset_time = response.json()["results"]["sunset"].split("T")[1]
    sunrise_hour = int(sunrise_time.split(":")[0])
    sunset_hour = int(sunset_time.split(":")[0])

    return (sunrise_hour, sunset_hour)


def is_ISS_close_to_me():
    iss_lat, iss_long = get_ISS_position()

    if abs(iss_lat - MY_LATITUDE) < MAX_LAT_LONG_DIFF and abs(iss_long - MY_LONGITUDE) < MAX_LAT_LONG_DIFF:
        return True
    else:
        return False


def is_sundown():
    sunrise_hour, sunset_hour = get_sunrise_sunset_hour()
    timenow = dt.datetime.now()

    if timenow.hour < sunrise_hour or timenow.hour > sunset_hour:
        return True
    else:
        return False


def send_email(email_message):
    connection = smtplib.SMTP(host=SMTP_HOST, port=SMTP_PORT)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.send_message(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, text_message=email_message)
    connection.close()


if __name__ == "__main__":
    
    while True:
        time.sleep(DELAY_IN_SECONDS)

        if is_ISS_close_to_me() and is_sundown():
            send_email(EMAIL_MESSAGE)
        else:
            print("Waiting ISS to be close to you...")

