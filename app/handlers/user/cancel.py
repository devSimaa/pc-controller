from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from app.keyboards.keyboard import base_kb


@dp.message_handler(text="Выйти", state="*")
async def com_cancel(message: types.message, state: FSMContext):
    if state is None:
        return
    await state.finish()
    await message.answer("Вы вышли с поиска.",reply_markup=base_kb())
