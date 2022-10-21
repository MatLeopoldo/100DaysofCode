import requests
from twilio.rest import Client 

MY_ACCOUNT_SID = "xxxxxxxxxxxxxxxxxxxxxxxx"
MY_AUTH_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxx"
PHONE_NUMBER = {'from': "+xxxxxxxxxxxx", 'to': "+xxxxxxxxxxxx"}
SMS_MESSAGE = "It's gonna rain tomorrow. Take an umbrella before going to work."

MY_LATITUDE = -23.179140
MY_LONGITUDE = -45.887241
MY_APP_KEY = "xxxxxxxxxxxxxxxxxxxxxxxx"

WEATHER_REQUEST_URL = "https://api.openweathermap.org/data/2.5/forecast"
WEATHER_REQUEST_PARAMETERS = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "cnt": 8,
    "appid": MY_APP_KEY,}

POSSIBLE_RAINING_CONDITIONS = ["Thunderstorm", "Drizzle", "Rain"]


def get_weather_info():
    response = requests.get(url=WEATHER_REQUEST_URL, params=WEATHER_REQUEST_PARAMETERS)
    response.raise_for_status()
    weather_data = response.json()
    return weather_data


def is_gonna_rain_tomorrow(weather_tomorrow):
    for three_hours_data in weather_tomorrow['list']:
        weather_condition = three_hours_data['weather'][0]["main"]
        if weather_condition in POSSIBLE_RAINING_CONDITIONS:
            return True
    return False


def send_sms_alert():
    client = Client(MY_ACCOUNT_SID, MY_AUTH_TOKEN) 
    message = client.messages.create(to=PHONE_NUMBER["to"], from_=PHONE_NUMBER["from"], body=SMS_MESSAGE)
    print(message.status)


if __name__ == "__main__":
    weather_tomorrow = get_weather_info()
    if is_gonna_rain_tomorrow(weather_tomorrow):
        send_sms_alert()

