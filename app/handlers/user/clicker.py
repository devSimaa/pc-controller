from aiogram import types, Dispatcher
from loader import dp, bot

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

from app.keyboards.inline_keyboard import clicker_ikb
from app.others.clicker import Cclicker


class Clicker_State(StatesGroup):
    menu = State()
    on = State()
    off = State()


# кликер
@dp.message_handler(text="♾ Кликер")
async def clicker(message: types.Message):
    await Clicker_State.first()
    await message.answer(
        text=f"⚙️ Меню кликера",
        reply_markup=clicker_ikb(),
    )


@dp.callback_query_handler(text="clicker_on", state=Clicker_State)
async def on_clicker(callback: types.CallbackQuery, state=FSMContext):
    await callback.answer("Кликер включен")

    await Clicker_State.on.set()
    while True:
        Cclicker("on")


@dp.callback_query_handler(text="clicker_off", state=Clicker_State)
async def off_clicker(callback: types.CallbackQuery, state=FSMContext):
    await callback.answer("Кликер выключен")
    await Clicker_State.off.set()
    Cclicker("off")
