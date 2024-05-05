import json
import random
from typing import Dict
import requests

url = 'https://lime-shop.com/api/section/dzhinsy_flare_and_bootcut'

payload = ""
headers = {
    "authority": "lime-shop.com",
    "accept": "application/json",
    "accept-language": "ru,en;q=0.9",
    "cache-control": "no-cache",
    "cookie": "l_locale=ru; _ga=GA1.2.1898477944.1714251822; l_region=ru; l-accept-cookies=true; roistat_visit=65274474; roistat_first_visit=65274474; roistat_visit_cookie_expire=1209600; _tt_enable_cookie=1; _ttp=85uLKVbLWNga190rdHSCLu3IA5u; ___dc=c702cd04-4b8a-42f3-b686-f2f9818f64fd; roistat_call_tracking=1; roistat_emailtracking_email=null; roistat_emailtracking_tracking_email=null; roistat_emailtracking_emails=null; l_kind=men; _gid=GA1.2.2115208036.1714370114; roistat_cookies_to_resave=roistat_ab%2Croistat_ab_submit%2Croistat_call_tracking%2Croistat_emailtracking_email%2Croistat_emailtracking_tracking_email%2Croistat_emailtracking_emails; _gat_UA-107774222-1=1",
    "pragma": "no-cache",
    "referer": "https://lime-shop.com/ru_ru",
    "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "YaBrowser";v="24.4", "Yowser";v="2.5"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 YaBrowser/24.4.0.0 Safari/537.36",
    "uuid": "ddd011c9-30c8-4a13-9172-82a44721e7dd",
    "x-frontend-version": "1.5.0",
    "x-lang": "ru",
    "x-requested-with": "XMLHttpRequest",
    "x-site": "ru"
}

response = requests.request("GET", url, data=payload, headers=headers)
json_data = response.text

data = json.loads(json_data)


def decode_unicode(obj):
    if isinstance(obj, dict):
        return {k: decode_unicode(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [decode_unicode(item) for item in obj]
    elif isinstance(obj, str):
        return obj.encode('utf-8').decode('utf-8')
    else:
        return obj


def get_hrefs(data: Dict):
    scheme = 'https://lime-shop.com/ru_ru/product/'
    all_hrefs = []
    for el in data['items']:
        for elem in el['cells']:
            try:
                all_hrefs.append(f"{scheme}{elem['entity']['code']}-{elem['entity']['models'][0]['code']}")
            except KeyError:
                continue
    print(all_hrefs)
    random_hrefs = all_hrefs[random.randint(0, len(all_hrefs)-1)]
    print(random_hrefs)
    return random_hrefs


decoded_data_man = decode_unicode(data)
# print(json.dumps(decoded_data_man, ensure_ascii=False, indent=2))
get_hrefs(decoded_data_man)



'''{
  "id": 142,
  "name": "ЮБКИ МИДИ",
  "code": "skirts_midi",
  "items": [
    {
      "id": 542202,
      "type": 10,
      "cells": [
        {
          "id": 6615302,
          "type": "product",
          "primary_color": 1,
          "entity": {
            "id": 13261,
            "name": "Юбка миди из трикотажа кроше",
            "article": "0237-585",
            "code": "13261_0237_585",
            "description": "Юбка миди из хлопкового трикотажа по технологии вязки кроше. Эластичный тонкий пояс. Фестончатый нижний край.",
            "composition": "100% ХЛОПОК",
            "care": "Ручная стирка. Не отбеливать. Сушка на плоскости после стирки без отжима  . Холодный утюг до 110 °С. Профессиональная сухая чистка в углеводородах, мягкий режим. Не замачивать. Нельзя выкручивать. Стирать вывернутым наизнанку. Стирать отдельно. Гладить изделие вывернутым наизнанку. Рекомендуется гладить с паром",
            "description_text": "Юбка миди из хлопкового трикотажа по технологии вязки кроше. Эластичный тонкий пояс. Фестончатый нижний край.",
            "models": [
              {
                "id": 17662,
                "code": "cernyi",
                "category": "SKIRT",
                "color": {
                  "id": 1,
                  "hex": "000000",
                  "name": "черный"
                },
                "photo": {
                  "id": 182663,
                  "slot": 2,
                  "width": 3374,
                  "height": 2250,
                  "type": 1,
                  "url": "https://cache-limeshop.cdnvideo.ru/limeshop/aa/76804708280d750d7e13549ab9e9564d261f5be27.jpg"
                },
                "name": "Юбка миди из трикотажа кроше",
                "product": {
                  "code": "13261_0237_585",
                  "name": "Юбка миди из трикотажа кроше"
                },
                "skus": [
                  {
                    "id": 49583,
                    "size": {
                      "id": 2,
                      "unit": "INT",
                      "value": "S"
                    },
                    "stock": {
                      "online": 46,
                      "offline": 199
                    },
                    "price": 5999,
                    "price_formatted": "5999 руб.",
                    "old_price": null,
                    "old_price_formatted": "0 руб."
                  }
                ],
                "medias": [
                  {
                    "id": 182663,
                    "slot": 2,
                    "width": 3374,
                    "height": 2250,
                    "type": 1,
                    "url": "https://cache-limeshop.cdnvideo.ru/limeshop/aa/76804708280d750d7e13549ab9e9564d261f5be27.jpg"
                  }
                ],
                "badge": []
              }
            ]
          },
          "slot": 1
        }
      ]
    },
    {
      "id": 542203,
      "type": 33,
      "cells": [
        {
          "id": 6615303,
          "type": "product",
          "primary_color": 1,
          "entity": {
            "id": 13261,
            "name": "Юбка миди из трикотажа кроше",
            "article": "0237-585",
            "code": "13261_0237_585",
            "description": "Юбка миди из хлопкового трикотажа по технологии вязки кроше. Эластичный тонкий пояс. Фестончатый нижний край.",
            "composition": "100% ХЛОПОК",
            "care": "Ручная стирка. Не отбеливать. Сушка на плоскости после стирки без отжима  . Холодный утюг до 110 °С. Профессиональная сухая чистка в углеводородах, мягкий режим. Не замачивать. Нельзя выкручивать. Стирать вывернутым наизнанку. Стирать отдельно. Гладить изделие вывернутым наизнанку. Рекомендуется гладить с паром",
            "description_text": "Юбка миди из хлопкового трикотажа по технологии вязки кроше. Эластичный тонкий пояс. Фестончатый нижний край.",
            "models": [
              {
                "id": 17488,
                "code": "molocnyi",
                "category": "SKIRT",
                "color": {
                  "id": 8,
                  "hex": "FFFFF0",
                  "name": "молочный"
                },
                "photo": {
                  "id": 182659,
                  "slot": 2,
                  "width": 1500,
                  "height": 2250,
                  "type": 1,
                  "url": "https://cache-limeshop.cdnvideo.ru/limeshop/aa/768047056c1d652815ca848ea9e36d8a135f6fdfc.jpg"
                },
                "name": "Юбка миди из трикотажа кроше",
                "product": {
                  "code": "13261_0237_585",
                  "name": "Юбка миди из трикотажа кроше"
                },
                "skus": [
                  {
                    "id": 48706,
                    "size": {
                      "id": 2,
                      "unit": "INT",
                      "value": "S"
                    },
                    "stock": {
                      "online": 7,
                      "offline": 193
                    },
                    "price": 5999,
                    "price_formatted": "5999 руб.",
                    "old_price": null,
                    "old_price_formatted": "0 руб."
                  }
                ],
                "medias": [
                  {
                    "id": 182659,
                    "slot": 2,
                    "width": 1500,
                    "height": 2250,
                    "type": 1,
                    "url": "https://cache-limeshop.cdnvideo.ru/limeshop/aa/768047056c1d652815ca848ea9e36d8a135f6fdfc.jpg"
                  }
                ],
                "badge": []
              }
            ]
          },
          "slot": 1
        }
      ]
    },
    {
      "id": 522409,
      "type": 8,
      "cells": [
        {
          "id": 6624276,
          "type": "product",
          "primary_color": 1,
          "entity": {
            "id": 18284,
            "name": "Юбка миди с драпировкой",
            "article": "5973-049",
            "code": "18284_5973_049",
            "description": "Юбка миди из смесового льна с высоким разрезом. Декоративный узел на поясе создает драпировку с естественными складками на поясе. Застежка на молнию.",
            "composition": null,
            "care": "Машинная стирка 30 °С; очень мягкий режим . Не отбеливать. Сушка в машине запрещена. Холодный утюг до 110 °С. Профессиональная сухая чистка в углеводородах, мягкий режим. Не замачивать. Нельзя выкручивать. Стирать с вещами такой же окраски. Гладить со специальной насадкой на подошве утюга. Рекомендуется гладить с паром",
            "description_text": "Юбка миди из смесового льна с высоким разрезом. Декоративный узел на поясе создает драпировку с естественными складками на поясе. Застежка на молнию.",
            "models": [
              {
                "id": 24324,
                "code": "cernyi",
                "category": "SKIRT",
                "color": {
                  "id": 1,
                  "hex": "000000",
                  "name": "черный"
                },
                "photo": {
                  "id": 180092,
                  "slot": 1,
                  "width": 1500,
                  "height": 2249,
                  "type": 1,
                  "url": "https://cache-limeshop.cdnvideo.ru/limeshop/aa/76670576029b76d3818eb4ed9a78b30dc37194a0c.jpg"
                },
                "name": "Юбка миди с драпировкой",
                "product": {
                  "code": "18284_5973_049",
                  "name": "Юбка миди с драпировкой"
                },
                "skus": [
                  {
                    "id": 82013,
                    "size": {
                      "id": 3,
                      "unit": "INT",
                      "value": "M"
                    },
                    "stock": {
                      "online": 9,
                      "offline": 17
                    },
                    "price": 5999,
                    "price_formatted": "5999 руб.",
                    "old_price": null,
                    "old_price_formatted": "0 руб."
                  }
                ],
                "medias": [
                  {
                    "id": 180092,
                    "slot": 1,
                    "width": 1500,
                    "height": 2249,
                    "type": 1,
                    "url": "https://cache-limeshop.cdnvideo.ru/limeshop/aa/76670576029b76d3818eb4ed9a78b30dc37194a0c.jpg"
                  }
                ],
                "badge": []
              }
            ]
          },
          "slot": 1
        }
      ]
    },
    {
      "id": 529039,
      "type": 11,
      "cells": [
        {
          "id": 6582305,
          "type": "product",
          "primary_color": 1,
          "entity": {
            "id": 18315,
            "name": "Атласная юбка с цветочным узором",
            "article": "4642-239",
            "code": "18315_4642_239",
            "description": "Юбка миди из вискозного атласа  с цветочным узором из пайеток и бисера. Контрастная оборка из жатой ткани по низу. На подкладке. Застежка на потайную молнию сбоку.",
            "composition": null,
            "care": "Не стирать. Не отбеливать. Сушка в машине запрещена. Холодный утюг до 110 °С. Профессиональная сухая чистка в углеводородах, мягкий режим. Не гладить отделку. Гладить изделие вывернутым наизнанку. Рекомендуется гладить с паром",
            "description_text": "Юбка миди из вискозного атласа  с цветочным узором из пайеток и бисера. Контрастная оборка из жатой ткани по низу. На подкладке. Застежка на потайную молнию сбоку.",
            "models": [
              {
                "id": 24367,
                "code": "seryi",
                "category": "SKIRT",
                "color": {
                  "id": 35,
                  "hex": "808080",
                  "name": "серый"
                },
                "photo": {
                  "id": 180397,
                  "slot": 1,
                  "width": 1500,
                  "height": 2250,
                  "type": 1,
                  "url": "https://cache-limeshop.cdnvideo.ru/limeshop/aa/7647831490d89024eed6c41bab08ba7da9690c657.jpg"
                },
                "name": "Атласная юбка с цветочным узором",
                "product": {
                  "code": "18315_4642_239",
                  "name": "Атласная юбка с цветочным узором"
                },
                "skus": [
                  {
                    "id": 82209,
                    "size": {
                      "id": 1,
                      "unit": "INT",
                      "value": "XS"
                    },
                    "stock": {
                      "online": 41,
                      "offline": 13
                    },
                    "price": 7999,
                    "price_formatted": "7999 руб.",
                    "old_price": null,
                    "old_price_formatted": "0 руб."
                  }
                ],
                "medias": [
                  {
                    "id": 180397,
                    "slot": 1,
                    "width": 1500,
                    "height": 2250,
                    "type": 1,
                    "url": "https://cache-limeshop.cdnvideo.ru/limeshop/aa/7647831490d89024eed6c41bab08ba7da9690c657.jpg"
                  }
                ],
                "badge": [
                  {
                    "value": "STUDIO",
                    "type": 5
                  }
                ]
              }
            ]
          },
          "slot": 1
        },
        {
          "id": 6643143,
          "type": "product",
          "primary_color": 1,
          "entity": {
            "id": 18315,
            "name": "Атласная юбка с цветочным узором",
            "article": "4642-239",
            "code": "18315_4642_239",
            "description": "Юбка миди из вискозного атласа  с цветочным узором из пайеток и бисера. Контрастная оборка из жатой ткани по низу. На подкладке. Застежка на потайную молнию сбоку.",
            "composition": null,
            "care": "Не стирать. Не отбеливать. Сушка в машине запрещена. Холодный утюг до 110 °С. Профессиональная сухая чистка в углеводородах, мягкий режим. Не гладить отделку. Гладить изделие вывернутым наизнанку. Рекомендуется гладить с паром",
            "description_text": "Юбка миди из вискозного атласа  с цветочным узором из пайеток и бисера. Контрастная оборка из жатой ткани по низу. На подкладке. Застежка на потайную молнию сбоку.",
            "models": [
              {
                "id": 24367,
                "code": "seryi",
                "category": "SKIRT",
                "color": {
                  "id": 35,
                  "hex": "808080",
                  "name": "серый"
                },
                "photo": {
                  "id": 181160,
                  "slot": 2,
                  "width": 1500,
                  "height": 2250,
                  "type": 1,
                  "url": "https://cache-limeshop.cdnvideo.ru/limeshop/aa/7647752562fb81a2d1711485cbf97fa5581337ca9.jpg"
                },
                "name": "Атласная юбка с цветочным узором",
                "product": {
                  "code": "18315_4642_239",
                  "name": "Атласная юбка с цветочным узором"
                },
                "skus": [
                  {
                    "id": 82209,
                    "size": {
                      "id": 1,
                      "unit": "INT",
                      "value": "XS"
                    },
                    "stock": {
                      "online": 41,
                      "offline": 13
                    },
                    "price": 7999,
                    "price_formatted": "7999 руб.",
                    "old_price": null,
                    "old_price_formatted": "0 руб."
                  }
                ],
                "medias": [
                  {
                    "id": 181160,
                    "slot": 2,
                    "width": 1500,
                    "height": 2250,
                    "type": 1,
                    "url": "https://cache-limeshop.cdnvideo.ru/limeshop/aa/7647752562fb81a2d1711485cbf97fa5581337ca9.jpg"
                  }
                ],
                "badge": [
                  {
                    "value": "STUDIO",
                    "type": 5
                  }
                ]
              }
            ]
          },
          "slot": 2
        }
      ]
    }
  ],
  "meta": {
    "page": 1,
    "items": 4,
    "total": 7
  },
  "http_meta": {
    "title": "Купить юбки миди в интернет-магазине LIME с доставкой по Москве и Санкт-Петербургу | Каталог с ценами",
    "description": "Интернет-магазин LIME предлагает купить женские юбки миди по выгодным ценам. Оперативная обработка заказов",
    "keywords": "lime, одежда, фирмы, марка, женская, компании, российская, брендовая, каталог, самара, коллекция, купить, интернет, магазин, модной, москва, стильную, заказать, продажа, цены, россия, недорогой, сеть, заказ, заказать, качественную, розницу, покупка, вещей, товар",
    "og:title": "Купить юбки миди в интернет-магазине LIME с доставкой по Москве и Санкт-Петербургу | Каталог с ценами",
    "og:description": "Интернет-магазин LIME предлагает купить женские юбки миди по выгодным ценам. Оперативная обработка заказов",
    "theme-font_color": "#000000",
    "theme-color": "#FFFFFF"
  }
}'''