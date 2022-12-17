from aiogram import types, Router, F
from attachments import keyboards as kb
from attachments import messages as msg

router = Router()


@router.message(F.text == kb.start_titles[3])
async def who_we(message: types.Message):
    await message.answer(msg.who_we, reply_markup=kb.start)
