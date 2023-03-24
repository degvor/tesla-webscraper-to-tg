import requests
from bs4 import BeautifulSoup
import time
from Token import *

# Url of site that we are scraping from
url_site = 'https://www.tesmanian.com'

# Url for posting by tg bot to tg channel
telegram_url = token

# Last news saving variable
last_news = set()

# creating function to post by tg bot to tg channel
def send_message(title, url):
    message = title + '\n' + url
    response = requests.get(telegram_url + message)
    return response.json()

# function for scraping data from site
def get_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_list = soup.find_all('p', class_='h3')
    news = set()
    for item in news_list:
        title = item.a.text.strip()
        url = item.a.get('href')
        news.add((title, url))
    return news
