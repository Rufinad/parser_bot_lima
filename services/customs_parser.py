import random
import time
from datetime import datetime
import locale
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


def is_new(date: str):
    """Функция проверяет новость на новизну (сравнивает с текущей датой)"""
    locale.setlocale(locale.LC_ALL, '')  # иначе русские даты не пашут
    current_date = datetime.now().strftime('%d %B %Y')  # cls str
    # current_date = '26 марта 2024'  # дата приведена для тестирования!!!!!
    form_cur_date = datetime.strptime(current_date, '%d %B %Y')  # cls datetime
    formatted_date = date.replace('a', 'а')  # ебаная таможня использует английские буквы в русских словах
    news_date = datetime.strptime(formatted_date, '%d %B %Y %H:%M')  # cls datetime
    if news_date >= form_cur_date:  # сравнивать можно только объекты datetime
        return True
    return False


def get_custom_news():
    cookie_dict = {'XSRF-TOKEN': 'yJpdiI6Im01WGVmVlpGVGs5TU5jaFlGZHNVYlE9PSIsInZhbHVlIjoiNTM0VHVQXC96NGRNc3ZxZ24yN3ZwcWw3d2ZiWTRhR1RMVGNOZ01DMk9pXC9aUktpdEljWFVJQWNpVEJIY2ZaRnVqIiwibWFjIjoiOWI4YWMwNjYyNjI3YWZjNTJlN2E3ZDk0YWJkNzEyMjJlNzVjYzllZjRhMWQ4ZjY3ZGQ1MmE2YTRmZDRkNGU5MiJ9',
                   'sayt_fts_rossii_session': 'yJpdiI6ImZ5Rnhud0ZoWk42dEhJZUNtbWttMnc9PSIsInZhbHVlIjoiRXVlQTNqcm1id2xSXC92cFE5QXg0M2k2WndPYmpZVjZocVVhRFJVTExyMnYyZGNmcnA3aHdWR2Y2eWt6aGVRYkJaSzhpK3Z5dWlnOTdiTEZmS3lyQlRTR3V0cDM5eHdKZjFnY2hFWEpTSmlvNGxWK0kyRkdBU2g2cHZHM0dIc2NXIiwibWFjIjoiNWFlYTBlNDA1MWQ5MTAxZDA4OWJhOTgyMmI3NjBmNTgwYzMxYzc1NjlmYmE3YTM0NmIxNWUyZDY1MGU2NjQzMiJ9'}
    ua = UserAgent()
    headers = {
    'Host': 'customs.gov.ru',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate',
    'Referer': 'https://customs.gov.ru/press/federal',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    # Requests doesn't support trailers
    # 'Te': 'trailers',
    'Connection': 'close',
    # 'Cookie': 'XSRF-TOKEN=eyJpdiI6IlBUbHlyYnlqY3g4WDJtUzNQMWtWTXc9PSIsInZhbHVlIjoidFZ5WFg4TFNrclV2K1JqQWVqbDJjUjBqTExKN0U5OVl4OHpnSG85VjBXVU1ETzBmMzJqeTlmcEFsUzRUQVlJaSIsIm1hYyI6ImUzZTJjNzdjNDM0ZTllMzA4ZTRkNmM5NWE2MDI1YWYzZTU4OGRiZWM4NjMzYTZjODg3ZmZjYmE2OTJkOWNkNDMifQ%3D%3D; sayt_fts_rossii_session=eyJpdiI6IkUyMWpkUFFDSUJwVXI4bzFlbUZMTHc9PSIsInZhbHVlIjoiMXpMZGxOSlVpdjIxVVFFZUJrWlBjelFsem9vXC9OMjhsNlNpa1VFYU1teis5S0tLdjYrMGkwK2Q2V09pdDFMeDJsNEw3STZUVFZCeHdCV3k2MUVvZFBWYlMrNkVvNmdOSlltTEs0Z1BKWjNmdnp4WGNmckR4elQxWjA5MmgrQmg5IiwibWFjIjoiODc1MWJhNzBkMGE5NjQ5OTgzZTU3ZTdiZTk2NjQ4MmM3NDY4NTlhNmE3ZGUxN2RiZTdmYzk3Zjg2Mjk0ZWVhNyJ9',
}
    url = 'https://customs.gov.ru/press/federal'
    result = []
    with requests.Session() as s:
        response = s.get(url, headers=headers, cookies=cookie_dict)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        if response.status_code == 200:
            top_news = soup.find_all('div', class_=['list-news__header'])
            top_news_datetime = soup.find('div', class_='list-news__big-data').text.strip()
            top_news_href = [x.find('a')['href'] for x in top_news]
            all_news = soup.find_all('div', class_=['list-news__item'])
            all_news_datetime = [x.find('div', class_='list-news__item-data').text.strip() for x in all_news]
            all_news_hrefs = [x.find('a')['href'] for x in all_news]  # все ссылки на новости
            all_news = [list(a) for a in zip(all_news_hrefs, all_news_datetime)]  # ссылка-дата
            only_new = [x for x in all_news if is_new(x[1])]  # только новые ссылки с датами
            only_new.extend([top_news_href, top_news_datetime])
            time.sleep(2)
            for href in only_new:
                try:
                    r = requests.get(url=href[0])
                    time.sleep(random.randint(3, 7))
                    # r.encoding = 'utf-8'
                    card_soup = BeautifulSoup(r.text, 'lxml')
                    # print(card_soup)
                    news_text = card_soup.find('div', class_='pin').text
                    # print(news_text)
                    result.append([href[0], news_text])
                except Exception:
                    continue
            print(result)
            return result


if __name__ == '__main__':
    get_custom_news()
