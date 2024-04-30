import aiogram
from aiogram import Router, F
from aiogram_dialog import StartMode, DialogManager
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram_dialog.widgets.kbd import ManagedCheckbox, Multiselect, ManagedMultiselect
from states.statesform import StepsForm
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
from aiogram_dialog.widgets.kbd import Button, Select

router = Router()


# этот роутер реагирует на запуск бота
@router.message(CommandStart())
async def command_start_process(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=StepsForm.GET_TYPE, mode=StartMode.RESET_STACK)


# этот хендлер переключит состояние на выбор размера верха и запишет в диалог дату, что выбран мужик
async def for_man(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    dialog_manager.dialog_data['type'] = 'man'
    await dialog_manager.start(state=StepsForm.GET_TOP_SIZE)


# этот хендлер переключит состояние на выбор размера низа и запишет размер верха
async def get_top_size(callback: CallbackQuery, widget: Select, dialog_manager: DialogManager, item_id: str):
    dialog_manager.dialog_data['top_size'] = item_id
    print(f'размер верха {item_id}')
    await dialog_manager.start(state=StepsForm.GET_LOWER_SIZE)


# этот хендлер переключит состояние на выбор фасона и запишет размер низа
async def get_lower_size(callback: CallbackQuery, widget: Select, dialog_manager: DialogManager, item_id: str):
    dialog_manager.dialog_data['lower_size'] = item_id
    print(f'размер низа {item_id}')
    await dialog_manager.start(state=StepsForm.GET_STYLE)


# этот хендлер переключит состояние на выбор события и запишет фасон
async def get_style(callback: CallbackQuery, widget: Select, dialog_manager: DialogManager, item_id: str):
    dialog_manager.dialog_data['style'] = item_id
    print(f'фасон {item_id}')
    await dialog_manager.start(state=StepsForm.GET_EVENT)


# этот хендлер переключит состояние на предоставление ссылок на товары и запишет на какое событие подбираем шмотки
async def get_event(callback: CallbackQuery, widget: Select, dialog_manager: DialogManager, item_id: str):
    dialog_manager.dialog_data['event'] = item_id
    print(f'событие {item_id}')
    print(dialog_manager.dialog_data)
    # await callback.message.answer(f'В итоге ты выбрал: размер верха {dialog_manager.dialog_data["top_size"]}, '
    #                               f'размер низа {dialog_manager.dialog_data["lower_size"]},'
    #                               f'фасон {dialog_manager.dialog_data["style"]}',
    #                               f'событие {dialog_manager.dialog_data["event"]}')
    # await dialog_manager.start(state=StepsForm.GET_LINKS)