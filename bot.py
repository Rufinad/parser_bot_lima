import asyncio
from datetime import datetime, timedelta
import logging
from aiogram import Bot, Dispatcher
from aiogram_dialog import setup_dialogs

import bot_dialogs.handlers
from bot_dialogs.dialogs import start_dialog
from keyboards.main_menu import set_main_menu
from config_data.config import Config, load_config
from aiogram.fsm.storage.redis import Redis, RedisStorage, DefaultKeyBuilder


"""цель бота: подбирать одежду по запросу пользователя"""

# Инициализируем логгер
logger = logging.getLogger(__name__)

async def main():
    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher()

    # Регистрируем роутеры в диспетчере
    dp.include_router(bot_dialogs.handlers.router)
    dp.include_router(start_dialog)
    setup_dialogs(dp)

    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # настраиваем главное меню
    await set_main_menu(bot)

    # Запускаем бота и пропускаем все накопленные входящие
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
