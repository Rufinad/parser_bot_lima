from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Создаем объекты инлайн-кнопок
button_1 = InlineKeyboardButton(
    text='FTS',
    callback_data='FTS'
)
button_2 = InlineKeyboardButton(
    text='Sigma',
    callback_data='Sigma'
)
button_3 = InlineKeyboardButton(
    text='Portnews',
    callback_data='Portnews'
)
button_4 = InlineKeyboardButton(
    text='Custom',
    callback_data='Custom'
)

# Создаем объект инлайн-клавиатуры
start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[button_1],
                     [button_2],
                     [button_3],
                     [button_4],
                     ])

