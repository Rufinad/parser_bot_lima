from datetime import datetime
import locale
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

locale.setlocale(locale.LC_ALL, '')  # иначе русские даты не пашут


def is_new(date: str):
    """Функция проверяет новость на новизну (сравнивает с текущей датой)"""
    # current_date = datetime.now().strftime(' %d %b %Y')  # cls str
    current_date = '15 марта 2024'  # дата приведена для тестирования!!!!!
    form_cur_date = datetime.strptime(current_date, '%d %B %Y')  # cls datetime
    formatted_date = date.replace('a', 'а')  # ебаная таможня использует английские буквы в русских словах
    news_date = datetime.strptime(formatted_date, '%d %B %Y %H:%M')  # cls datetime
    if news_date >= form_cur_date:  # сравнивать можно только объекты datetime
        return True
    return False


def get_custom_news():
    ua = UserAgent()
    headers = {'User-Agent': ua.chrome}
    url = 'https://customs.gov.ru/press/federal'
    result = []
    with requests.Session() as s:
        response = s.get(url, headers=headers)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        if response.status_code == 200:
            all_news = soup.find_all('div', class_=['list-news__item'])
            all_news_datetime = [x.find('div', class_='list-news__item-data').text.strip() for x in all_news]
            all_news_hrefs = [x.find('a')['href'] for x in all_news]  # все ссылки на новости
            all_news = [list(a) for a in zip(all_news_hrefs, all_news_datetime)]  # ссылка-дата
            only_new = [x for x in all_news if is_new(x[1])]  # только новые ссылки с датами
            # print(only_new)
            for href in only_new:
                r = requests.get(url=href[0])
                # r.encoding = 'utf-8'
                card_soup = BeautifulSoup(r.text, 'lxml')
                print(card_soup)
                news_text = card_soup.find('div', class_='pin')
                # print(news_text)
                # # Разбиваем текст на строки
                # lines = news_text.split('\n')
                # # Удаляем первые 3 строки
                # new_text = '\n'.join(lines[3:])
                # result.append([href[0], news_text])
            print(result)
            return result


if __name__ == '__main__':
    get_custom_news()
