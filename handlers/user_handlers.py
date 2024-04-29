from aiogram import Router, F, Bot, html
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.enums import ParseMode

from keyboards.inline_kb import start_keyboard
from services.lima_parser_man import get_custom_news
# from handlers.apsched import send_message_cron
from services.fts_parser import get_fts_news
from services.portnews_parser import get_portnews
from services.sigma_parser import get_sigma_news


router = Router()

''' 3 инлайн кнопки ведут себя по-разному, алерты, сообщение, всплывающее на 2-3 сек окно'''


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message, bot: Bot, state: FSMContext):
    await state.clear()
    await message.answer(text='Привет! Сейчас могу вот что рассказать 👇 ',
                         reply_markup=start_keyboard)


@router.callback_query(F.data == 'FTS')
async def send_fts_news(callback: CallbackQuery):
    fts_data = get_fts_news()
    if fts_data:
        for item in fts_data:
            await callback.message.answer(text=f'<a href="{item[0]}">VED-TODAY</a>: {item[1]}',
                                   disable_web_page_preview=True)
    else:
        await callback.message.answer(text='к сожалению новых новостей с сайта https://ved.today нет')


@router.callback_query(F.data == 'Sigma')
async def send_sigma_news(callback: CallbackQuery):
    sigma_news = get_sigma_news()
    if sigma_news:
        for item in sigma_news:
            await callback.message.answer(text=f'<a href="{item[0]}">СИГМА-СОФТ</a>: {item[1]}',
                                   disable_web_page_preview=True)
    else:
        await callback.message.answer(text='к сожалению новых новостей с сайта https://www.sigma-soft.ru нет')


@router.callback_query(F.data == 'Portnews')
async def send_portnews(callback: CallbackQuery):
    portnews_data = get_portnews()
    if portnews_data:
        for item in portnews_data:
            await callback.message.answer(text=f'<a href="{item[0]}">PORTNEWS</a>: {item[1]}',
                                   disable_web_page_preview=True)
    else:
        await callback.message.answer(text='к сожалению новых новостей с сайта https://www.portnews.ru нет')


@router.callback_query(F.data == 'Custom')
async def send_portnews(callback: CallbackQuery):
    custom_data = get_custom_news()
    if custom_data:
        for item in custom_data:
            await callback.message.answer(text=f'<a href="{item[0]}">CUSTOM-GOV</a>: {item[1]}',
                                   disable_web_page_preview=True)
    else:
        await callback.message.answer(text='к сожалению новых новостей с сайта https://www.portnews.ru нет')