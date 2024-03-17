from datetime import datetime
import locale
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

locale.setlocale(locale.LC_ALL, '')  # иначе русские даты не пашут


def is_new(date: str):
    """Функция проверяет новость на новизну (сравнивает с текущей датой)"""
    # current_date = datetime.now().strftime(' %d %b %Y')  # cls str
    current_date = ' 15 марта 2024'  # дата приведена для тестирования!!!!!
    form_cur_date = datetime.strptime(current_date, ' %d %B %Y')  # cls datetime
    news_date = datetime.strptime(date, '%d %B %Y')  # cls datetime
    if news_date >= form_cur_date:  # сравнивать можно только объекты datetime
        return True
    return False

lst = ['15 марта 2024', '14 марта 2024']

res = [x for x in lst if is_new(x)]

print(res)

# from datetime import datetime
#
# # Преобразование строки '26 января 2024' в объект datetime
# date_str = '26 января 2024'
# date = datetime.strptime(date_str, '%d %B %Y')
#
# # Получение текущей даты
# current_date = datetime.now()
#
# # Сравнение дат
# if date > current_date:
#     print('Дата "26 января 2024" позже текущей даты.')
# elif date < current_date:
#     print('Дата "26 января 2024" раньше текущей даты.')
# else:
#     print('Дата "26 января 2024" совпадает с текущей датой.')
#
