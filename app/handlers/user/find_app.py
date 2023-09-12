from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from app.keyboards.keyboard import cancel_state
from windowsapps import open_app

class AppSearch(StatesGroup):
    search = State()

# создание профиля
@dp.message_handler(text='🗂 Поиск')
async def search_app(message: types.message):
    await message.reply("Набери название приложения которое хочешь открыть.", reply_markup=cancel_state())
    await AppSearch.search.set()




@dp.message_handler(state=AppSearch.search)
async def load_gender(message: types.Message, state=FSMContext):
    try:
        async with state.proxy() as data:
            data["search"] = message.text
            open_app(data["search"])
        await message.reply("Запущено")
            
    except Exception as e:
            await message.reply("Приложение не найдено")
            print(f"Ошибка при запуске приложения: {e}")


