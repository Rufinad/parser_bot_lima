import json
from services.decode_unicode import decode_unicode
from services.hrefs_parser import get_hrefs
from typing import Dict
from aiogram.types import CallbackQuery
from aiogram_dialog import StartMode, DialogManager
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
import random
import time
from datetime import datetime
import locale
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

# async def username_getter(dialog_manager: DialogManager, event_from_user, **kwargs):
#     return {'username': event_from_user.username}


async def get_sex(dialog_manager: DialogManager, **kwargs):
    sex = [
        ("для мужчины", 1),
        ("для женщины", 2),
        ]
    dialog_manager.dialog_data['sex'] = sex
    return {'sex': sex}

async def get_size_selections(dialog_manager: DialogManager, **kwargs):
    size = [
        ('XXS', 1),
        ('XS', 2),
        ('S', 3),
        ('M', 4),
        ('L', 5),
        ('XL', 6),
        ('XXL', 7),
    ]
    dialog_manager.dialog_data['size'] = size
    return {'size': size}


async def get_man_style_selections(dialog_manager: DialogManager, **kwargs):
    man_style = [
        ('строгий', 1),
        ('расслабленный', 2),
    ]
    dialog_manager.dialog_data['man_style'] = man_style
    return {'man_style': man_style}


async def get_woman_style_selections(dialog_manager: DialogManager, **kwargs):
    woman_style = [
        ('по фигуре', 1),
        ('оверсайз', 2),
    ]
    dialog_manager.dialog_data['woman_style'] = woman_style
    return {'woman_style': woman_style}


async def get_woman_appearance(dialog_manager: DialogManager, **kwargs):
    woman_appearance = [
        ('с юбкой', 1),
        ('с брюками', 2),
        ('с джинсами', 3)
    ]
    dialog_manager.dialog_data['woman_appearance'] = woman_appearance
    return {'woman_appearance': woman_appearance}


async def get_woman_appearance_holiday(dialog_manager: DialogManager, **kwargs):
    woman_appearance = [
        ('с юбкой', 1),
        ('с брюками', 2),
        ('с платьем', 3)
    ]
    dialog_manager.dialog_data['woman_appearance'] = woman_appearance
    return {'woman_appearance': woman_appearance}

async def get_event_selections(dialog_manager: DialogManager, **kwargs):
    event = [
        ('в офис', 1),
        ('на праздничный вечер', 2)
    ]
    dialog_manager.dialog_data['event'] = event
    return {'event': event}


def get_href_product(url):
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
    decoded_data = decode_unicode(data)
    random_href = get_hrefs(decoded_data)
    print(random_href)
    return random_href


async def get_woman_skirts_midi(dialog_manager: DialogManager, **kwargs):
    random_href = get_href_product('https://lime-shop.com/api/section/skirts_midi')
    return {'skirts_midi': random_href}


async def get_woman_shirts(dialog_manager: DialogManager, **kwargs):
    random_href = get_href_product('https://lime-shop.com/api/section/shirts')
    return {'shirts': random_href}


async def get_woman_blouses(dialog_manager: DialogManager, **kwargs):
    random_href = get_href_product('https://lime-shop.com/api/section/blouses')
    return {'blouses': random_href}


async def get_woman_bracelets(dialog_manager: DialogManager, **kwargs):
    random_href = get_href_product('https://lime-shop.com/api/section/bracelets')
    return {'bracelets': random_href}


async def get_woman_basic_tops(dialog_manager: DialogManager, **kwargs):
    random_href = get_href_product('https://lime-shop.com/api/section/basic_tops')
    return {'basic_tops': random_href}


async def get_woman_trousers_straight(dialog_manager: DialogManager, **kwargs):
    random_href = get_href_product('https://lime-shop.com/api/section/trousers_straight')
    return {'trousers_straight': random_href}


async def get_woman_bryuki_flares(dialog_manager: DialogManager, **kwargs):
    random_href = get_href_product('https://lime-shop.com/api/section/bryuki_flares')
    return {'bryuki_flares': random_href}


async def get_woman_dzhinsy_flare_and_bootcut(dialog_manager: DialogManager, **kwargs):
    random_href = get_href_product('https://lime-shop.com/api/section/dzhinsy_flare_and_bootcut')
    return {'dzhinsy_flare_and_bootcut': random_href}


async def get_woman_dresses_mini(dialog_manager: DialogManager, **kwargs):
    random_href = get_href_product('https://lime-shop.com/api/section/dresses_mini')
    return {'dresses_mini': random_href}


async def get_woman_skirts_maxi(dialog_manager: DialogManager, **kwargs):
    random_href = get_href_product('https://lime-shop.com/api/section/skirts_maxi')
    return {'skirts_maxi': random_href}


async def get_woman_bryuki_loose_fitting(dialog_manager: DialogManager, **kwargs):
    random_href = get_href_product('https://lime-shop.com/api/section/bryuki_loose_fitting')
    return {'bryuki_loose_fitting': random_href}


async def get_woman_trousers_darted(dialog_manager: DialogManager, **kwargs):
    random_href = get_href_product('https://lime-shop.com/api/section/trousers_darted')
    return {'trousers_darted': random_href}


async def get_woman_blazers_double_breasted(dialog_manager: DialogManager, **kwargs):
    random_href = get_href_product('https://lime-shop.com/api/section/blazers_double_breasted')
    return {'blazers_double_breasted': random_href}


async def get_woman_dzhinsy_wide_leg(dialog_manager: DialogManager, **kwargs):
    random_href = get_href_product('https://lime-shop.com/api/section/dzhinsy_wide_leg')
    return {'dzhinsy_wide_leg': random_href}


async def get_woman_dresses_maxi(dialog_manager: DialogManager, **kwargs):
    random_href = get_href_product('https://lime-shop.com/api/section/dresses_maxi')
    return {'dresses_maxi': random_href}


async def get_man_men_trousers_classic(dialog_manager: DialogManager, **kwargs):
    random_href = get_href_product('https://lime-shop.com/api/section/men_trousers_classic')
    return {'men_trousers_classic': random_href}


async def get_man_men_shirts_formal(dialog_manager: DialogManager, **kwargs):
    random_href = get_href_product('https://lime-shop.com/api/section/men_shirts_formal')
    return {'men_shirts_formal': random_href}


async def get_man_men_blazers(dialog_manager: DialogManager, **kwargs):
    random_href = get_href_product('https://lime-shop.com/api/section/men_blazers')
    return {'men_blazers': random_href}


async def get_man_men_trousers_chino(dialog_manager: DialogManager, **kwargs):
    random_href = get_href_product('https://lime-shop.com/api/section/men_trousers_chino')
    return {'men_trousers_chino': random_href}


async def get_man_men_shirts_short_sleeve(dialog_manager: DialogManager, **kwargs):
    random_href = get_href_product('https://lime-shop.com/api/section/men_shirts_short_sleeve')
    return {'men_shirts_short_sleeve': random_href}


async def get_man_men_trousers_loose_fitting(dialog_manager: DialogManager, **kwargs):
    random_href = get_href_product('https://lime-shop.com/api/section/men_trousers_loose_fitting')
    return {'men_trousers_loose_fitting': random_href}


async def get_man_men_shirts_linen(dialog_manager: DialogManager, **kwargs):
    random_href = get_href_product('https://lime-shop.com/api/section/men_shirts_linen')
    return {'men_shirts_linen': random_href}