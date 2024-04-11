import asyncio
from datetime import datetime, timedelta
import logging
from aiogram import Bot, Dispatcher
from handlers import user_handlers, apsched
from keyboards.main_menu import set_main_menu
from config_data.config import Config, load_config
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.fsm.storage.redis import Redis, RedisStorage, DefaultKeyBuilder
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler_di import ContextSchedulerDecorator
import asyncpg


"""цель бота отправлять в канал сообщение с новостями, которые были получены при помощи парcинга сайтов"""

# Инициализируем логгер
logger = logging.getLogger(__name__)

async def main():
    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher()
    # создадим хранилище с помощью Redis и передадим в диспетчер
    redis_storage = RedisStorage.from_url(
        url='redis://localhost:6379/0',
        key_builder=DefaultKeyBuilder(with_destiny=True, with_bot_id=True),
    )

    dp = Dispatcher(storage=redis_storage)
    jobstores = {
        'default': RedisJobStore(jobs_key='dispatched_trips_jobs',
                                 run_times_key='dispatched_trips_running',
                                 )
    }

    # добавляем возможность отправки сообщений по времени
    scheduler = ContextSchedulerDecorator(AsyncIOScheduler(timezone='Europe/Moscow', jobstores=jobstores))
    scheduler.ctx.add_instance(bot, declared_class=Bot)
    # scheduler.add_job(apsched.fts_time, trigger='date', run_date=datetime.now() + timedelta(seconds=10))
    # scheduler.add_job(apsched.sigma_time, trigger='date', run_date=datetime.now() + timedelta(seconds=10))
    # scheduler.add_job(apsched.custom_time, trigger='date', run_date=datetime.now() + timedelta(seconds=10))
    scheduler.add_job(apsched.sigma_time, trigger='cron', hour='17',
                      minute='00', start_date=datetime.now())
    scheduler.add_job(apsched.custom_time, trigger='cron', hour='18',
                      minute='00', start_date=datetime.now())
    scheduler.add_job(apsched.fts_time, trigger='cron', hour='20',
                      minute='00', start_date=datetime.now())
    scheduler.add_job(apsched.portnews_time, trigger='cron', hour='19',
                      minute='00', start_date=datetime.now())

    scheduler.start()

    # Регистриуем роутеры в диспетчере
    dp.include_router(user_handlers.router)

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