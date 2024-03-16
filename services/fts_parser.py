from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, '')  # иначе русские даты не пашут
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


def is_new(date: str):
    """Функция проверяет новость на новизну (сравнивает с текущей датой)"""
    current_date = datetime.now().strftime(' %d %b %Yг')  # cls str
    # current_date = ' 26 Янв 2024г'  # дата приведена для тестирования!!!!!
    form_cur_date = datetime.strptime(current_date, ' %d %b %Yг')  # cls datetime
    news_date = datetime.strptime(date, ' %d %b %Yг')  # cls datetime
    if news_date >= form_cur_date:  # сравнивать можно только объекты datetime
        return True
    return False


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
            all_news_datetime = [x.find('time').text for x in news]
            only_new = [x for x in all_news_datetime if is_new(x)]
            all_news_hrefs = [x.find('a')['href'] for x in news]  # все ссылки по новостям
            all_news_headers = [x.find('h3').text for x in news]  # все заголовки по новостям
            all_news_content = [x.find('p').text for x in news]  # тексты новостей
            all_news = [list(a) for a in zip(all_news_hrefs, all_news_headers, all_news_content, all_news_datetime)]
            result = [x for x in all_news if x[3] in only_new]  # отбираем только новые новости
            # print(result)
            return result




if __name__ == '__main__':
    get_fts_news()
