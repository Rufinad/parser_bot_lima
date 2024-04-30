from bot_dialogs.handlers import for_man, get_top_size, get_lower_size, get_style, get_event
from states.statesform import StepsForm
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
from aiogram_dialog.widgets.text import Const, Format, List, Multi, Case, Jinja
from aiogram_dialog.widgets.kbd import Button, Row, ManagedMultiselect, Column, Group, Select
from bot_dialogs.getters import username_getter, get_size_selections, get_style_selections, get_event_selections


start_dialog = Dialog(
    Window(
        Format('Привет, {username}!, Для кого подбираете одежду?'),
        Button(
            text=Const('Для мужчины'),
            id='button_1',
            on_click=for_man
            ),
        getter=username_getter,
        state=StepsForm.GET_TYPE),
    Window(
        Const(text='Какой у Вас размер верха?'),
        Select(
            Format('{item[0]}'),
            id='top_size',
            item_id_getter=lambda x: x[1],
            items='size',
            on_click=get_top_size
        ),
        state=StepsForm.GET_TOP_SIZE,
        getter=get_size_selections
        ),
    Window(
        Const(text='Какой у Вас размер низа?'),
        Select(
            Format('{item[0]}'),
            id='lower_size',
            item_id_getter=lambda x: x[1],
            items='size',
            on_click=get_lower_size
        ),
        state=StepsForm.GET_LOWER_SIZE,
        getter=get_size_selections
        ),
    Window(
        Const(text='Какого фасона предпочитаете носить одежду'),
        Select(
            Format('{item[0]}'),
            id='style',
            item_id_getter=lambda x: x[1],
            items='style',
            on_click=get_style
            ),
        state=StepsForm.GET_STYLE,
        getter=get_style_selections
        ),
    Window(
            Const(text='Для какого случая подбираете одежду?'),
            Select(
                Format('{item[0]}'),
                id='event',
                item_id_getter=lambda x: x[1],
                items='event',
                on_click=get_event
                ),
            state=StepsForm.GET_EVENT,
            getter=get_event_selections
            )
    )
