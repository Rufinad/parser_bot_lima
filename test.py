from datetime import datetime
import locale
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

def get_custom_news():
    ua = UserAgent()
    headers = {'User-Agent': ua.chrome}
    url = 'https://customs.gov.ru/press/federal'

    with requests.Session() as s:
        response = s.get(url, headers=headers)
        cookies = response.cookies
        for cookie in cookies:
            print(f"Имя: {cookie.name}, Значение: {cookie.value}")
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')



if __name__ == '__main__':
    get_custom_news()