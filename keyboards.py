from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

start = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3, one_time_keyboard=True)
start1 = KeyboardButton('Кто мы?')
start2 = KeyboardButton('Что бот делает?')
start3 = KeyboardButton('Регистрация')
start4 = KeyboardButton('Поиск ментора')
start5 = KeyboardButton('Достигатор')
start.add(start1, start2, start3, start4, start5)

