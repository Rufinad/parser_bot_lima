import random
import time

from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


def get_fts_news():
    ua = UserAgent()
    headers = {'User-Agent': ua.chrome}
    url = 'https://ved.today/category/novosti-tamozhni'
    with requests.Session() as s:
        response = s.get(url, headers=headers)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        if response.status_code == 200:
            news = soup.find_all('div', class_=['biglast_item item'])
            all_news_hrefs = [x.find('a')['href'] for x in news]  # все ссылки по новостям
            all_news_headers = [x.find('h3').text for x in news]  # все заголовки по новостям
            all_news_content = [x.find('p').text for x in news]  # тексты новостей

            result = [list(a) for a in zip(all_news_hrefs, all_news_headers, all_news_content)]
            # print(result[0][0])
            print(result[0])
            return result[0]




if __name__ == '__main__':
    get_fts_news()