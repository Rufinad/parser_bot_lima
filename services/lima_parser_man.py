import json

import requests

url = "https://lime-shop.com/api/menu/left_men"

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


decoded_data_man = decode_unicode(data)

print(json.dumps(decoded_data_man, ensure_ascii=False, indent=2))

'''
"/home/san/Рабочий стол/freelance/parser_bot_lima/venv/bin/python" /home/san/Рабочий стол/freelance/parser_bot_lima/services/lima_parser_man.py 
{
  "items": [
    {
      "id": 2566,
      "name": "НОВИНКИ",
      "url": "/catalog/men_new",
      "marker": "delimiter",
      "theme": {
        "color": null,
        "background": null
      },
      "items": []
    },
    {
      "id": 4078,
      "name": "LA SIESTA",
      "url": "https://lime-shop.com/ru_ru/lp/man-summer-24/",
      "marker": "static",
      "theme": {
        "color": null,
        "background": null
      },
      "items": []
    },
    {
      "id": 4034,
      "name": "OFFICE СORE",
      "url": "/catalog/men_office_core",
      "marker": "delimiter",
      "theme": {
        "color": null,
        "background": null
      },
      "items": []
    },
    {
      "id": 4100,
      "name": "ПРОМО",
      "url": "/catalog/sale_men",
      "marker": "highlight new",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 4101,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/sale_men",
          "marker": "highlight",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4102,
          "name": "ВЕРХНЯЯ ОДЕЖДА",
          "url": "/catalog/sale_men_outwear",
          "marker": "highlight",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4103,
          "name": "СВИТЕРЫ | ТОЛСТОВКИ",
          "url": "/catalog/sale_men_knitwear",
          "marker": "highlight",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4104,
          "name": "БРЮКИ | ДЖИНСЫ",
          "url": "/catalog/sale_men_trousers",
          "marker": "highlight",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4105,
          "name": "ФУТБОЛКИ | ПОЛО",
          "url": "/catalog/sale_men_t_shirts",
          "marker": "highlight",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4106,
          "name": "РУБАШКИ",
          "url": "/catalog/sale_men_shirts",
          "marker": "highlight",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        }
      ]
    },
    {
      "id": 4026,
      "name": "ЛЕН",
      "url": "/catalog/men_linen",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": []
    },
    {
      "id": 3859,
      "name": "ХИТЫ ПРОДАЖ",
      "url": "/catalog/men_bestsellers",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": []
    },
    {
      "id": 2960,
      "name": "БЛЕЙЗЕРЫ",
      "url": "/catalog/men_blazers",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": []
    },
    {
      "id": 2572,
      "name": "БРЮКИ",
      "url": "/catalog/men_trousers",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 3005,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/men_trousers",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3008,
          "name": "КЛАССИЧЕСКИЕ",
          "url": "/catalog/men_trousers_classic",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3006,
          "name": "ДЖОГГЕРЫ",
          "url": "/catalog/men_trousers_joggers",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3153,
          "name": "КАРГО | ПАРАШЮТЫ",
          "url": "/catalog/men_trousers_cargo",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3007,
          "name": "ЧИНОС",
          "url": "/catalog/men_trousers_chino",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4084,
          "name": "СВОБОДНЫЙ КРОЙ",
          "url": "/catalog/men_trousers_loose_fitting",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4096,
          "name": "ЛЬНЯНЫЕ",
          "url": "/catalog/men_trousers_linen",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        }
      ]
    },
    {
      "id": 2956,
      "name": "РУБАШКИ",
      "url": "/catalog/men_shirts",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 3659,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/men_shirts",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3661,
          "name": "ОДНОТОННЫЕ",
          "url": "/catalog/men_shirts_plain",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3662,
          "name": "С ПРИНТОМ",
          "url": "/catalog/men_shirts_printed",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3660,
          "name": "ФОРМАЛЬНЫЕ",
          "url": "/catalog/men_shirts_formal",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3863,
          "name": "ДЖИНСОВЫЕ",
          "url": "/catalog/men_shirts_denim",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4083,
          "name": "КОРОТКИЙ РУКАВ",
          "url": "/catalog/men_shirts_short_sleeve",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4004,
          "name": "ЛЬНЯНЫЕ",
          "url": "/catalog/men_shirts_linen",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        }
      ]
    },
    {
      "id": 1,
      "name": "КЛАССИЧЕСКИЕ КОСТЮМЫ",
      "url": "/catalog/men_suits_classic",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": []
    },
    {
      "id": 4089,
      "name": "ПРЕМИАЛЬНЫЙ ХЛОПОК",
      "url": "/catalog/men_t_shirts_premium_cotton",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": []
    },
    {
      "id": 3723,
      "name": "ВЕРХНЯЯ ОДЕЖДА",
      "url": "/catalog/men_outerwear",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 3726,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/men_outerwear",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3725,
          "name": "ПАЛЬТО | ТРЕНЧИ",
          "url": "/catalog/men_coats",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2573,
          "name": "КУРТКИ",
          "url": "/catalog/men_jackets",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3724,
          "name": "БОМБЕРЫ",
          "url": "/catalog/men_jackets_bombers",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3775,
          "name": "КУРТКИ-РУБАШКИ",
          "url": "/catalog/men_overshirt",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3862,
          "name": "ДЕНИМ",
          "url": "/catalog/men_jackets_denim",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3815,
          "name": "ЖИЛЕТЫ",
          "url": "/catalog/men_gilets",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        }
      ]
    },
    {
      "id": 2568,
      "name": "ФУТБОЛКИ",
      "url": "/catalog/men_t_shirts",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 3083,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/men_t_shirts",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3084,
          "name": "БАЗОВЫЕ",
          "url": "/catalog/men_t_shirts_basics",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3996,
          "name": "С ПРИНТОМ",
          "url": "/catalog/men_t_shirts_printed",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3278,
          "name": "КОРОТКИЙ РУКАВ",
          "url": "/catalog/men_t_shirts_short_sleeve",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3279,
          "name": "ЛОНГСЛИВЫ",
          "url": "/catalog/men_t_shirts_long_sleeve",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4088,
          "name": "ПРЕМИАЛЬНЫЙ ХЛОПОК",
          "url": "/catalog/men_t_shirts_premium_cotton",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        }
      ]
    },
    {
      "id": 3869,
      "name": "ШОРТЫ",
      "url": "/catalog/men_shorts",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 4097,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/men_shorts",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4098,
          "name": "ДЖИНСОВЫЕ",
          "url": "/catalog/men_shorts_denim",
          "marker": "new",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        }
      ]
    },
    {
      "id": 3076,
      "name": "СВИТЕРЫ | КАРДИГАНЫ",
      "url": "/catalog/men_knitwear",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 3652,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/men_knitwear",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3653,
          "name": "СВИТЕРЫ",
          "url": "/catalog/men_sweaters",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3654,
          "name": "КАРДИГАНЫ",
          "url": "/catalog/men_cardigans",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3668,
          "name": "ПОЛО",
          "url": "/catalog/men_knit_polo",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3816,
          "name": "КОРОТКИЙ РУКАВ",
          "url": "/catalog/men_sweaters_short_sleeve",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        }
      ]
    },
    {
      "id": 2569,
      "name": "ДЖИНСЫ",
      "url": "/catalog/men_jeans",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 3012,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/men_jeans",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3014,
          "name": "ШИРОКИЕ",
          "url": "/catalog/men_jeans_loose",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3667,
          "name": "ПРЯМЫЕ",
          "url": "/catalog/men_jeans_straight",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3739,
          "name": "КАРГО",
          "url": "/catalog/men_jeans_cargo",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3015,
          "name": "SLIM | TAPERED",
          "url": "/catalog/men_jeans_slim",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        }
      ]
    },
    {
      "id": 3672,
      "name": "КОМПЛЕКТЫ",
      "url": "/catalog/men_co_ord_sets",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": []
    },
    {
      "id": 4082,
      "name": "КУРТКИ-РУБАШКИ",
      "url": "/catalog/men_overshirt",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": []
    },
    {
      "id": 2570,
      "name": "ПОЛО",
      "url": "/catalog/men_polo",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 3655,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/men_polo",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3657,
          "name": "КОРОТКИЙ РУКАВ",
          "url": "/catalog/men_polo_short_sleeve",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3656,
          "name": "ДЛИННЫЙ РУКАВ",
          "url": "/catalog/men_polo_long_sleeve",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        }
      ]
    },
    {
      "id": 2567,
      "name": "ТОЛСТОВКИ",
      "url": "/catalog/men_sweatshirts",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 3663,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/men_sweatshirts",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3664,
          "name": "БАЗОВЫЕ",
          "url": "/catalog/men_swetshirts_basics",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3665,
          "name": "С ПРИНТОМ",
          "url": "/catalog/men_sweatshirts_printed",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3666,
          "name": "ХУДИ",
          "url": "/catalog/men_sweatshirts_hoodies",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3785,
          "name": "ZIP-TOP",
          "url": "/catalog/men_sweatshirts_zip_top",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        }
      ]
    },
    {
      "id": 2574,
      "name": "СПОРТИВНЫЕ КОМПЛЕКТЫ",
      "url": "/catalog/men_sportswear",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": []
    },
    {
      "id": 2575,
      "name": "ОБУВЬ",
      "url": "/catalog/men_all_shoes",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 3719,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/men_all_shoes",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3722,
          "name": "КЕДЫ | КРОССОВКИ",
          "url": "/catalog/men_shoes_sneakers",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3721,
          "name": "ЛОФЕРЫ",
          "url": "/catalog/men_lofers",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4006,
          "name": "САБО | САНДАЛИИ",
          "url": "/catalog/men_sandals",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3720,
          "name": "БОТИНКИ",
          "url": "/catalog/men_shoes_boots",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        }
      ]
    },
    {
      "id": 3036,
      "name": "АКСЕССУАРЫ",
      "url": "/catalog/men_accessories",
      "marker": "delimiter",
      "theme": {
        "color": null,
        "background": null
      },
      "items": []
    },
    {
      "id": 3765,
      "name": "EDITORIAL",
      "url": "/catalog/men_all",
      "marker": "delimiter",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 3676,
          "name": "DAY AT HOME",
          "url": "https://lime-shop.com/ru_ru/lp/man-spring24/",
          "marker": "static",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        }
      ]
    },
    {
      "id": 3843,
      "name": "ПОДАРОЧНАЯ КАРТА",
      "url": "https://lime-shop.com/ru_ru#gift",
      "marker": "static",
      "theme": {
        "color": null,
        "background": null
      },
      "items": []
    }
  ]
}

Process finished with exit code 0
'''