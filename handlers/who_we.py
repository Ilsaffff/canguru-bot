from aiogram import types, Dispatcher
from attachments import keyboards as kb
from attachments import messages as msg


async def who_we(message: types.Message):
    await message.answer(msg.who_we, reply_markup=kb.start)


def register_handler_start(dp: Dispatcher):
    dp.register_message_handler(who_we, text='Кто мы?')
