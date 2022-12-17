from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import types, Router, F
from aiogram.filters import Command
from attachments import messages as msg
from attachments import keyboards as kb
import logging

router = Router()


@router.message(F.text == 'Отмена')
@router.message(F.text.casefold() == "Отмена")
async def cancel_handler(message: types.Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info("Cancelling state %r", current_state)
    await state.clear()
    await message.answer(
        "Отменено.",
        reply_markup=kb.start)
