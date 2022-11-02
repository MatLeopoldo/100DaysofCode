from flight_sheet import FlightSheet
from flight_search import FlightSearch
from twilio_sms import SMSHandler
import datetime as dt

TWILIO_ACCOUNT_ID = ""
TWILIO_AUTH_TOKEN = ""
TWILIO_PHONE_NUMBER = ""
DEST_PHONE_NUMBER = "" 

FLIGHT_SHEET_ENDPOINT = "https://api.sheety.co/xxxxxxxxxxxxxxxxxxxxxxxxx/flightDeals/prices"
FLIGHT_SHEET_TOKEN = ""

FLIGHT_SEARCH_KEY = ""

SEARCH_PERIOD_IN_DAYS = 180
CITY_ORIGIN = "London"


def get_date_formatted(date: dt.datetime) -> str:
   return date.strftime("%d/%m/%Y")


def decode_date(date_encoded: str) -> dt.datetime:
   return dt.datetime.strptime(date_encoded, "%Y-%m-%dT%H:%M:%S.000Z")


def get_flight_dates(period_in_days: int) -> tuple:
   date_from = dt.datetime.now() + dt.timedelta(days=1)
   date_to = date_from + dt.timedelta(days=period_in_days)
   return (date_from, date_to)


def add_missing_iata_codes(flight_search: FlightSearch, flight_sheet: FlightSheet) -> None:
   destinations_info = flight_sheet.get_destinations_info()

   for destination in destinations_info:
      if destination['iataCode'] == "":
         city_code = flight_search.get_iata_city_code(destination['city'])
         parameters = {
            'price': {
               'iataCode': city_code
            }
         }
         flight_sheet.update_flight_info(destination['id'], parameters)


def get_cheapest_flights(flight_search: FlightSearch, 
                         destinations_info: list, 
                         city_origin: str,
                         date_from: dt.datetime,
                         date_to: dt.datetime) -> dict:

   origin_code = flight_search.get_iata_city_code(city_origin)
   date_from_formatted = get_date_formatted(date_from)
   date_to_formatted = get_date_formatted(date_to)

   flight_search.set_date_period(date_from_formatted, date_to_formatted)
   flight_search.set_flight_origin(origin_code)
   
   cheapest_flights = {}

   for destination in destinations_info:
      flight_search.set_flight_destiny(destination['iataCode'])
      cheapest_flights[destination['city']] = flight_search.search_cheapest_flight()

   return cheapest_flights


def send_flights_prices(destinations_info: list, cheapest_flights: dict, sms_handler: SMSHandler):
   for destination in destinations_info:
      flight_info = cheapest_flights[destination['city']]
      if flight_info['price'] < destination['lowestPrice']:
         flight_date = decode_date(flight_info['departure_date'])

         message = f"Low price alert! Only Є{flight_info['price']} to fly from " + \
                   f"{flight_info['city_from']}-{flight_info['airport_from']} to " + \
                   f"{flight_info['city_to']}-{flight_info['airport_to']} on " + \
                   f"{get_date_formatted(flight_date)}."
         sms_handler.send_sms_message(DEST_PHONE_NUMBER, message) 


if __name__ == "__main__":
   flight_sheet = FlightSheet(FLIGHT_SHEET_ENDPOINT, FLIGHT_SHEET_TOKEN)
   flight_search = FlightSearch(FLIGHT_SEARCH_KEY)
   sms_handler = SMSHandler(TWILIO_ACCOUNT_ID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER)
   date_from, date_to = get_flight_dates(SEARCH_PERIOD_IN_DAYS)

   add_missing_iata_codes(flight_search, flight_sheet)
   destinations_info = flight_sheet.get_destinations_info()
   cheapest_flights = get_cheapest_flights(flight_search, destinations_info, CITY_ORIGIN, date_from, date_to)
   send_flights_prices(destinations_info, cheapest_flights, sms_handler)



   

    