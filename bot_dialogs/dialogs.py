from bot_dialogs.handlers import select_top_size, select_lower_size, select_man_style, select_event, select_sex, \
    select_woman_style, select_woman_appearance
from states.statesform import StepsForm
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
from aiogram_dialog.widgets.text import Const, Format, List, Multi, Case, Jinja
from aiogram_dialog.widgets.kbd import Button, Row, ManagedMultiselect, Column, Group, Select
from bot_dialogs.getters import get_size_selections, get_man_style_selections, get_event_selections, \
    get_sex, get_woman_style_selections, get_woman_appearance

start_dialog = Dialog(
    Window(
        Const(text='Здравствуйте, для кого будем подбирать одежду?'),
        Select(
            Format('{item[0]}'),
            id='sex',
            item_id_getter=lambda x: x[1],
            items='sex',
            on_click=select_sex
        ),
        getter=get_sex,
        state=StepsForm.GET_TYPE),
    Window(
        Const(text='Какой у Вас размер верха?'),
        Select(
            Format('{item[0]}'),
            id='top_size',
            item_id_getter=lambda x: x[1],
            items='size',
            on_click=select_top_size
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
            on_click=select_lower_size
        ),
        state=StepsForm.GET_LOWER_SIZE,
        getter=get_size_selections
        ),
    Window(
        Const(text='Какого фасона предпочитаете носить одежду?'),
        Select(
            Format('{item[0]}'),
            id='man_style',
            item_id_getter=lambda x: x[1],
            items='man_style',
            on_click=select_man_style
            ),
        state=StepsForm.GET_MAN_STYLE,
        getter=get_man_style_selections,
        ),
    Window(
        Const(text='Какого фасона предпочитаете носить одежду?'),
        Select(
            Format('{item[0]}'),
            id='woman_style',
            item_id_getter=lambda x: x[1],
            items='woman_style',
            on_click=select_woman_style
        ),
        state=StepsForm.GET_WOMAN_STYLE,
        getter=get_woman_style_selections,
    ),
    Window(
        Const(text='Какой образ предпочитаете?'),
        Select(
            Format('{item[0]}'),
            id='woman_appearance',
            item_id_getter=lambda x: x[1],
            items='woman_appearance',
            on_click=select_woman_appearance
        ),
        state=StepsForm.GET_WOMAN_APPEARANCE,
        getter=get_woman_appearance,
    ),
    Window(
            Const(text='Для какого случая подбираете одежду?'),
            Select(
                Format('{item[0]}'),
                id='event',
                item_id_getter=lambda x: x[1],
                items='event',
                on_click=select_event
                ),
            state=StepsForm.GET_EVENT,
            getter=get_event_selections
            )
    )
