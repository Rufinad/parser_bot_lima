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


date = '18 мартa 2024 09:45'

print(is_new(date))