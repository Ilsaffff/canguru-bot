from aiogram.utils import executor
from handlers import start, registration, bot_does, who_we
from create_bot import dp

start.register_handler_start(dp)
registration.register_handlers_reg(dp)
bot_does.register_handler_start(dp)
who_we.register_handler_start(dp)

executor.start_polling(dp)
