from aiogram import types, Dispatcher
from attachments import keyboards as kb
from attachments import messages as msg


async def bot_does(message: types.Message):
    await message.answer(msg.bot_does, reply_markup=kb.start)


def register_handler(dp: Dispatcher):
    dp.register_message_handler(bot_does, text='Что бот делает?')
