from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import types, Router, F
from attachments import messages as msg
from attachments import keyboards as kb
from aiogram.types import ReplyKeyboardRemove
from data_base.db import DBHelper

db = DBHelper()

router = Router()


class Acheiver(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()
    step4 = State()
    goal = State()


@router.message(F.text == kb.start_titles[2])
async def step1(message: types.Message, state=FSMContext):
    if db.user_regist(user_id=message.from_user.id):
        await state.set_state(Acheiver.step1)
        await message.answer(msg.achiever1, reply_markup=kb.achiever1)
    else:
        await state.clear()
        await message.answer('Сначала тебе нужно зарегистрироваться :)', reply_markup=kb.start)


@router.message(Acheiver.step1, F.text.in_([kb.achiever_titles[1], kb.achiever_titles[2]]))
async def step2(message: types.Message, state=FSMContext):
    await state.set_state(Acheiver.step2)
    await message.answer(msg.achiever2, reply_markup=kb.achiever2)


@router.message(Acheiver.step2, F.text.in_([kb.achiever_titles[3], kb.achiever_titles[4]]))
async def step3(message: types.Message, state=FSMContext):
    await state.set_state(Acheiver.step3)
    await message.answer(msg.achiever3, reply_markup=kb.achiever3)


@router.message(Acheiver.step3, F.text.in_([kb.achiever_titles[5], kb.achiever_titles[6]]))
async def step4(message: types.Message, state=FSMContext):
    await state.set_state(Acheiver.step4)
    await message.answer(msg.achiever4, reply_markup=kb.achiever4)


@router.message(Acheiver.step4, F.text.in_([kb.achiever_titles[7], kb.achiever_titles[8]]))
async def step4(message: types.Message, state=FSMContext):
    await state.set_state(Acheiver.goal)
    await message.answer(msg.achiever5, reply_markup=ReplyKeyboardRemove())


@router.message(Acheiver.goal)
async def step4(message: types.Message, state=FSMContext):
    data = await state.update_data(goal=message.text)
    db.add_goal(user_id=message.from_user.id,
                goal=data['goal'])
    await state.clear()
    await message.answer(msg.achiever6)
    await message.answer(msg.achiever7, reply_markup=kb.start)
