from bot_dialogs.handlers import select_top_size, select_lower_size, select_man_style, select_event, select_sex, \
    select_woman_style, select_woman_appearance, get_finish_links, restart_search
from states.statesform import StepsForm
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
from aiogram_dialog.widgets.text import Const, Format, List, Multi, Case, Jinja
from aiogram_dialog.widgets.kbd import Button, Row, ManagedMultiselect, Column, Group, Select, Url
from bot_dialogs.getters import get_size_selections, get_man_style_selections, get_event_selections, \
    get_sex, get_woman_style_selections, get_woman_appearance, get_woman_appearance_holiday, \
    get_woman_shirts, get_woman_blouses, get_woman_bracelets, get_woman_basic_tops, get_woman_trousers_straight, \
    get_woman_bryuki_flares, get_woman_dzhinsy_flare_and_bootcut, get_woman_dresses_mini, get_woman_skirts_maxi, \
    get_woman_skirts_midi, get_woman_bryuki_loose_fitting, get_woman_trousers_darted, get_woman_blazers_double_breasted, \
    get_woman_dzhinsy_wide_leg, get_woman_dresses_maxi, get_man_men_trousers_classic, get_man_men_shirts_formal, \
    get_man_men_blazers, get_man_men_trousers_chino, get_man_men_shirts_short_sleeve, \
    get_man_men_trousers_loose_fitting, get_man_men_shirts_linen

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
        Const(text='Какой образ предпочитаете?'),
        Select(
            Format('{item[0]}'),
            id='woman_appearance_holiday',
            item_id_getter=lambda x: x[1],
            items='woman_appearance',
            on_click=select_woman_appearance
        ),
        state=StepsForm.GET_WOMAN_APPEARANCE_HOLIDAY,
        getter=get_woman_appearance_holiday,
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
    ),
    Window(
        Const(
            text='Искусственный интеллект проанализировал более тысячи предметов гардероба и хочет предложить Вам лучшее!'),
        Button(
            text=Const('Показать подборку'),
            id='button_1',
            on_click=get_finish_links),
        state=StepsForm.GET_LINKS
    ),
    Window(
        Const('Результат работы искусственного интеллекта 👇'),
        Url(text=Const('Миди юбки'),
            url=Format('{skirts_midi}'),
            id='button_1_2'),
        Url(text=Const('Рубашки'),
            url=Format('{shirts}'),
            id='button_1_3'),
        Url(text=Const('Блузы'),
            url=Format('{blouses}'),
            id='button_1_4'),
        Url(text=Const('Браслеты'),
            url=Format('{bracelets}'),
            id='button_1_6'),
        Button(text=Const('Начать подборку заново!'),
               id='restart',
               on_click=restart_search
               ),
        getter=(get_woman_skirts_midi, get_woman_shirts, get_woman_blouses, get_woman_bracelets),
        state=StepsForm.VAR_1,
    ),
    Window(
        Const('Результат работы искусственного интеллекта 👇'),
        Url(text=Const('Миди юбки'),
            url=Format('{skirts_midi}'),
            id='button_2_2'),
        Url(text=Const('Топы базовые'),
            url=Format('{basic_tops}'),
            id='button_2_3'),
        Url(text=Const('Браслеты'),
            url=Format('{bracelets}'),
            id='button_2_6'),
        Button(text=Const('Начать подборку заново!'),
               id='restart',
               on_click=restart_search
               ),
        getter=(get_woman_skirts_midi, get_woman_basic_tops, get_woman_bracelets),
        state=StepsForm.VAR_2,
    ),
    Window(
        Const('Результат работы искусственного интеллекта 👇'),
        Url(text=Const('Брюки прямого кроя'),
            url=Format('{trousers_straight}'),
            id='button_3_2'),
        Url(text=Const('Топы базовые'),
            url=Format('{basic_tops}'),
            id='button_3_3'),
        Url(text=Const('Браслеты'),
            url=Format('{bracelets}'),
            id='button_3_6'),
        Button(text=Const('Начать подборку заново!'),
               id='restart',
               on_click=restart_search
               ),
        getter=(get_woman_trousers_straight, get_woman_basic_tops, get_woman_bracelets),
        state=StepsForm.VAR_3,
    ),
    Window(
        Const('Результат работы искусственного интеллекта 👇'),
        Url(text=Const('Брюки расклешенные'),
            url=Format('{bryuki_flares}'),
            id='button_4_2'),
        Url(text=Const('Рубашки'),
            url=Format('{shirts}'),
            id='button_4_3'),
        Url(text=Const('Блузы'),
            url=Format('{blouses}'),
            id='button_4_4'),
        Url(text=Const('Браслеты'),
            url=Format('{bracelets}'),
            id='button_4_6'),
        Button(text=Const('Начать подборку заново!'),
               id='restart',
               on_click=restart_search
               ),
        getter=(get_woman_bryuki_flares, get_woman_blouses, get_woman_shirts, get_woman_bracelets),
        state=StepsForm.VAR_4,
        ),
    Window(
        Const('Результат работы искусственного интеллекта 👇'),
        Url(text=Const('Джинсы расклешенные'),
            url=Format('{dzhinsy_flare_and_bootcut}'),
            id='button_5_2'),
        Url(text=Const('Топы базовые'),
            url=Format('{basic_tops}'),
            id='button_5_3'),
        Url(text=Const('Браслеты'),
            url=Format('{bracelets}'),
            id='button_5_6'),
        Button(text=Const('Начать подборку заново!'),
               id='restart',
               on_click=restart_search
               ),
        getter=(get_woman_dzhinsy_flare_and_bootcut, get_woman_bracelets, get_woman_basic_tops),
        state=StepsForm.VAR_5,
    ),
    Window(
        Const('Результат работы искусственного интеллекта 👇'),
        Url(text=Const('Платье мини'),
            url=Format('{dresses_mini}'),
            id='button_6_2'),
        Url(text=Const('Браслеты'),
            url=Format('{bracelets}'),
            id='button_6_6'),
        Button(text=Const('Начать подборку заново!'),
               id='restart',
               on_click=restart_search
               ),
        getter=(get_woman_dresses_mini, get_woman_bracelets),
        state=StepsForm.VAR_6,
    ),
    Window(
        Const('Результат работы искусственного интеллекта 👇'),
        Url(text=Const('Юбка макси'),
            url=Format('{skirts_maxi}'),
            id='button_7_2'),
        Url(text=Const('Рубашки'),
            url=Format('{shirts}'),
            id='button_7_3'),
        Url(text=Const('Браслеты'),
            url=Format('{bracelets}'),
            id='button_7_6'),
        Button(text=Const('Начать подборку заново!'),
               id='restart',
               on_click=restart_search
               ),
        getter=(get_woman_skirts_maxi, get_woman_shirts, get_woman_bracelets),
        state=StepsForm.VAR_7,
    ),
    Window(
        Const('Результат работы искусственного интеллекта 👇'),
        Url(text=Const('Юбка миди'),
            url=Format('{skirts_midi}'),
            id='button_8_2'),
        Url(text=Const('Топы базовые'),
            url=Format('{basic_tops}'),
            id='button_8_3'),
        Url(text=Const('Браслеты'),
            url=Format('{bracelets}'),
            id='button_8_6'),
        Button(text=Const('Начать подборку заново!'),
               id='restart',
               on_click=restart_search
               ),
        getter=(get_woman_skirts_midi, get_woman_basic_tops, get_woman_bracelets),
        state=StepsForm.VAR_8,
    ),
    Window(
        Const('Результат работы искусственного интеллекта 👇'),
        Url(text=Const('Брюки свободного кроя'),
            url=Format('{bryuki_loose_fitting}'),
            id='button_9_2'),
        Url(text=Const('Рубашки'),
            url=Format('{shirts}'),
            id='button_9_3'),
        Url(text=Const('Браслеты'),
            url=Format('{bracelets}'),
            id='button_9_6'),
        Button(text=Const('Начать подборку заново!'),
               id='restart',
               on_click=restart_search
               ),
        getter=(get_woman_bryuki_loose_fitting, get_woman_shirts, get_woman_bracelets),
        state=StepsForm.VAR_9,
    ),
    Window(
        Const('Результат работы искусственного интеллекта 👇'),
        Url(text=Const('Брюки с защипами'),
            url=Format('{trousers_darted}'),
            id='button_10_2'),
        Url(text=Const('Блейзеры двубортные'),
            url=Format('{blazers_double_breasted}'),
            id='button_10_3'),
        Url(text=Const('Браслеты'),
            url=Format('{bracelets}'),
            id='button_10_6'),
        Button(text=Const('Начать подборку заново!'),
               id='restart',
               on_click=restart_search
               ),
        getter=(get_woman_trousers_darted, get_woman_blazers_double_breasted, get_woman_bracelets),
        state=StepsForm.VAR_10,
    ),
    Window(
        Const('Результат работы искусственного интеллекта 👇'),
        Url(text=Const('Джинсы широкие'),
            url=Format('{dzhinsy_wide_leg}'),
            id='button_11_2'),
        Url(text=Const('Рубашки'),
            url=Format('{shirts}'),
            id='button_11_3'),
        Url(text=Const('Браслеты'),
            url=Format('{bracelets}'),
            id='button_11_6'),
        Button(text=Const('Начать подборку заново!'),
               id='restart',
               on_click=restart_search
               ),
        getter=(get_woman_dzhinsy_wide_leg, get_woman_shirts, get_woman_bracelets),
        state=StepsForm.VAR_11,
    ),
    Window(
        Const('Результат работы искусственного интеллекта 👇'),
        Url(text=Const('Платье макси'),
            url=Format('{dresses_maxi}'),
            id='button_12_2'),
        Url(text=Const('Браслеты'),
            url=Format('{bracelets}'),
            id='button_12_6'),
        Button(text=Const('Начать подборку заново!'),
               id='restart',
               on_click=restart_search
               ),
        getter=(get_woman_dresses_maxi, get_woman_bracelets),
        state=StepsForm.VAR_12,
    ),
    Window(
        Const('Результат работы искусственного интеллекта 👇'),
        Url(text=Const('Брюки классические'),
            url=Format('{men_trousers_classic}'),
            id='button_13_2'),
        Url(text=Const('Рубашки формальные'),
            url=Format('{men_shirts_formal}'),
            id='button_13_5'),
        Button(text=Const('Начать подборку заново!'),
               id='restart',
               on_click=restart_search
               ),
        getter=(get_man_men_trousers_classic, get_man_men_shirts_formal),
        state=StepsForm.VAR_13,
    ),
    Window(
        Const('Результат работы искусственного интеллекта 👇'),
        Url(text=Const('Брюки классические'),
            url=Format('{men_trousers_classic}'),
            id='button_14_2'),
        Url(text=Const('Блейзеры'),
            url=Format('{men_blazers}'),
            id='button_14_5'),
        Button(text=Const('Начать подборку заново!'),
               id='restart',
               on_click=restart_search
               ),
        getter=(get_man_men_trousers_classic, get_man_men_blazers),
        state=StepsForm.VAR_14,
    ),
    Window(
        Const('Результат работы искусственного интеллекта 👇'),
        Url(text=Const('Брюки. Чинос'),
            url=Format('{men_trousers_chino}'),
            id='button_15_2'),
        Url(text=Const('Рубашка с коротким рукавом'),
            url=Format('{men_shirts_short_sleeve}'),
            id='button_15_5'),
        Button(text=Const('Начать подборку заново!'),
               id='restart',
               on_click=restart_search
               ),
        getter=(get_man_men_trousers_chino, get_man_men_shirts_short_sleeve),
        state=StepsForm.VAR_15,
    ),
    Window(
        Const('Результат работы искусственного интеллекта 👇'),
        Url(text=Const('Брюки свободного кроя'),
            url=Format('{men_trousers_loose_fitting}'),
            id='button_16_2'),
        Url(text=Const('Рубашки льняные'),
            url=Format('{men_shirts_linen}'),
            id='button_16_5'),
        Button(text=Const('Начать подборку заново!'),
               id='restart',
               on_click=restart_search
               ),
        getter=(get_man_men_trousers_loose_fitting, get_man_men_shirts_linen),
        state=StepsForm.VAR_16,
    ),
)
