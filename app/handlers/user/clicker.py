from aiogram import types, Dispatcher
from loader import dp, bot
from keyboards import clicker_ikb


# кликер
@dp.message_handler(text="♾ Кликер")
async def clicker(message: types.Message):
    await message.answer(
        text=f"⚙️ Меню кликера",
        reply_markup=clicker_ikb(),
    )


# @dp.callback_query_handler(text=["Включение кликера", "Выключение кликера"])
# async def clicker_callback(callback: types.CallbackQuery):
#     if callback.data == "Включение кликера":
#         await callback.answer("Кликер включен")
#         setclicker(1)
#     elif callback.data == "Выключение кликера":
#         await callback.answer("Кликер выключен")
#         setclicker(0)
