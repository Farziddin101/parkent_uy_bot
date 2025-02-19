from aiogram.dispatcher.filters.state import State, StatesGroup

class Form(StatesGroup):
    MAIN = State()
    PARKENT_MAIN = State()
    PARKENT_READY = State()
    PARKENT_UNDER_CONSTRUCTION = State()
    PARKENT_GALLERY = State()
    LAKESIDE_MAIN = State()
    LAKESIDE_READY = State()
    LAKESIDE_100PERSENT = State()
    LAKESIDE_5PERSENT = State()
    LAKESIDE_CREDIT = State()
    LAKESIDE_PHOTO = State()
    LAKESIDE_GALLERY = State()
