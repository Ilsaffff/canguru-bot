from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram import types, Dispatcher
from attachments import messages as msg
from attachments import keyboards as kb


class SearchMentor(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()


async def step1(message: types.Message):
    await SearchMentor.step1.set()
    await message.answer(msg.search_mentor1, reply_markup=kb.search_mentor1)


async def step2(messsage: types.Message):
    await SearchMentor.next()
    await messsage.answer(msg.search_mentor2, reply_markup=kb.search_mentor2)


async def step3(messsage: types.Message):
    await SearchMentor.next()
    await messsage.answer(msg.search_mentor3, reply_markup=kb.search_mentor3)


async def finish(messsage: types.Message, state=FSMContext):
    await state.finish()
    await messsage.answer(msg.search_mentor4)
    await messsage.answer(msg.search_mentor5, reply_markup=kb.start)


def register_handler(dp: Dispatcher):
    dp.register_message_handler(step1, text='Поиск ментора', state=None)
    dp.register_message_handler(step2, text='Все понятно!', state=SearchMentor.step1)
    dp.register_message_handler(step3, text=['Ага, всё понятно!', 'Не-а, объясните ещё раз'], state=SearchMentor.step2)
    dp.register_message_handler(finish, text=['Интересно, сейчас изучу', 'Сделаю это позже'], state=SearchMentor.step3)
