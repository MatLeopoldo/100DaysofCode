import requests


class FlightSheet:
    
    def __init__(self, api_endpoint: str, api_token: str) -> None:
        self.endpoint = api_endpoint
        self.headers = {'Authorization': api_token}

    
    def get_destinations_info(self) -> list:
        response = requests.get(url=self.endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()['prices']

    
    def update_flight_info(self, object_id: int, flight_info: dict) -> None:
        endpoint = f"{self.endpoint}/{object_id}"
        response = requests.put(url=endpoint, json=flight_info, headers=self.headers)
        response.raise_for_status()
