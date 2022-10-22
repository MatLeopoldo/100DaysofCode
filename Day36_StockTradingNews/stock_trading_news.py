import requests
import datetime as dt
from twilio.rest import Client 

SMS_ACCOUNT_SID = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
SMS_AUTH_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PHONE_NUMBER = {'from': "+xxxxxxxxxxx", 'to': "+xxxxxxxxxxxxx"}

COMPANY_SYMBOL = "TSLA"
STOCK_PRICES_OUTPUT_SIZE = "compact"
STOCK_PRICES_FUNCTION = "TIME_SERIES_DAILY"
STOCK_PRICES_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
STOCK_PRICES_REQUEST_URL = "https://www.alphavantage.co/query"
STOCK_PRICES_REQUEST_PARAMS = {
    'function': STOCK_PRICES_FUNCTION,
    'symbol': COMPANY_SYMBOL,
    'outputsize': STOCK_PRICES_OUTPUT_SIZE,
    'apikey': STOCK_PRICES_API_KEY,
}

NEWS_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
NEWS_REQUEST_URL = "https://newsapi.org/v2/everything"
NEWS_KEYWORD = "Tesla"
NEWS_ENGLISH_LANGUAGE = "en"
NEWS_SORT_BY_POPULARITY = "popularity"
NUMBER_OF_ARTICLES = 3

STOCK_PRICE_TRIGGER_DIFF_PERCENTAGE = 3


def get_stock_prices():
    response = requests.get(url=STOCK_PRICES_REQUEST_URL, params=STOCK_PRICES_REQUEST_PARAMS)
    response.raise_for_status()
    return response.json()['Time Series (Daily)']


def get_yesterday_date():
    return dt.datetime.strftime(dt.datetime.now() - dt.timedelta(days=1), '%Y-%m-%d')


def get_day_before_yesterday_date():
    return dt.datetime.strftime(dt.datetime.now() - dt.timedelta(days=2), '%Y-%m-%d')


def get_stock_prices_daily_diff(stock_prices):
    """
    Return the difference, in percentage, between the final stock 
    price from yesterday and the day before yesterday.
    """
    yesterday_date = get_yesterday_date()
    day_before_date = get_day_before_yesterday_date()
    yesterday_closed_price = float(stock_prices[yesterday_date]['4. close'])
    day_before_closed_price = float(stock_prices[day_before_date]['4. close'])
    diff_percentage = (yesterday_closed_price - day_before_closed_price) * 100 / day_before_closed_price
    return diff_percentage


def get_company_most_popular_articles():
    """
    Return the 3 most popular articles about the company written yesterday.
    """
    yesterday_date = get_yesterday_date()      

    params = {
        'q': NEWS_KEYWORD,
        'language': NEWS_ENGLISH_LANGUAGE,
        'from':yesterday_date,
        'to':yesterday_date,
        'sortBy': NEWS_SORT_BY_POPULARITY,
        'apiKey': NEWS_API_KEY,
    }
    response = requests.get(url=NEWS_REQUEST_URL, params=params)
    response.raise_for_status()
    most_popular_articles = response.json()['articles'][:NUMBER_OF_ARTICLES]
    return most_popular_articles


def get_stock_difference_text(stock_difference):
    if stock_difference > 0:
        symbol = "⬆"
    else:
        symbol = "⬇"
    return f"Tesla: {symbol} {round(abs(stock_difference), 2)} %"


def send_company_articles_by_sms(company_articles, stock_difference):
    stock_diff_text = get_stock_difference_text(stock_difference)
    client = Client(SMS_ACCOUNT_SID, SMS_AUTH_TOKEN)

    for article in company_articles:
        sms_message = f"{stock_diff_text}\nHeadline: {article['title']}.\nBrief: {article['description']}"
        message = client.messages.create(from_=PHONE_NUMBER['from'], to=PHONE_NUMBER['to'], body=sms_message)
        print(message)


if __name__ == "__main__":
    tesla_stock_prices = get_stock_prices()
    diff_percentage = get_stock_prices_daily_diff(tesla_stock_prices)

    if diff_percentage > STOCK_PRICE_TRIGGER_DIFF_PERCENTAGE:
        company_news = get_company_most_popular_articles()
        send_company_articles_by_sms(company_news, diff_percentage)