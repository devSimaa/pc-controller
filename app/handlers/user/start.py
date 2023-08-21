from aiogram import types, Dispatcher
from loader import dp, bot
from keyboards import base_kb


# старт
@dp.message_handler(commands="start")
async def start_command(message: types.Message):
    await message.answer(
        text="Меню.",
        reply_markup=base_kb(),
    )
    await message.delete()
