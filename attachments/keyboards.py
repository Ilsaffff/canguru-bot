from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_titles = ['Регистрация', 'Поиск ментора', 'Достигатор', 'Кто мы?', 'Что бот делает?']
start = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=start_titles[0])],
              [KeyboardButton(text=start_titles[1]), KeyboardButton(text=start_titles[2])],
              [KeyboardButton(text=start_titles[3]), KeyboardButton(text=start_titles[4])], ],
    resize_keyboard=True)

search_mentor_titles = ['Отмена', 'Все понятно!', 'Ага, всё понятно!', 'Не-а, объясните ещё раз',
                        'Интересно, сейчас изучу', 'Сделаю это позже']
search_mentor1 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=search_mentor_titles[1])],
                                               [KeyboardButton(text=search_mentor_titles[0])], ],
                                     resize_keyboard=True)
search_mentor2 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=search_mentor_titles[2])],
                                               [KeyboardButton(text=search_mentor_titles[3])],
                                               [KeyboardButton(text=search_mentor_titles[0])], ],
                                     resize_keyboard=True)
search_mentor3 = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=search_mentor_titles[4])],
                                               [KeyboardButton(text=search_mentor_titles[5])],
                                               [KeyboardButton(text=search_mentor_titles[0])], ],
                                     resize_keyboard=True)
