from datetime import datetime
import locale
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

locale.setlocale(locale.LC_ALL, '')  # иначе русские даты не пашут


def is_new(date: str):
    """Функция проверяет новость на новизну (сравнивает с текущей датой)"""
    # current_date = datetime.now().strftime(' %d %b %Yг')  # cls str
    current_date = ' 26 Янв 2024г'  # дата приведена для тестирования!!!!!
    form_cur_date = datetime.strptime(current_date, ' %d %b %Yг')  # cls datetime
    news_date = datetime.strptime(date, ' %d %b %Yг')  # cls datetime
    if news_date >= form_cur_date:  # сравнивать можно только объекты datetime
        return True
    return False


def get_fts_news():
    ua = UserAgent()
    headers = {'User-Agent': ua.chrome}
    url = 'https://ved.today/category/novosti-tamozhni'
    result = []
    with requests.Session() as s:
        response = s.get(url, headers=headers)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        if response.status_code == 200:
            news = soup.find_all('div', class_=['biglast_item item'])
            all_news_datetime = [x.find('time').text for x in news]
            all_news_hrefs = [x.find('a')['href'] for x in news]  # все ссылки по новостям
            all_news = [list(a) for a in zip(all_news_hrefs, all_news_datetime)]  # ссылка-дата
            only_new = [x for x in all_news if is_new(x[1])]  # только новые ссылки с датами
            for href in only_new:
                r = requests.get(url=href[0])
                # r.encoding = 'utf-8'
                card_soup = BeautifulSoup(r.text, 'lxml')
                try:
                    news_text = card_soup.find('div', class_='content_text').text
                    # Разбиваем текст на строки
                    lines = news_text.split('\n')
                    # Удаляем первые 3 строки
                    new_text = '\n'.join(lines[3:])
                    result.append([href[0], new_text])
                except Exception:
                    continue
            # print(result)
            return result


if __name__ == '__main__':
    get_fts_news()
