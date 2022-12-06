from aiogram import Bot, types
from aiogram import Dispatcher
from aiogram.utils import executor
import keyboards as kb
import messages as msg

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer(msg.message_start, reply_markup=kb.start)


if __name__ == '__main__':
    executor.start_polling(dp)
