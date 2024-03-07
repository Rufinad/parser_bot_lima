import random
import time

from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


def get_sigma_news():
    result = {}
    scheme = 'https://www.sigma-soft.ru/'
    ua = UserAgent()
    headers = {'User-Agent': ua.chrome}
    url = 'https://www.sigma-soft.ru/news_vad.shtml?sec=news_vad'
    with requests.Session() as s:
        response = s.get(url, headers=headers)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        if response.status_code == 200:
            news = soup.find_all('a', class_=['news'])
            all_news_hrefs = [scheme + x['href'] for x in news]  # все ссылки по новостям
            # print(all_news_hrefs)
            for href in all_news_hrefs:
            # href= all_news_hrefs[0]
                r = requests.get(url=href)
                # r.encoding = 'utf-8'
                card_soup = BeautifulSoup(r.text, 'lxml')
                news_text = card_soup.find('p', attrs={'style': 'text-align: justify'}).text
                # print(news_text)
                result[href] = news_text
            # print(result)
            return result





if __name__ == '__main__':
    get_sigma_news()