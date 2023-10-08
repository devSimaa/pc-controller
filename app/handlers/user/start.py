from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart
from loader import dp, bot
from app.keyboards import base_kb


# старт
@dp.message_handler(CommandStart())
async def start_command(message: types.Message):
    await message.answer(
        text="Меню.",
        reply_markup=base_kb(),
    )
    await message.delete()
