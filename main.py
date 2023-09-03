from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.callback_data import CallbackData
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app import middlewares, filtres, handlers
from config import *
from loader import dp, bot


async def start_up(_):
    find_screandhots()
    print(" PC Controller-Bot | start ")


if __name__ == "__main__":
    executor.start_polling(
        dp,
        on_startup=start_up,
        skip_updates=True,
    )
