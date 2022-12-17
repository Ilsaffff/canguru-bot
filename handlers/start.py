from aiogram import types, Dispatcher
from attachments import keyboards as kb
from attachments import messages as msg


async def start(message: types.Message):
    await message.answer(msg.start, reply_markup=kb.start)


def register_handler(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')
