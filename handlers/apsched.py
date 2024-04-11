from aiogram import Bot

from services.customs_parser import get_custom_news
from services.fts_parser import get_fts_news
from services.portnews_parser import get_portnews
from services.sigma_parser import get_sigma_news


async def fts_time(bot: Bot):
    fts_data = get_fts_news()
    if fts_data:
        for item in fts_data:
            await bot.send_message(chat_id='-1002077691327', text=f'<a href="{item[0]}">VED-TODAY</a>: {item[1]}',
                                   disable_web_page_preview=True)
    # else:
    #     await bot.send_message(chat_id='-1002077691327', text='к сожалению новых новостей с сайта ved.today нет')


async def sigma_time(bot: Bot):
    sigma_data = get_sigma_news()
    if sigma_data:
        for item in sigma_data:
            await bot.send_message(chat_id='-1002077691327', text=f'<a href="{item[0]}">СИГМА-СОФТ</a>: {item[1]}',
                                   disable_web_page_preview=True)
    # else:
    #     await bot.send_message(chat_id='-1002077691327', text='к сожалению новых новостей с сайта sigma-soft.ru нет')


async def custom_time(bot: Bot):
    custom_data = get_custom_news()
    if custom_data:
        for item in custom_data:
            await bot.send_message(chat_id='-1002077691327', text=f'<a href="{item[0]}">CUSTOM-GOV</a>: {item[1]}',
                                   disable_web_page_preview=True)


async def portnews_time(bot: Bot):
    portnews_data = get_portnews()
    if portnews_data:
        for item in portnews_data:
            await bot.send_message(chat_id='-1002077691327', text=f'<a href="{item[0]}">PORTNEWS</a>: {item[1]}',
                                   disable_web_page_preview=True)