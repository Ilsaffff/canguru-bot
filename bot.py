from aiogram.utils import executor
from handlers import start, cancel, registration, bot_does, who_we, search_mentor
from create_bot import dp

start.register_handler(dp)
cancel.register_handler(dp)
registration.register_handlers(dp)
bot_does.register_handler(dp)
who_we.register_handler(dp)
search_mentor.register_handler(dp)

executor.start_polling(dp)
