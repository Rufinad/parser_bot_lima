from typing import Dict
import random


def get_hrefs(data: Dict):
    scheme = 'https://lime-shop.com/ru_ru/product/'
    all_hrefs = []
    for el in data['items']:
        for elem in el['cells']:
            try:
                all_hrefs.append(f"{scheme}{elem['entity']['code']}-{elem['entity']['models'][0]['code']}")
            except KeyError:
                continue
    # print(all_hrefs)
    random_hrefs = all_hrefs[random.randint(0, len(all_hrefs) - 1)]
    # print(random_hrefs)
    return random_hrefs
