from aiogram import types, Dispatcher
from loader import dp, bot
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from app.keyboards import clicker_ikb
from app.others.clicker import Cclicker


class Clicker_State(StatesGroup):
    on = State()
    off = State()


# кликер
@dp.message_handler(text="♾ Кликер")
async def clicker(message: types.Message):
    await message.answer(
        text=f"⚙️ Меню кликера",
        reply_markup=clicker_ikb(),
    )


@dp.callback_query_handler(text="clicker_on")
async def on_clicker(callback: types.CallbackQuery):
    await callback.answer("Кликер включен")

    await Clicker_State.on.set()
    # while True:
    Cclicker("on")


@dp.callback_query_handler(text="clicker_off")
async def off_clicker(callback: types.CallbackQuery):
    await callback.answer("Кликер выключен")
    await Clicker_State.off.set()
    Cclicker("off")


# @dp.callback_query_handler(text=["Включение кликера", "Выключение кликера"])
# async def clicker_callback(callback: types.CallbackQuery):
#     if callback.data == "Включение кликера":
#         await callback.answer("Кликер включен")
#         setclicker(1)
#     elif callback.data == "Выключение кликера":
#         await callback.answer("Кликер выключен")
#         setclicker(0)
