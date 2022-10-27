import requests
import datetime as dt

MY_GENDER = "male"
MY_WEIGHT_KG = 91
MY_HEIGHT_CM = 189
MY_AGE = 26

NUTRITION_API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITION_API_ID = "xxxxxxxxxxxxxxxxxxxx"
NUTRITION_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"
NUTRITION_API_HEADERS = {
    'x-app-id': NUTRITION_API_ID,
    'x-app-key': NUTRITION_API_KEY,
    'Content-Type': 'application/json' 
}

SPREADSHEET_API_ENDPOINT = "https://api.sheety.co/xxxxxxxxxxxxxxxxxxxxxxxx/myWorkouts/workouts"
SPREADSHEET_API_TOKEN = "Bearer xxxxxxxxxxxxxxxxxxxxxxxx"
SPREADSHEET_API_HEADERS = {
    'Authorization': SPREADSHEET_API_TOKEN,
}


def get_exercises_stats(user_workout: str) -> list:
    nutrition_api_params = {
        'query': user_workout,
        'gender': MY_GENDER,
        'weight_kg': MY_WEIGHT_KG,
        'height_cm': MY_HEIGHT_CM,
        'age': MY_AGE
    }
    response = requests.post(url=NUTRITION_API_ENDPOINT, json=nutrition_api_params, headers=NUTRITION_API_HEADERS)
    response.raise_for_status()
    exercises_stats = [{'exercise': exercise_info['name'], 'duration': exercise_info['duration_min'], 
                        'calories': exercise_info['nf_calories']} for exercise_info in response.json()['exercises']]
    return exercises_stats


def get_date_formatted(date: dt.datetime) -> str:
    return dt.datetime.strftime(date, '%d/%m/%Y')


def get_time_formatted(date: dt.datetime) -> str:
    return dt.datetime.strftime(date, '%H:%M:%S')


def write_in_spreadsheet(exercise_stats: dict, date: dt.datetime):
    spreadsheet_parameters = {
        'workout': {
            'date': get_date_formatted(date),
            'time': get_time_formatted(date),
            'exercise': exercise_stats['exercise'].title(),
            'duration': exercise_stats['duration'],
            'calories': exercise_stats['calories']
        }
    }
    response = requests.post(url=SPREADSHEET_API_ENDPOINT, json=spreadsheet_parameters,headers=SPREADSHEET_API_HEADERS)
    return response.json()

if __name__ == "__main__":
    time_now = dt.datetime.now()
    user_workout = input("Tell me which exercises you did: ")
    exercises_stats = get_exercises_stats(user_workout)

    for stats in exercises_stats:
        print(write_in_spreadsheet(stats, time_now))