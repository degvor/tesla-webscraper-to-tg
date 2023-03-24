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

# main loop
while True:
    try:
        news = get_news(url_site)
        # finding only new news
        new_news = news - last_news
        # posting news to tg channel
        for item in new_news:
            title, url = item
            url = url_site + url
            send_message(title, url)
        # reload last news
        last_news = news
    except Exception as e:
        print(e)
    # time delay for next check
    time.sleep(15)
