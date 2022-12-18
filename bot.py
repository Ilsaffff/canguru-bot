import asyncio
from attachments.config import TOKEN
from aiogram import Bot, Dispatcher
from handlers import start, search_mentor, cancel, who_we, registration, bot_does, achiever, other_words

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(start.router)
dp.include_router(cancel.router)
dp.include_router(registration.router)
dp.include_router(search_mentor.router)
dp.include_router(who_we.router)
dp.include_router(bot_does.router)
dp.include_router(achiever.router)
dp.include_router(other_words.router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
