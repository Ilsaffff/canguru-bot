from aiogram.fsm.context import FSMContext
from aiogram import types, Router, F
from attachments import keyboards as kb

router = Router()


@router.message(F.text == 'Отмена')
@router.message(F.text.casefold() == "Отмена")
async def cancel_handler(message: types.Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(
        "Отменено.",
        reply_markup=kb.start)
