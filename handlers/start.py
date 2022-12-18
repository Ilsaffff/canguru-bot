from aiogram import types
from attachments import keyboards as kb
from attachments import messages as msg
from aiogram.filters.command import Command
from aiogram import Router

from aiogram.fsm.context import FSMContext

router = Router()


@router.message(Command(commands='start'))
async def start(message: types.Message, state=FSMContext):
    await state.clear()
    await message.answer(text=msg.start, reply_markup=kb.start)
