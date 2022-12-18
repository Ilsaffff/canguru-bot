from aiogram import Router, types
import logging
from aiogram.fsm.context import FSMContext
from attachments import keyboards as kb
router = Router()


@router.message()
async def other_words(message: types.Message, state=FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await message.answer('У тебя всё получится!', reply_markup=kb.start)
        return
    logging.info("Cancelling state %r", current_state)
    await message.answer('Нажми на кнопку :)')
