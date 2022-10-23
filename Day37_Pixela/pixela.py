import requests
import datetime as dt


CREATE_USER_ENDPOINT = "https://pixe.la/v1/users"
MY_USERNAME = "my_username"
MY_TOKEN = "my_token"
CREATE_USER_PARAMETERS = {
    'token': MY_TOKEN,
    'username': MY_USERNAME,
    'agreeTermsOfService': "yes",
    'notMinor': "yes",
}

CREATE_GRAPH_ENDPOINT = f"https://pixe.la/v1/users/{MY_USERNAME}/graphs" 
GRAPH_ID = "graph1"
GRAPH_NAME = "Cycling Graph"
GRAPH_UNIT = "Km"
GRAPH_TYPE = "float"
GRAPH_COLOR = "sora"
CREATE_GRAPH_PARAMETERS = {
    'id': GRAPH_ID,
    'name': GRAPH_NAME,
    'unit': GRAPH_UNIT,
    'type': GRAPH_TYPE,
    'color': GRAPH_COLOR 
}

ADD_PIXEL_ENDPOINT = f"https://pixe.la/v1/users/{MY_USERNAME}/graphs/{GRAPH_ID}"

REQUEST_HEADERS = {
    'X-USER-TOKEN': MY_TOKEN
}


def create_pixela_user() -> bool:
    response = requests.post(url=CREATE_USER_ENDPOINT, json=CREATE_USER_PARAMETERS)

    if response.json()['isSuccess']:
        print("User created successfully!")
        return True
    else:
        print(f"It was not possible to create a user: {response.json()['message']}")
        return False
    

def create_pixela_graph() -> bool:
    response = requests.post(url=CREATE_GRAPH_ENDPOINT, json=CREATE_GRAPH_PARAMETERS, headers=REQUEST_HEADERS)
    print(response.json())

    if response.json()['isSuccess']:
        print("Graph created successfully!")
        return True
    else:
        print(f"It was not possible to create a graph: {response.json()['message']}")
        return False


def get_date_formatted(date: dt.datetime) -> str:
    return dt.datetime.strftime(date, "%Y%m%d")


def add_exercise_note(date: dt.datetime, distance: float) -> bool:
    add_pixel_parameters = {
        'date': get_date_formatted(date),
        'quantity': str(distance)
    }
    response = requests.post(url=ADD_PIXEL_ENDPOINT, json=add_pixel_parameters, headers=REQUEST_HEADERS)

    if response.json()['isSuccess']:
        print("Exercise note added successfully!")
        return True
    else:
        print(f"It was not possible to add exercise note: {response.json()['message']}")
        return False


def update_exercise_note(date: dt.datetime, distance: float) -> bool:
    update_pixel_endpoint = f"{ADD_PIXEL_ENDPOINT}/{get_date_formatted(date)}"
    update_pixel_parameters = {
        'quantity': str(distance)
    }
    response = requests.put(url=update_pixel_endpoint, json=update_pixel_parameters, headers=REQUEST_HEADERS)

    if response.json()['isSuccess']:
        print("Exercise note updated successfully!")
        return True
    else:
        print(f"It was not possible to update exercise note: {response.json()['message']}")
        return False


def delete_exercise_note(date: dt.datetime) -> bool:
    delete_pixel_endpoint = f"{ADD_PIXEL_ENDPOINT}/{get_date_formatted(date)}"
    response = requests.delete(url=delete_pixel_endpoint, headers=REQUEST_HEADERS)

    if response.json()['isSuccess']:
        print("Exercise note deleted successfully!")
        return True
    else:
        print(f"It was not possible to delete exercise note: {response.json()['message']}")
        return False


if __name__ == "__main__":
    yesterday_date = dt.datetime(year=2022, month=10, day=22)
    delete_exercise_note(yesterday_date)