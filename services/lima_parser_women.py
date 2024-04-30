import json

import requests

url = "https://lime-shop.com/api/menu/left_women"

payload = ""
headers = {
    "authority": "lime-shop.com",
    "accept": "application/json",
    "accept-language": "ru,en;q=0.9",
    "cache-control": "no-cache",
    "cookie": "l_locale=ru; _ga=GA1.2.1898477944.1714251822; l_region=ru; l-accept-cookies=true; roistat_visit=65274474; roistat_first_visit=65274474; roistat_visit_cookie_expire=1209600; _tt_enable_cookie=1; _ttp=85uLKVbLWNga190rdHSCLu3IA5u; ___dc=c702cd04-4b8a-42f3-b686-f2f9818f64fd; roistat_call_tracking=1; roistat_emailtracking_email=null; roistat_emailtracking_tracking_email=null; roistat_emailtracking_emails=null; l_kind=men; _gid=GA1.2.2115208036.1714370114; roistat_cookies_to_resave=roistat_ab%2Croistat_ab_submit%2Croistat_call_tracking%2Croistat_emailtracking_email%2Croistat_emailtracking_tracking_email%2Croistat_emailtracking_emails; _gat_UA-107774222-1=1",
    "pragma": "no-cache",
    "referer": "https://lime-shop.com/catalog/men_linen",
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


decoded_data_women = decode_unicode(data)

print(json.dumps(decoded_data_women, ensure_ascii=False, indent=2))


'''
"/home/san/Рабочий стол/freelance/parser_bot_lima/venv/bin/python" /home/san/Рабочий стол/freelance/parser_bot_lima/services/lima_parser_women.py 
{
  "items": [
    {
      "id": 2151,
      "name": "НОВИНКИ",
      "url": "/catalog/new",
      "marker": "delimiter",
      "theme": {
        "color": null,
        "background": null
      },
      "items": []
    },
    {
      "id": 4092,
      "name": "THE CRUISE",
      "url": "https://lime-shop.com/ru_ru/lp/woman-summer-24-basic/",
      "marker": "static new",
      "theme": {
        "color": null,
        "background": null
      },
      "items": []
    },
    {
      "id": 4076,
      "name": "SUMMER TOUCH",
      "url": "https://lime-shop.com/ru_ru/lp/woman-summer-24-studio/",
      "marker": "delimiter static",
      "theme": {
        "color": null,
        "background": null
      },
      "items": []
    },
    {
      "id": 4058,
      "name": "ЛЕН",
      "url": "/catalog/linen",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 4059,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/linen",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4060,
          "name": "БЛЕЙЗЕРЫ | ЖИЛЕТЫ",
          "url": "/catalog/blazers_linen",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4061,
          "name": "БРЮКИ",
          "url": "/catalog/trousers_linen",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4062,
          "name": "КОСТЮМЫ",
          "url": "/catalog/suits_linen",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4063,
          "name": "ПЛАТЬЯ",
          "url": "/catalog/dresses_linen",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4064,
          "name": "РУБАШКИ",
          "url": "/catalog/shirts_linen",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4065,
          "name": "ЮБКИ",
          "url": "/catalog/skirts_linen",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4066,
          "name": "ТОПЫ",
          "url": "/catalog/tops_linen",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4067,
          "name": "ШОРТЫ",
          "url": "/catalog/shorts_linen",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4068,
          "name": "КОМПЛЕКТЫ",
          "url": "/catalog/linen_co_ord_sets",
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
      "id": 3827,
      "name": "КОЛЛЕКЦИЯ STUDIO",
      "url": "/catalog/studio",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 3839,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/studio",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3828,
          "name": "БЛЕЙЗЕРЫ | ЖИЛЕТЫ",
          "url": "/catalog/studio_blazers",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3829,
          "name": "БРЮКИ",
          "url": "/catalog/studio_trousers",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4054,
          "name": "КОСТЮМЫ",
          "url": "/catalog/studio_suits",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3830,
          "name": "ПЛАТЬЯ | КОМБИНЕЗОНЫ",
          "url": "/catalog/studio_dresses",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3831,
          "name": "ВЕРХНЯЯ ОДЕЖДА",
          "url": "/catalog/studio_outerwear",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3832,
          "name": "СВИТЕРЫ | КАРДИГАНЫ",
          "url": "/catalog/studio_kniwear",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3833,
          "name": "РУБАШКИ | БЛУЗЫ",
          "url": "/catalog/studio_shirts",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3834,
          "name": "ДЖИНСЫ",
          "url": "/catalog/studio_jeans",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3835,
          "name": "ТОПЫ | БОДИ",
          "url": "/catalog/studio_tops",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3836,
          "name": "ФУТБОЛКИ | ТОЛСТОВКИ",
          "url": "/catalog/studio_t_shirts",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3837,
          "name": "ЮБКИ",
          "url": "/catalog/studio_skirts",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3838,
          "name": "ШОРТЫ",
          "url": "/catalog/studio_shorts",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3840,
          "name": "СУМКИ | АКСЕССУАРЫ",
          "url": "/catalog/studio_accessories",
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
      "id": 3800,
      "name": "ВЕРХНЯЯ ОДЕЖДА",
      "url": "/catalog/outerwear",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 3802,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/outerwear",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2125,
          "name": "КУРТКИ",
          "url": "/catalog/kurtki",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3684,
          "name": "ИСКУССТВЕННАЯ КОЖА",
          "url": "/catalog/faux_leather_jacket",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4018,
          "name": "КОЖА",
          "url": "/catalog/jacket_leather",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3801,
          "name": "ДЖИНСОВЫЕ",
          "url": "/catalog/jackets_denim",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3685,
          "name": "БОМБЕРЫ",
          "url": "/catalog/jackets_bomber",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3325,
          "name": "ТРЕНЧИ",
          "url": "/catalog/trench_coats",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3324,
          "name": "ПАЛЬТО",
          "url": "/catalog/coats",
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
      "id": 2114,
      "name": "ПЛАТЬЯ | КОМБИНЕЗОНЫ",
      "url": "/catalog/dresses",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 3599,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/dresses",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3600,
          "name": "МИДИ",
          "url": "/catalog/dresses_midi",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3601,
          "name": "МАКСИ",
          "url": "/catalog/dresses_maxi",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3602,
          "name": "МИНИ",
          "url": "/catalog/dresses_mini",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4037,
          "name": "ЛЬНЯНЫЕ",
          "url": "/catalog/dresses_linen",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3603,
          "name": "ТРИКОТАЖНЫЕ",
          "url": "/catalog/dresses_knitwear",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3718,
          "name": "КОМБИНЕЗОНЫ",
          "url": "/catalog/jumpsuits",
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
      "id": 2120,
      "name": "РУБАШКИ | БЛУЗЫ",
      "url": "/catalog/shirts_all",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 2121,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/shirts_all",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3604,
          "name": "РУБАШКИ",
          "url": "/catalog/shirts",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3605,
          "name": "БЛУЗЫ",
          "url": "/catalog/blouses",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3534,
          "name": "БАЗОВЫЕ",
          "url": "/catalog/shirts_basics",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3306,
          "name": "С ПРИНТОМ",
          "url": "/catalog/shirts_printed",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4038,
          "name": "ЛЬНЯНЫЕ",
          "url": "/catalog/shirts_linen",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3671,
          "name": "ДЖИНСОВЫЕ",
          "url": "/catalog/shirts_denim",
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
      "id": 2100,
      "name": "ЮБКИ",
      "url": "/catalog/skirts",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 2101,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/skirts",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2103,
          "name": "МИДИ",
          "url": "/catalog/skirts_midi",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3606,
          "name": "МАКСИ",
          "url": "/catalog/skirts_maxi",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2102,
          "name": "МИНИ",
          "url": "/catalog/skirts_mini",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4039,
          "name": "ЛЬНЯНЫЕ",
          "url": "/catalog/skirts_linen",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3679,
          "name": "ДЖИНСОВЫЕ",
          "url": "/catalog/skirts_denim",
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
      "id": 3314,
      "name": "КОМПЛЕКТЫ",
      "url": "/catalog/co_ord_sets",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 4025,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/co_ord_sets",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4041,
          "name": "ЛЬНЯНЫЕ",
          "url": "/catalog/linen_co_ord_sets",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4020,
          "name": "ТРИКОТАЖНЫЕ",
          "url": "/catalog/knit_co_ord_sets",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4021,
          "name": "ДЖИНСОВЫЕ",
          "url": "/catalog/denim_co_ord_sets",
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
      "id": 2085,
      "name": "БЛЕЙЗЕРЫ | ЖИЛЕТЫ",
      "url": "/catalog/blazers",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 2481,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/blazers",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2482,
          "name": "ОДНОБОРТНЫЕ",
          "url": "/catalog/blazers_single_breasted",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2483,
          "name": "ДВУБОРТНЫЕ",
          "url": "/catalog/blazers_double_breasted",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3715,
          "name": "УКОРОЧЕННЫЕ",
          "url": "/catalog/blazers_cropped",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4035,
          "name": "ЛЬНЯНЫЕ",
          "url": "/catalog/blazers_linen",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2484,
          "name": "ЖИЛЕТЫ",
          "url": "/catalog/waistcoat",
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
      "id": 2062,
      "name": "БРЮКИ",
      "url": "/catalog/trousers",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 2064,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/trousers",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2066,
          "name": "СВОБОДНЫЙ КРОЙ",
          "url": "/catalog/bryuki_loose_fitting",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2068,
          "name": "ПРЯМОЙ КРОЙ",
          "url": "/catalog/trousers_straight",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3717,
          "name": "РАСКЛЕШЕННЫЕ",
          "url": "/catalog/bryuki_flares",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4024,
          "name": "С ЗАЩИПАМИ",
          "url": "/catalog/trousers_darted",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4057,
          "name": "ЛЬНЯНЫЕ",
          "url": "/catalog/trousers_linen",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2065,
          "name": "ДЖОГГЕРЫ",
          "url": "/catalog/bryuki_joggers",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2071,
          "name": "КАРГО | ПАРАШЮТЫ",
          "url": "/catalog/trousers_cargo",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2063,
          "name": "ЛЕГИНСЫ",
          "url": "/catalog/legginsy",
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
      "id": 2113,
      "name": "КОСТЮМЫ",
      "url": "/catalog/suits",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 4043,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/suits",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4046,
          "name": "КЛАССИЧЕСКИЕ",
          "url": "/catalog/suits_classic",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4044,
          "name": "ЛЬНЯНЫЕ",
          "url": "/catalog/suits_linen",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4045,
          "name": "ЦВЕТНЫЕ",
          "url": "/catalog/suits_color",
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
      "id": 3707,
      "name": "СВИТЕРЫ | КАРДИГАНЫ",
      "url": "/catalog/sweaters_and_cardigans",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 3710,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/sweaters_and_cardigans",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3708,
          "name": "СВИТЕРЫ",
          "url": "/catalog/tricotash_sweater",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3709,
          "name": "КАРДИГАНЫ",
          "url": "/catalog/cardigans",
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
      "id": 2072,
      "name": "ФУТБОЛКИ",
      "url": "/catalog/t_shirts",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 2073,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/t_shirts",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2074,
          "name": "БАЗОВЫЕ",
          "url": "/catalog/futbolki_basic",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2076,
          "name": "ДЛИННЫЙ РУКАВ",
          "url": "/catalog/futbolki_long_sleeve",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2075,
          "name": "КОРОТКИЙ РУКАВ",
          "url": "/catalog/futbolki_short_sleeve",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2077,
          "name": "С ПРИНТОМ",
          "url": "/catalog/futbolki_printed",
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
      "id": 4027,
      "name": "ДЕНИМ",
      "url": "/catalog/denim",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 4032,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/denim",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4028,
          "name": "КУРТКИ",
          "url": "/catalog/jackets_denim",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4029,
          "name": "РУБАШКИ",
          "url": "/catalog/shirts_denim",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4033,
          "name": "ДЖИНСЫ",
          "url": "/catalog/jeans",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4030,
          "name": "ЮБКИ",
          "url": "/catalog/skirts_denim",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4031,
          "name": "ШОРТЫ",
          "url": "/catalog/shorts_denim",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4087,
          "name": "КОМБИНЕЗОНЫ",
          "url": "/catalog/jumpsuits_denim",
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
      "id": 2052,
      "name": "ДЖИНСЫ",
      "url": "/catalog/jeans",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 2053,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/jeans",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2056,
          "name": "ПРЯМЫЕ",
          "url": "/catalog/dzhinsy_straight",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3740,
          "name": "РАСКЛЕШЕННЫЕ",
          "url": "/catalog/dzhinsy_flare_and_bootcut",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3610,
          "name": "ШИРОКИЕ",
          "url": "/catalog/dzhinsy_wide_leg",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2054,
          "name": "MOM FIT",
          "url": "/catalog/dzhinsy_mom",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2061,
          "name": "BOYFRIEND",
          "url": "/catalog/dzhinsy_boyfriend",
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
      "id": 2078,
      "name": "ТОПЫ | БОДИ",
      "url": "/catalog/tops",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 2080,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/tops",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2081,
          "name": "БАЗОВЫЕ",
          "url": "/catalog/basic_tops",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3741,
          "name": "УКОРОЧЕННЫЕ",
          "url": "/catalog/tops_crop",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4042,
          "name": "ЛЬНЯНЫЕ",
          "url": "/catalog/tops_linen",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2098,
          "name": "ТРИКОТАЖНЫЕ",
          "url": "/catalog/tricotash_topy",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2079,
          "name": "БОДИ",
          "url": "/catalog/bodi",
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
      "id": 2106,
      "name": "ШОРТЫ",
      "url": "/catalog/shorty",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 3803,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/shorty",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3804,
          "name": "БЕРМУДЫ",
          "url": "/catalog/shorty_bermudy",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3860,
          "name": "ДЖИНСОВЫЕ",
          "url": "/catalog/shorts_denim",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4040,
          "name": "ЛЬНЯНЫЕ",
          "url": "/catalog/shorts_linen",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3861,
          "name": "СПОРТИВНЫЕ",
          "url": "/catalog/shorts_sporty",
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
      "id": 2089,
      "name": "ТОЛСТОВКИ",
      "url": "/catalog/sweatshirts",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 3607,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/sweatshirts",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3608,
          "name": "БАЗОВЫЕ",
          "url": "/catalog/sweatshirt_basic",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3609,
          "name": "С ПРИНТОМ",
          "url": "/catalog/sweatshirt_printed",
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
      "id": 3820,
      "name": "СПОРТИВНЫЕ КОМПЛЕКТЫ",
      "url": "/catalog/sportswear",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": []
    },
    {
      "id": 2152,
      "name": "НИЖНЕЕ БЕЛЬЕ | ОДЕЖДА ДЛЯ ДОМА",
      "url": "/catalog/underwear",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 3039,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/underwear",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3042,
          "name": "БЮСТГАЛЬТЕРЫ",
          "url": "/catalog/bralettes",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3043,
          "name": "ТРУСЫ",
          "url": "/catalog/briefs",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3044,
          "name": "БОДИ",
          "url": "/catalog/bodysuits",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 6,
          "name": "ОДЕЖДА ДЛЯ ДОМА",
          "url": "/catalog/loungewear",
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
      "id": 2180,
      "name": "ОБУВЬ",
      "url": "/catalog/all_shoes",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 3637,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/all_shoes",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3639,
          "name": "КЕДЫ | КРОССОВКИ",
          "url": "/catalog/trainers",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3640,
          "name": "ТУФЛИ",
          "url": "/catalog/shoes",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3794,
          "name": "БАЛЕТКИ",
          "url": "/catalog/ballerinas",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3851,
          "name": "БОСОНОЖКИ | САНДАЛИИ",
          "url": "/catalog/sandals",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3641,
          "name": "ЛОФЕРЫ | САБО",
          "url": "/catalog/loafers",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3638,
          "name": "БОТИНКИ | САПОГИ",
          "url": "/catalog/boots",
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
      "id": 2462,
      "name": "СУМКИ",
      "url": "/catalog/bags",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 3792,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/bags",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3793,
          "name": "КОЖА",
          "url": "/catalog/bags_leather",
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
      "id": 3021,
      "name": "УКРАШЕНИЯ",
      "url": "/catalog/jewellery",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 3796,
          "name": "ВСЕ МОДЕЛИ ",
          "url": "/catalog/jewellery",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3795,
          "name": "СЕРЬГИ",
          "url": "/catalog/earrings",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3797,
          "name": "БРАСЛЕТЫ",
          "url": "/catalog/bracelets",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4019,
          "name": "КОЛЬЦА",
          "url": "/catalog/rings",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3798,
          "name": "ОЖЕРЕЛЬЯ",
          "url": "/catalog/necklaces",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3799,
          "name": "ДЛЯ ВОЛОС",
          "url": "/catalog/accessesories_hair",
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
      "id": 2140,
      "name": "АКСЕССУАРЫ",
      "url": "/catalog/accessories",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 2491,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/accessories",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2511,
          "name": "РЕМНИ",
          "url": "/catalog/belts",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3778,
          "name": "СОЛНЦЕЗАЩИТНЫЕ ОЧКИ",
          "url": "/catalog/sunglasses",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3019,
          "name": "БЕЙСБОЛКИ | ШАПКИ",
          "url": "/catalog/hats",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4056,
          "name": "ПЛАТКИ | ШАРФЫ",
          "url": "/catalog/scarves",
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
      "id": 4165,
      "name": "ПОСЛЕДНИЕ РАЗМЕРЫ",
      "url": "/catalog/last_sizes",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": []
    },
    {
      "id": 4107,
      "name": "ПРОМО",
      "url": "/catalog/sale",
      "marker": "highlight delimiter new",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 4120,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/sale",
          "marker": "highlight",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4108,
          "name": "ВЕРХНЯЯ ОДЕЖДА",
          "url": "/catalog/sale_verkhnyaya_odezhda",
          "marker": "highlight",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4109,
          "name": "БЛЕЙЗЕРЫ | ЖИЛЕТЫ",
          "url": "/catalog/sale_blazers",
          "marker": "highlight",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4110,
          "name": "БРЮКИ",
          "url": "/catalog/sale_bryuki",
          "marker": "highlight",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4111,
          "name": "КОСТЮМЫ",
          "url": "/catalog/sale_suits",
          "marker": "highlight",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4112,
          "name": "ПЛАТЬЯ | КОМБИНЕЗОНЫ",
          "url": "/catalog/sale_platya",
          "marker": "highlight",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4113,
          "name": "РУБАШКИ | БЛУЗЫ",
          "url": "/catalog/sale_rubashki_i_bluzki",
          "marker": "highlight",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4114,
          "name": "ДЖИНСЫ",
          "url": "/catalog/sale_dzhinsy",
          "marker": "highlight",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4115,
          "name": "ФУТБОЛКИ | ТОПЫ",
          "url": "/catalog/sale_futbolki",
          "marker": "highlight",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4116,
          "name": "ЮБКИ | ШОРТЫ ",
          "url": "/catalog/sale_skirts",
          "marker": "highlight",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4117,
          "name": "КОМПЛЕКТЫ",
          "url": "/catalog/sale_co_ord_sets",
          "marker": "highlight",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4118,
          "name": "ОДЕЖДА ДЛЯ ДОМА",
          "url": "/catalog/sale_underwear",
          "marker": "highlight",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4119,
          "name": "ОБУВЬ",
          "url": "/catalog/sale_shoes",
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
      "id": 3730,
      "name": "EDITORIAL",
      "url": "/catalog/belts",
      "marker": "delimiter",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 4014,
          "name": "LAZY MORNING",
          "url": "https://lime-shop.com/ru_ru/lp/underwear-summer24/",
          "marker": "static",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3768,
          "name": "DEEP BLUE",
          "url": "https://lime-shop.com/ru_ru/lp/woman-spring-24-basic/",
          "marker": "static",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3634,
          "name": "FORMS AND MOTIONS",
          "url": "https://lime-shop.com/ru_ru/lp/woman-spring-24-studio/",
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
      "id": 3842,
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