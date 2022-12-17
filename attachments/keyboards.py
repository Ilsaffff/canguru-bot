from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
start1 = KeyboardButton('Регистрация')
start.add(start1)
start2 = KeyboardButton('Поиск ментора')
start3 = KeyboardButton('Достигатор')
start4 = KeyboardButton('Кто мы?')
start5 = KeyboardButton('Что бот делает?')
start.add(start2, start3, start4, start5)

search_mentor1 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
search_mentor_kb1 = KeyboardButton('Все понятно!')
search_mentor_kb2 = KeyboardButton('Отмена')
search_mentor1.add(search_mentor_kb1, search_mentor_kb2)

search_mentor2 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
search_mentor_kb1 = KeyboardButton('Ага, всё понятно!')
search_mentor_kb2 = KeyboardButton('Не-а, объясните ещё раз')
search_mentor_kb3 = KeyboardButton('Отмена')
search_mentor2.add(search_mentor_kb1, search_mentor_kb2, search_mentor_kb3)

search_mentor3 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
search_mentor_kb1 = KeyboardButton('Интересно, сейчас изучу')
search_mentor_kb2 = KeyboardButton('Сделаю это позже')
search_mentor_kb3 = KeyboardButton('Отмена')
search_mentor3.add(search_mentor_kb1, search_mentor_kb2, search_mentor_kb3)