import requests
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "PZR1OZ9MS6MQD200"
NEWS_API_KEY = "ba829aadae2c4b91ab4f255f64a32bd6"

stock_url_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_url_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_closing_price = data_list[0]["4. close"]
day_before_yesterday_closing_price = data_list[1]["4. close"]

price_difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
price_difference_in_percentage = abs(price_difference / yesterday_closing_price) * 100

up_down = "🔻"
if price_difference > 0:
    up_down = "🔺"

print(price_difference_in_percentage.__round__(3))

if price_difference_in_percentage > 0.05:
    # retrieve articles
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = response.json()["article"]
    top_3_articles = articles[:3]

    # send message

    formatted_articles = [f"{STOCK_NAME}: {up_down}{price_difference_in_percentage}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in
                          top_3_articles]

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    for article in formatted_articles:
        message = client.messages.create(
            body='Hi there',
            from_='+15017122661',
            to='+15558675310'
        )
