import requests
import datetime

def fetch_latest_news(api_key, news_keywords="", lookback_days=10):
    if news_keywords == "":
        raise AssertionError("No input for the keyword is given")

    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z']

    for letter in news_keywords:
        if letter.lower() not in alphabets:
            raise AssertionError(f"Invalid news_keywords input! It contains non-alphabetical character: {news_keywords}")

    # Find the date that I should find the news articles from using lookback_days
    current_date = datetime.date.today()
    lookback_date = current_date - datetime.timedelta(days=lookback_days)

    url = f'https://newsapi.org/v2/everything?' \
       f'q={news_keywords}&' \
       f'from={lookback_date}&' \
       f'language=en&' \
       f'apiKey={api_key}' \

    response = requests.get(url)

    return response.json()