from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import types, Router, F
from attachments import messages as msg
from attachments import keyboards as kb
from aiogram.types import ReplyKeyboardRemove
from data_base.db import DBHelper


db = DBHelper()

router = Router()


class Registration(StatesGroup):
    name = State()
    age = State()
    city = State()
    description = State()


@router.message(F.text == kb.start_titles[0])
async def name(message: types.Message, state: FSMContext):
    if not db.user_regist(user_id=message.from_user.id):
        await state.set_state(Registration.name)
        await message.answer(msg.reg_name, reply_markup=ReplyKeyboardRemove())
    else:
        await state.clear()
        await message.answer('Ты уже зарегистрирован :)', reply_markup=kb.start)


@router.message(Registration.name)
async def age(message: types.Message, state=FSMContext):
    await state.update_data(name=message.text)
    await message.answer(msg.reg_age)
    await state.set_state(Registration.age)


@router.message(Registration.age)
async def city(message: types.Message, state=FSMContext):
    data = await state.update_data(age=message.text)
    await state.set_state(Registration.city)
    await message.answer(msg.reg_city)


@router.message(Registration.city)
async def description(message: types.Message, state=FSMContext):
    data = await state.update_data(city=message.text)
    await state.set_state(Registration.description)
    await message.answer(msg.reg_description)


@router.message(Registration.description)
async def finish(message: types.Message, state=FSMContext):
    data = await state.update_data(description=message.text)
    db.add_user(user_id=message.from_user.id,
                username=message.from_user.username,
                first_name=data['name'],
                age=data['age'],
                city=data['city'],
                description=data['description'])
    await state.clear()
    await message.answer(msg.reg_finish, reply_markup=kb.start)
