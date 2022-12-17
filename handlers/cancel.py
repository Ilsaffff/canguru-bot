from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from attachments import messages as msg
from attachments import keyboards as kb
from aiogram.dispatcher.filters import Text


async def cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(msg.cancel, reply_markup=kb.start)


def register_handler(dp: Dispatcher):
    dp.register_message_handler(cancel, state="*", text='Отмена')
    dp.register_message_handler(cancel, Text(equals='Отмена', ignore_case=True), state="*")
