from aiogram import types, Router, F
from attachments import keyboards as kb
from attachments import messages as msg

router = Router()


@router.message(F.text == kb.start_titles[4])
async def bot_does(message: types.Message):
    await message.answer(msg.bot_does, reply_markup=kb.start)
