import json

import requests

url = "https://lime-shop.com/api/menu/left_kids"

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


decoded_data_kids = decode_unicode(data)
# print(decoded_data)

# print(json.dumps(decoded_data, ensure_ascii=False, indent=2))


'''
"/home/san/Рабочий стол/freelance/parser_bot_lima/venv/bin/python" /home/san/Рабочий стол/freelance/parser_bot_lima/services/lima_parser_kids.py 
{
  "items": [
    {
      "id": 4090,
      "name": "HAPPY FARM",
      "url": "/catalog/kids_happy_farm",
      "marker": "delimiter new",
      "theme": {
        "color": null,
        "background": null
      },
      "items": []
    },
    {
      "id": 2525,
      "name": "ДЕВОЧКИ | 7-14 ЛЕТ",
      "url": "/catalog/kids_all",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 2526,
          "name": "НОВИНКИ",
          "url": "/catalog/kids_girls_new",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2527,
          "name": "ТОЛСТОВКИ",
          "url": "/catalog/kids_girls_sweatshirts",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2534,
          "name": "БРЮКИ",
          "url": "/catalog/kids_girls_trousers",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2528,
          "name": "ФУТБОЛКИ | ТОПЫ",
          "url": "/catalog/kids_girls_t_shirts",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2529,
          "name": "ДЖИНСЫ",
          "url": "/catalog/kids_girls_jeans",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2536,
          "name": "ПЛАТЬЯ",
          "url": "/catalog/kids_girls_dresses",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2530,
          "name": "РУБАШКИ",
          "url": "/catalog/kids_girls_shirts",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2532,
          "name": "ЮБКИ | ШОРТЫ",
          "url": "/catalog/kids_girls_skirts",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2531,
          "name": "ТРИКОТАЖ",
          "url": "/catalog/kids_girls_knitwear",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3593,
          "name": "КУРТКИ | БЛЕЙЗЕРЫ",
          "url": "/catalog/kids_girls_jackets",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2981,
          "name": "КОМПЛЕКТЫ",
          "url": "/catalog/kids_girls_co_orders",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2537,
          "name": "ОБУВЬ",
          "url": "/catalog/kids_girls_shoes",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3086,
          "name": "АКСЕССУАРЫ | УКРАШЕНИЯ",
          "url": "/catalog/kids_girls_accessories",
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
      "id": 2538,
      "name": "МАЛЬЧИКИ | 7-14 ЛЕТ",
      "url": "/catalog/kids_all",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 2539,
          "name": "НОВИНКИ",
          "url": "/catalog/kids_boys_new",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2540,
          "name": "ТОЛСТОВКИ",
          "url": "/catalog/kids_boys_sweatshirts",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2545,
          "name": "БРЮКИ",
          "url": "/catalog/kids_boys_trousers",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2541,
          "name": "ФУТБОЛКИ | ПОЛО",
          "url": "/catalog/kids_boys_t_shirts",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2542,
          "name": "ДЖИНСЫ",
          "url": "/catalog/kids_boys_jeans",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2543,
          "name": "РУБАШКИ",
          "url": "/catalog/kids_boys_shirts",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4080,
          "name": "ШОРТЫ",
          "url": "/catalog/kids_boys_shorts",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2544,
          "name": "СВИТЕРЫ",
          "url": "/catalog/kids_boys_knitwear",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3590,
          "name": "КУРТКИ",
          "url": "/catalog/kids_boys_jackets",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2982,
          "name": "КОМПЛЕКТЫ",
          "url": "/catalog/kids_boys_co_orders",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2548,
          "name": "ОБУВЬ",
          "url": "/catalog/kids_boys_shoes",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3128,
          "name": "АКСЕССУАРЫ",
          "url": "/catalog/kids_boys_accessories",
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
      "id": 2549,
      "name": "ДЕВОЧКИ | 3-6 ЛЕТ",
      "url": "/catalog/kids_all",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 2550,
          "name": "НОВИНКИ",
          "url": "/catalog/kids_baby_girls_new",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2552,
          "name": "ТОЛСТОВКИ",
          "url": "/catalog/kids_baby_girls_sweatshirts",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3067,
          "name": "БРЮКИ | ЛЕГИНСЫ",
          "url": "/catalog/kids_baby_girls_all_trousers",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2551,
          "name": "ФУТБОЛКИ | ТОПЫ",
          "url": "/catalog/kids_baby_girls_t_shirts",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4016,
          "name": "ЮБКИ | ШОРТЫ",
          "url": "/catalog/kids_baby_girls_skirts",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3027,
          "name": "ТРИКОТАЖ",
          "url": "/catalog/kids_baby_girls_knitwear",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2964,
          "name": "ДЖИНСЫ",
          "url": "/catalog/kids_baby_girls_jeans",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3627,
          "name": "РУБАШКИ",
          "url": "/catalog/kids_baby_girls_shirts",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3779,
          "name": "ПЛАТЬЯ",
          "url": "/catalog/kids_baby_girls_dresses",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3693,
          "name": "КУРТКИ | ЖИЛЕТЫ",
          "url": "/catalog/kids_baby_girls_jackets",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2983,
          "name": "КОМПЛЕКТЫ",
          "url": "/catalog/kids_baby_girls_co_orders",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2557,
          "name": "ОБУВЬ",
          "url": "/catalog/kids_baby_girls_shoes",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3087,
          "name": "АКСЕССУАРЫ | УКРАШЕНИЯ",
          "url": "/catalog/kids_baby_girls_accessories",
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
      "id": 2558,
      "name": "МАЛЬЧИКИ | 3-6 ЛЕТ",
      "url": "/catalog/kids_all",
      "marker": "",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 2559,
          "name": "НОВИНКИ",
          "url": "/catalog/kids_baby_boys_new",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2561,
          "name": "ТОЛСТОВКИ",
          "url": "/catalog/kids_baby_boys_sweatshirts",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2562,
          "name": "БРЮКИ | ШОРТЫ",
          "url": "/catalog/kids_baby_boys_trousers",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2560,
          "name": "ФУТБОЛКИ | ПОЛО",
          "url": "/catalog/kids_baby_boys_t_shirts_basics",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2962,
          "name": "ДЖИНСЫ",
          "url": "/catalog/kids_baby_boys_jeans",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2563,
          "name": "РУБАШКИ",
          "url": "/catalog/kids_baby_boys_shirts",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3694,
          "name": "КУРТКИ | ЖИЛЕТЫ",
          "url": "/catalog/kids_baby_boys_jackets",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4094,
          "name": "КОМПЛЕКТЫ",
          "url": "/catalog/kids_baby_boys_co_orders",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 2565,
          "name": "ОБУВЬ",
          "url": "/catalog/kids_baby_boys_shoes",
          "marker": "",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3088,
          "name": "АКСЕССУАРЫ",
          "url": "/catalog/kids_baby_boys_accessories",
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
      "id": 4121,
      "name": "ПРОМО",
      "url": "/catalog/kids_sale",
      "marker": "highlight delimiter new",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 4142,
          "name": "ВСЕ МОДЕЛИ",
          "url": "/catalog/kids_sale",
          "marker": "highlight",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 4122,
          "name": "ДЕВОЧКИ | 7-14",
          "url": "/catalog/kids_girls_sale",
          "marker": "highlight",
          "theme": {
            "color": null,
            "background": null
          },
          "items": [
            {
              "id": 4143,
              "name": "ВСЕ МОДЕЛИ",
              "url": "/catalog/kids_girls_sale",
              "marker": "highlight",
              "theme": {
                "color": null,
                "background": null
              },
              "items": []
            },
            {
              "id": 4123,
              "name": "КУРТКИ | ЖИЛЕТЫ",
              "url": "/catalog/kids_girls_sale_jackets",
              "marker": "highlight",
              "theme": {
                "color": null,
                "background": null
              },
              "items": []
            },
            {
              "id": 4124,
              "name": "ТОЛСТОВКИ | ТРИКОТАЖ",
              "url": "/catalog/kids_girls_sale_sweatshirts",
              "marker": "highlight",
              "theme": {
                "color": null,
                "background": null
              },
              "items": []
            },
            {
              "id": 4125,
              "name": "БРЮКИ | ЮБКИ",
              "url": "/catalog/kids_girls_sale_trousers",
              "marker": "highlight",
              "theme": {
                "color": null,
                "background": null
              },
              "items": []
            },
            {
              "id": 4147,
              "name": "ФУТБОЛКИ | РУБАШКИ",
              "url": "/catalog/kids_girls_sale_t_shirts",
              "marker": "highlight",
              "theme": {
                "color": null,
                "background": null
              },
              "items": []
            },
            {
              "id": 4161,
              "name": "ОБУВЬ",
              "url": "/catalog/kids_girls_sale_shoes",
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
          "id": 4127,
          "name": "МАЛЬЧИКИ | 7-14",
          "url": "/catalog/kids_boys_sale",
          "marker": "highlight",
          "theme": {
            "color": null,
            "background": null
          },
          "items": [
            {
              "id": 4144,
              "name": "ВСЕ МОДЕЛИ",
              "url": "/catalog/kids_boys_sale",
              "marker": "highlight",
              "theme": {
                "color": null,
                "background": null
              },
              "items": []
            },
            {
              "id": 4128,
              "name": "КУРТКИ | ЖИЛЕТЫ",
              "url": "/catalog/kids_boys_sale_jackets",
              "marker": "highlight",
              "theme": {
                "color": null,
                "background": null
              },
              "items": []
            },
            {
              "id": 4129,
              "name": "ФУТБОЛКИ | РУБАШКИ",
              "url": "/catalog/kids_boys_sale_t_shirts",
              "marker": "highlight",
              "theme": {
                "color": null,
                "background": null
              },
              "items": []
            },
            {
              "id": 4130,
              "name": "БРЮКИ | ДЖИНСЫ",
              "url": "/catalog/kids_boys_sale_trousers",
              "marker": "highlight",
              "theme": {
                "color": null,
                "background": null
              },
              "items": []
            },
            {
              "id": 4131,
              "name": "ТОЛСТОВКИ",
              "url": "/catalog/kids_boys_sale_sweatshirts",
              "marker": "highlight",
              "theme": {
                "color": null,
                "background": null
              },
              "items": []
            },
            {
              "id": 4162,
              "name": "ОБУВЬ",
              "url": "/catalog/kids_boys_sale_shoes",
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
          "id": 4132,
          "name": "ДЕВОЧКИ | 3-6",
          "url": "/catalog/kids_baby_girls_sale",
          "marker": "highlight",
          "theme": {
            "color": null,
            "background": null
          },
          "items": [
            {
              "id": 4145,
              "name": "ВСЕ МОДЕЛИ",
              "url": "/catalog/kids_baby_girls_sale",
              "marker": "highlight",
              "theme": {
                "color": null,
                "background": null
              },
              "items": []
            },
            {
              "id": 4133,
              "name": "КУРТКИ | ЖИЛЕТЫ",
              "url": "/catalog/kids_baby_girls_sale_jackets",
              "marker": "highlight",
              "theme": {
                "color": null,
                "background": null
              },
              "items": []
            },
            {
              "id": 4134,
              "name": "ТОЛСТОВКИ | ФУТБОЛКИ",
              "url": "/catalog/kids_baby_girls_sale_sweatshirts",
              "marker": "highlight",
              "theme": {
                "color": null,
                "background": null
              },
              "items": []
            },
            {
              "id": 4135,
              "name": "БРЮКИ | ДЖИНСЫ",
              "url": "/catalog/kids_baby_girls_sale_trousers",
              "marker": "highlight",
              "theme": {
                "color": null,
                "background": null
              },
              "items": []
            },
            {
              "id": 4136,
              "name": "ПЛАТЬЯ",
              "url": "/catalog/kids_baby_girls_sale_dresses",
              "marker": "highlight",
              "theme": {
                "color": null,
                "background": null
              },
              "items": []
            },
            {
              "id": 4163,
              "name": "ОБУВЬ",
              "url": "/catalog/kids_baby_girls_sale_shoes",
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
          "id": 4137,
          "name": "МАЛЬЧИКИ | 3-6",
          "url": "/catalog/kids_baby_boys_sale",
          "marker": "highlight",
          "theme": {
            "color": null,
            "background": null
          },
          "items": [
            {
              "id": 4146,
              "name": "ВСЕ МОДЕЛИ",
              "url": "/catalog/kids_baby_boys_sale",
              "marker": "highlight",
              "theme": {
                "color": null,
                "background": null
              },
              "items": []
            },
            {
              "id": 4138,
              "name": "КУРТКИ | ЖИЛЕТЫ",
              "url": "/catalog/kids_baby_boys_sale_jackets",
              "marker": "highlight",
              "theme": {
                "color": null,
                "background": null
              },
              "items": []
            },
            {
              "id": 4139,
              "name": "ТОЛСТОВКИ",
              "url": "/catalog/kids_baby_boys_sale_sweatshirts",
              "marker": "highlight",
              "theme": {
                "color": null,
                "background": null
              },
              "items": []
            },
            {
              "id": 4140,
              "name": "БРЮКИ",
              "url": "/catalog/kids_baby_boys_sale_trousers",
              "marker": "highlight",
              "theme": {
                "color": null,
                "background": null
              },
              "items": []
            },
            {
              "id": 4141,
              "name": "ФУТБОЛКИ | РУБАШКИ",
              "url": "/catalog/kids_baby_boys_sale_t_shirts",
              "marker": "highlight",
              "theme": {
                "color": null,
                "background": null
              },
              "items": []
            },
            {
              "id": 4164,
              "name": "ОБУВЬ",
              "url": "/catalog/kids_baby_boys_sale_shoes",
              "marker": "highlight",
              "theme": {
                "color": null,
                "background": null
              },
              "items": []
            }
          ]
        }
      ]
    },
    {
      "id": 3702,
      "name": "EDITORIAL",
      "url": "/catalog/kids_and_moms",
      "marker": "delimiter",
      "theme": {
        "color": null,
        "background": null
      },
      "items": [
        {
          "id": 4009,
          "name": "DREAMY COLORS",
          "url": "https://lime-shop.com/ru_ru/lp/kids-summer24/",
          "marker": "static",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3645,
          "name": "MUSEUM ADVENTURES",
          "url": "https://lime-shop.com/ru_ru/lp/kids-spring24/",
          "marker": "static",
          "theme": {
            "color": null,
            "background": null
          },
          "items": []
        },
        {
          "id": 3703,
          "name": "KIDS & MOMS",
          "url": "https://lime-shop.com/ru_ru/lp/kids-and-moms/",
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
      "id": 3844,
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