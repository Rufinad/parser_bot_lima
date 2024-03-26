from datetime import datetime
import locale
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

locale.setlocale(locale.LC_ALL, '')  # иначе русские даты не пашут


def is_new(date: str):
    """Функция проверяет новость на новизну (сравнивает с текущей датой)"""
    current_date = datetime.now().strftime('%d %B %Y')  # cls str
    current_date = '26 марта 2024'  # дата приведена для тестирования!!!!!
    form_cur_date = datetime.strptime(current_date, '%d %B %Y')  # cls datetime
    news_date = datetime.strptime(date, '%d %B %Y')  # cls datetime
    if news_date >= form_cur_date:  # сравнивать можно только объекты datetime
        return True
    return False
def get_sigma_news():
    """Функция парсит сайт и возвращает список из новостей которые еще не были отправлены"""
    result = []
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
            for href in all_news_hrefs:
                r = requests.get(url=href)
                # r.encoding = 'utf-8'
                card_soup = BeautifulSoup(r.text, 'lxml')
                try:
                    date_news = card_soup.find('p', class_='color4').text
                    if is_new(date_news):
                        news_text = card_soup.find('p', attrs={'style': 'text-align: justify'}).text
                        # print(news_text)
                        # Разбиваем текст на строки
                        lines = news_text.split('\n')
                        # Удаляем последние 3 строки (там где написано про оригинал новости)
                        new_text = '\n'.join(lines[:-3])
                        result.append([href, new_text])
                except Exception:
                    continue
            return result  # список списков в котором 0 элемент ссылка, 1 новость


if __name__ == '__main__':
    get_sigma_news()
