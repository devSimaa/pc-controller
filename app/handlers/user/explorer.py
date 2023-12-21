from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, Command
from loader import dp
from app.keyboards.inline_keyboard import explorer_listdir
import os
from pathlib import Path

current_directory = Path(os.getcwd()) 

@dp.message_handler(Text("explorer"))
@dp.message_handler(Command("explorer"))
async def explorer_command(message: types.Message):
    files_in_directory = os.listdir(current_directory)
    await message.answer(f"{current_directory}",
                         reply_markup= await explorer_listdir(files_in_directory))

@dp.callback_query_handler(Text(endswith="explorer_back"))
async def explorer_back(callback: types.CallbackQuery):
    global current_directory
    
    current_directory = current_directory.parents[0]
    files_in_directory = os.listdir(current_directory)
    await callback.message.edit_text(current_directory,reply_markup=await explorer_listdir(files_in_directory))


@dp.callback_query_handler(Text(endswith="_file"))
async def explorer_file(callback: types.CallbackQuery):
    global current_directory
    file = callback.data.replace('_file', '')
    if "." in file:
        if os.name == 'nt':
            os.system(f'start {current_directory}\{file}')
        elif os.name == 'posix':
            os.system(f'xdg-open {current_directory}\{file}')
        await callback.answer(f"{file} with open")
    else:
        current_directory = current_directory.joinpath(file)
        files_in_directory = os.listdir(current_directory)
        await callback.message.edit_text(current_directory,reply_markup=await explorer_listdir(files_in_directory))
