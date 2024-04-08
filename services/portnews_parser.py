from datetime import datetime
import locale
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


def is_new(date: str):
    """Функция проверяет новость на новизну (сравнивает с текущей датой)"""
    locale.setlocale(locale.LC_ALL, '')  # иначе русские даты не пашут
    current_date = datetime.now().strftime('%d %B %Y')  # cls str
    # current_date = ' 26 Янв 2024г'  # дата приведена для тестирования!!!!!
    form_cur_date = datetime.strptime(current_date, '%d %B %Y')  # cls datetime
    # print(form_cur_date)
    news_date = datetime.strptime(date, '%d %B %Y')  # cls datetime
    if news_date >= form_cur_date:  # сравнивать можно только объекты datetime
        return True
    return False


def get_fts_news():
    ua = UserAgent()
    headers = {'User-Agent': ua.chrome}
    scheme = 'https://portnews.ru'
    url = 'https://portnews.ru/news/tags/1489'
    result = []
    with requests.Session() as s:
        response = s.get(url, headers=headers)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        if response.status_code == 200:
            news = soup.find_all('table')
            all_date = soup.find_all('p', class_=['date'])
            all_news_datetime = [x.text for x in all_date]  # список со всеми датами новостей
            all_news_hrefs = [scheme + x.find('a')['href'] for x in news]  # все ссылки по новостям
            all_news = [list(a) for a in zip(all_news_hrefs, all_news_datetime)]  # ссылка-дата
            only_new = [x for x in all_news if is_new(x[1])]  # только новые ссылки с датами
            # print(only_new)
            for href in only_new:
                r = requests.get(url=href[0])
                # r.encoding = 'utf-8'
                card_soup = BeautifulSoup(r.text, 'lxml')
                print(card_soup)
                try:
                    news_text_lst = card_soup.find_all('p', attrs={'style': 'text-align: justify'})
                    print(news_text_lst)
                    news_text_row = '\n'.join(news_text_lst)
                    result.append([href[0], news_text_row])
                except Exception:
                    continue
            print(result)
            return result


if __name__ == '__main__':
    get_fts_news()
