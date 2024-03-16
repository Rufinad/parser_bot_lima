from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent



def get_sigma_news():
    """Функция парсит сайт и возвращает список из новостей которые еще не были отправлены"""
    with open('/home/san/Рабочий стол/проекты на Python/parser_bot/services/sent_sigma_hrefs.txt', 'r') as file:
        sent_sigma_hrefs = []
        for line in file:
            sent_sigma_hrefs.append(line.strip())
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
            new_news_hrefs = [i for i in all_news_hrefs if i not in sent_sigma_hrefs]  # только новые новости
            for href in new_news_hrefs:
                r = requests.get(url=href)
                # r.encoding = 'utf-8'
                card_soup = BeautifulSoup(r.text, 'lxml')
                try:
                    news_text = card_soup.find('p', attrs={'style': 'text-align: justify'}).text
                    result.append([href, news_text])
                    sent_sigma_hrefs.extend(new_news_hrefs)
                except Exception:
                    continue
            # print(sent_sigma_hrefs)
            with open('sent_sigma_hrefs.txt', 'a') as file:
                # Записываем каждый элемент списка в файл построчно
                for item in result:  # дозаписываем в файл новости которые отправили
                    file.write(item[0] + '\n')  # Записываем элемент и добавляем символ переноса строки
            # print(result)
            return result  # список списков в котором 0 элемент ссылка, 1 новость


if __name__ == '__main__':
    get_sigma_news()
