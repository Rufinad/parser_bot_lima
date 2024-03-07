from aiogram import Router, F, Bot, html
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.enums import ParseMode

from keyboards.inline_kb import start_keyboard
# from handlers.apsched import send_message_cron
from services.fts_parser import get_fts_news
from services.sigma_parser import get_sigma_news
from states.statesform import StartSG

router = Router()

''' 3 инлайн кнопки ведут себя по-разному, алерты, сообщение, всплывающее на 2-3 сек окно'''


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message, bot: Bot, state: FSMContext):
    await state.clear()
    await message.answer(text='Привет! Сейчас могу вот что рассказать 👇 ',
                         reply_markup=start_keyboard)


# @router.message(Command(commands='get_weather'))  # эта хрень работает если руками прописать /get_weather
@router.callback_query(F.data == 'FTS')
async def send_weather(callback: CallbackQuery):
    fts_data = get_fts_news()
    # for el in fts_data:
    #     url_text = el[1]
    await callback.answer(fts_data)


# @router.message(Command(commands='get_exchange_rate'))
@router.callback_query(F.data == 'Sigma')
async def send_rate(callback: CallbackQuery):
    sigma_news = get_sigma_news()
    await callback.answer(sigma_news)

