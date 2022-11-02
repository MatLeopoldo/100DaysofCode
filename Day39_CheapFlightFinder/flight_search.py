import requests

FLIGHT_SEARCH_SERVER = "https://api.tequila.kiwi.com"


class FlightSearch:

    def __init__(self, api_key) -> None:
        self.headers = {
            'accept': 'application/json',
            'apikey': api_key
        }
        self.origin = ""
        self.destiny = ""
        self.date_from = ""
        self.date_to = ""


    def get_iata_city_code(self, city_name: str) -> str:
        endpoint = FLIGHT_SEARCH_SERVER + "/locations/query"
        parameters = {
            'term': city_name,
            'location_types': "city",
        }
        response = requests.get(url=endpoint, params=parameters, headers=self.headers)
        response.raise_for_status()
        city_code = response.json()['locations'][0]['code']
        return city_code

    
    def set_flight_origin(self, city_code: str) -> None:
        self.origin = city_code
    

    def set_flight_destiny(self, city_code: str) -> None:
        self.destiny = city_code

    
    def set_date_period(self, date_from: str, date_to: str) -> None:
        self.date_from = date_from
        self.date_to = date_to

    
    def search_cheapest_flight(self) -> list:
        endpoint = FLIGHT_SEARCH_SERVER + "/v2/search"
        parameters = {
            'fly_from': self.origin,
            'fly_to': self.destiny,
            'date_from': self.date_from,
            'date_to': self.date_to,
            'one_for_city': 1,
        }
        response = requests.get(url=endpoint, params=parameters, headers=self.headers)
        response.raise_for_status()
        flight_data = response.json()

        flight_info = {}
        flight_info['city_from'] = flight_data['data'][0]['cityFrom']
        flight_info['city_to'] = flight_data['data'][0]['cityTo']
        flight_info['airport_from'] = flight_data['data'][0]['flyFrom']
        flight_info['airport_to'] = flight_data['data'][0]['flyTo']
        flight_info['departure_date'] = flight_data['data'][0]['local_departure']
        flight_info['price'] = flight_data['data'][0]['price']
        return flight_info
