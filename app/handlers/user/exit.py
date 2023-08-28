from aiogram import types, Dispatcher
from loader import dp, bot
from aiogram.dispatcher import FSMContext


@dp.callback_query_handler(text="clicker_exit", state="*")
async def com_cancel(callback: types.CallbackQuery, state: FSMContext):
    if state is None:
        return
    await state.finish()
