from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import types, Router
from attachments import messages as msg
from attachments import keyboards as kb
from aiogram.filters import Text
from aiogram import F

router = Router()


class SearchMentor(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()


@router.message(F.text == kb.start_titles[1])
async def step1(message: types.Message, state=FSMContext):
    await state.set_state(SearchMentor.step1)
    await message.answer(msg.search_mentor1, reply_markup=kb.search_mentor1)


@router.message(SearchMentor.step1, F.text == kb.search_mentor_titles[1])
async def step2(messsage: types.Message, state=FSMContext):
    await state.set_state(SearchMentor.step2)
    await messsage.answer(msg.search_mentor2, reply_markup=kb.search_mentor2)


@router.message(SearchMentor.step2, F.text.in_([kb.search_mentor_titles[2], kb.search_mentor_titles[3]]))
async def step3(messsage: types.Message, state=FSMContext):
    await state.set_state(SearchMentor.step3)
    await messsage.answer(msg.search_mentor3, reply_markup=kb.search_mentor3)


@router.message(SearchMentor.step3, F.text.in_([kb.search_mentor_titles[4], kb.search_mentor_titles[5]]))
async def step2(messsage: types.Message, state=FSMContext):
    await state.clear()
    await messsage.answer(msg.search_mentor5)
    await messsage.answer(msg.search_mentor4, reply_markup=kb.start)
