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



lst = [['https://portnews.ru/news/361692/', '8 апреля 2024'], ['https://portnews.ru/news/361548/', '4 апреля 2024'], ['https://portnews.ru/news/361469/', '2 апреля 2024'], ['https://portnews.ru/news/361416/', '1 апреля 2024'], ['https://portnews.ru/news/361365/', '31 марта 2024'], ['https://portnews.ru/news/361328/', '29 марта 2024'], ['https://portnews.ru/news/361283/', '28 марта 2024'], ['https://portnews.ru/news/361224/', '27 марта 2024'], ['https://portnews.ru/news/361162/', '26 марта 2024'], ['https://portnews.ru/news/361000/', '21 марта 2024'], ['https://portnews.ru/news/360952/', '20 марта 2024'], ['https://portnews.ru/news/360907/', '19 марта 2024'], ['https://portnews.ru/news/360833/', '18 марта 2024'], ['https://portnews.ru/news/360744/', '15 марта 2024'], ['https://portnews.ru/news/360704/', '14 марта 2024'], ['https://portnews.ru/news/360530/', '8 марта 2024'], ['https://portnews.ru/news/360462/', '6 марта 2024'], ['https://portnews.ru/news/360397/', '5 марта 2024'], ['https://portnews.ru/news/360332/', '4 марта 2024'], ['https://portnews.ru/news/360315/', '2 марта 2024'], ['https://portnews.ru/news/360305/', '1 марта 2024'], ['https://portnews.ru/news/360207/', '29 февраля 2024'], ['https://portnews.ru/news/360181/', '28 февраля 2024'], ['https://portnews.ru/news/360131/', '27 февраля 2024'], ['https://portnews.ru/news/360038/', '26 февраля 2024'], ['https://portnews.ru/news/359998/', '22 февраля 2024'], ['https://portnews.ru/news/359932/', '21 февраля 2024'], ['https://portnews.ru/news/359874/', '20 февраля 2024'], ['https://portnews.ru/news/359697/', '15 февраля 2024'], ['https://portnews.ru/news/359566/', '13 февраля 2024'], ['https://portnews.ru/news/359545/', '12 февраля 2024'], ['https://portnews.ru/news/359488/', '10 февраля 2024'], ['https://portnews.ru/news/359469/', '9 февраля 2024'], ['https://portnews.ru/news/359381/', '7 февраля 2024'], ['https://portnews.ru/news/359325/', '6 февраля 2024'], ['https://portnews.ru/news/359256/', '5 февраля 2024'], ['https://portnews.ru/news/359156/', '2 февраля 2024'], ['https://portnews.ru/news/359127/', '1 февраля 2024'], ['https://portnews.ru/news/359071/', '31 января 2024'], ['https://portnews.ru/news/359054/', '30 января 2024'], ['https://portnews.ru/news/358990/', '29 января 2024']]

only_new = [x for x in lst if is_new(x[1])]
print(only_new)
