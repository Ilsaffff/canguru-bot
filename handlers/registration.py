from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from attachments import messages as msg
from attachments import keyboards as kb


class Registration(StatesGroup):
    name = State()
    age = State()
    city = State()
    description = State()


async def name(message: types.Message):
    await Registration.name.set()
    await message.answer(msg.reg_name)


async def age(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await Registration.next()
    await message.answer(msg.reg_age)


async def city(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    await Registration.next()
    await message.answer(msg.reg_city)


async def description(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text
    await Registration.next()
    await message.answer(msg.reg_description)


async def finish(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await state.finish()
    await message.answer(msg.reg_finish, reply_markup=kb.start)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(name, text='Регистрация', state=None)
    dp.register_message_handler(age, state=Registration.name)
    dp.register_message_handler(city, state=Registration.age)
    dp.register_message_handler(description, state=Registration.city)
    dp.register_message_handler(finish, state=Registration.description)
