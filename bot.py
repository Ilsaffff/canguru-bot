from aiogram.utils import executor
from handlers import start, registration
from create_bot import dp

start.register_handler_start(dp)
registration.register_handlers_reg(dp)

executor.start_polling(dp)
