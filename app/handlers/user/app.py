from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from pathlib import Path
import os
import win32com.client

from loader import dp, bot
from app.others import screanshot
from app.keyboards.lnk_ikb import lnk
from data.config import DIR


lnk_path = Path(__file__).parents[3]

@dp.message_handler(text="🗂 Приложения")
async def comm_app(message: types.Message):
    screanshot.screen()
    await message.answer(
        text=f"Приложенния:",
        reply_markup=lnk(),
    )


@dp.callback_query_handler(Text(endswith=".lnk"))
async def open_app_callback(callback: types.CallbackQuery):
    await callback.answer(text=f"{callback.data} запущено")
    final_path = f"{DIR}\lnk\{callback.data}"

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(final_path)

    # Получаем путь к целевому файлу
    target_path = shortcut.Targetpath

    try:
        os.startfile(target_path)
    except Exception as e:
        print(f"Ошибка при запуске приложения: {e}")
