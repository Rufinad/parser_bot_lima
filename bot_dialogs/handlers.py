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


# этот хендлер переключит состояние на выбор размера верха и запишет в диалог дату, кому выбираем одежду
async def select_sex(callback: CallbackQuery, button: Button, dialog_manager: DialogManager, item_id: str):
    selected_sex = dialog_manager.dialog_data['sex'][int(item_id)-1][0]  # достаем из геттера
    dialog_manager.dialog_data['sel_sex'] = selected_sex
    await dialog_manager.switch_to(state=StepsForm.GET_TOP_SIZE)


# этот хендлер переключит состояние на выбор размера низа и запишет размер верха
async def select_top_size(callback: CallbackQuery, widget: Select, dialog_manager: DialogManager, item_id: str):
    selected_size = dialog_manager.dialog_data['size'][int(item_id)-1][0]  # достаем из геттера
    dialog_manager.dialog_data['top_size'] = selected_size
    await dialog_manager.switch_to(state=StepsForm.GET_LOWER_SIZE)


# этот хендлер переключит состояние на выбор фасона и запишет размер низа
async def select_lower_size(callback: CallbackQuery, widget: Select, dialog_manager: DialogManager, item_id: str):
    selected_size = dialog_manager.dialog_data['size'][int(item_id)-1][0]  # достаем из геттера
    dialog_manager.dialog_data['lower_size'] = selected_size
    if dialog_manager.dialog_data['sel_sex'] == 'Для мужчины':
        await dialog_manager.switch_to(state=StepsForm.GET_MAN_STYLE)
    else:
        await dialog_manager.switch_to(state=StepsForm.GET_WOMAN_STYLE)


# этот хендлер переключит состояние на выбор события и запишет фасон для мужчины
async def select_man_style(callback: CallbackQuery, widget: Select, dialog_manager: DialogManager, item_id: str):
    selected_style = dialog_manager.dialog_data['man_style'][int(item_id)-1][0]  # достаем из геттера
    dialog_manager.dialog_data['sel_style'] = selected_style
    await dialog_manager.switch_to(state=StepsForm.GET_EVENT)


# этот хендлер переключит состояние на выбор образа женщины и запишет фасон для женщины
async def select_woman_style(callback: CallbackQuery, widget: Select, dialog_manager: DialogManager, item_id: str):
    selected_style = dialog_manager.dialog_data['woman_style'][int(item_id)-1][0]  # достаем из геттера
    dialog_manager.dialog_data['sel_style'] = selected_style
    await dialog_manager.switch_to(state=StepsForm.GET_WOMAN_APPEARANCE)


# этот хендлер переключит состояние на выбор события и запишет образ для женщины
async def select_woman_appearance(callback: CallbackQuery, widget: Select, dialog_manager: DialogManager, item_id: str):
    selected_woman_appearance = dialog_manager.dialog_data['woman_appearance'][int(item_id)-1][0]  # достаем из геттера
    dialog_manager.dialog_data['sel_woman_appearance'] = selected_woman_appearance
    await dialog_manager.switch_to(state=StepsForm.GET_EVENT)


# этот хендлер переключит состояние на предоставление ссылок на товары и запишет на какое событие подбираем шмотки
async def select_event(callback: CallbackQuery, widget: Select, dialog_manager: DialogManager, item_id: str):
    selected_event = dialog_manager.dialog_data['event'][int(item_id)-1][0]
    dialog_manager.dialog_data['sel_event'] = selected_event
    await callback.message.answer(text=f'Определены параметры для поиска!'
                                       f' Ищем одежду: {dialog_manager.dialog_data["sel_sex"]}, '
                                       f' размер верха: {dialog_manager.dialog_data["top_size"]}, '
                                  f'размер низа: {dialog_manager.dialog_data["lower_size"]}, '
                                  f'фасон: {dialog_manager.dialog_data["sel_style"]},'
                                       f' событие: {dialog_manager.dialog_data["sel_event"]}')
    # await dialog_manager.switch_to(state=StepsForm.GET_LINKS)