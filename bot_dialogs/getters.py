from aiogram.types import CallbackQuery
from aiogram_dialog import StartMode, DialogManager
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs


# async def username_getter(dialog_manager: DialogManager, event_from_user, **kwargs):
#     return {'username': event_from_user.username}


async def get_sex(dialog_manager: DialogManager, **kwargs):
    sex = [
        ("Для мужчины", 1),
        ("Для женщины", 2),
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
        ('Строгий', 1),
        ('Расслабленный', 2),
    ]
    dialog_manager.dialog_data['man_style'] = man_style
    return {'man_style': man_style}


async def get_woman_style_selections(dialog_manager: DialogManager, **kwargs):
    woman_style = [
        ('По фигуре', 1),
        ('Оверсайз', 2),
    ]
    dialog_manager.dialog_data['woman_style'] = woman_style
    return {'woman_style': woman_style}


async def get_woman_appearance(dialog_manager: DialogManager, **kwargs):
    woman_appearance = [
        ('С юбкой', 1),
        ('С брюками', 2),
        ('С джинсами', 3)
    ]
    dialog_manager.dialog_data['woman_appearance'] = woman_appearance
    return {'woman_appearance': woman_appearance}


async def get_event_selections(dialog_manager: DialogManager, **kwargs):
    event = [
        ('В офис', 1),
        ('На праздничный вечер', 2)
    ]
    dialog_manager.dialog_data['event'] = event
    return {'event': event}
