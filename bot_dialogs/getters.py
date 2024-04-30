from aiogram.types import CallbackQuery
from aiogram_dialog import StartMode, DialogManager
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs



async def username_getter(dialog_manager: DialogManager, event_from_user, **kwargs):
    return {'username': event_from_user.username}


# Это геттер
async def get_size_selections(**kwargs):
    size = [
        ('S', 1),
        ('M', 2),
        ('L', 3),
        ('XL', 4),
        ('XXL', 5),
    ]
    return {'size': size}


async def get_style_selections(**kwargs):
    style = [
        ('Строгий', 1),
        ('Расслабленный', 2),
    ]
    return {'style': style}


async def get_event_selections(**kwargs):
    event = [
        ('В офис', 1),
        ('На праздничный вечер', 2)
    ]
    return {'event': event}
