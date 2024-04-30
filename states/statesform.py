from aiogram.fsm.state import StatesGroup, State


class StepsForm(StatesGroup):
    GET_TYPE = State()
    GET_TOP_SIZE = State()
    GET_LOWER_SIZE = State()
    GET_STYLE = State()
    GET_EVENT = State()
    GET_LINKS = State()




