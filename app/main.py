from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.callback_data import CallbackData
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# мои скрипты
from config import token_api
from controler import (
    plus_dpi,
    minus_dpi,
    mouve_x_plus,
    mouve_x_minus,
    mouve_y_plus,
    mouve_y_minus,
    LKM,
    PKM,
)
from keyboard import (
    base_kb,
    clicker_ikb,
    screan_ikb,
    volume_ikb,
    controler_ikb,
    dpi_ikb,
    connect_ikb,
)

from create_folder import find_screandhots
import screanshot

# import hashlib


dpi = 15

storage = MemoryStorage()
bot = Bot(token_api)
dp = Dispatcher(
    bot=bot,
    storage=storage,
)


async def start_up(_):
    find_screandhots()
    print(" |<>| Бот запущен |<>| ")


# старт
@dp.message_handler(commands="start")
async def start_command(message: types.Message):
    await message.answer(
        text="Меню.",
        reply_markup=base_kb(),
    )
    await message.delete()


# ferfr
@dp.message_handler(text="🖥 Сделать скриншот")
async def screanshot_command(message: types.Message):
    screanshot.screen()
    await message.answer(
        text=f"Скриншот создан.\n Под именнем [ {screanshot.random_name} ]",
        reply_markup=screan_ikb(),
    )


@dp.callback_query_handler(text="Отправить скриншот")
async def clicker_callback(callback: types.CallbackQuery):
    path = f"./screanshots/{screanshot.random_name}"
    with open(path, "rb") as photo:
        await callback.bot.send_photo(
            chat_id=callback.message.chat.id,
            photo=photo,
        )


@dp.message_handler(text="♾ Кликер")
async def clicker(message: types.Message):
    await message.answer(
        text=f"⚙️ Меню кликера",
        reply_markup=clicker_ikb(),
    )


@dp.message_handler(text="🔊 Микшер громкости")
async def сom_vmixer(message: types.Message):
    await message.answer(
        text=f"🎚 Микшер громкости: ",
        reply_markup=volume_ikb(),
    )


@dp.message_handler(text="🕹 Контролер пк")
async def com_controler(message: types.Message):
    await message.answer(
        text=f"Чтоб подключиться к контролеру, нужно нажать на кнопку.",
        reply_markup=connect_ikb(),
    )


@dp.callback_query_handler(text=["connect"])
async def connect_callback(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=f"🕹 Контролер: \nЧувствительность курсора регулируеться пальцес в верх и низ.",
        reply_markup=controler_ikb(),
    )


@dp.callback_query_handler(text=["DPI"])
async def controler_callback(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=f"📝Редактирование:",
        reply_markup=dpi_ikb(),
    )


@dp.callback_query_handler(text=["c_up", "c_down", "c_left", "c_right"])
async def controler_x_y_callback(callback: types.CallbackQuery):
    if callback.data == "c_up":
        mouve_y_minus(dpi)
        await callback.answer(" Вверх")
    elif callback.data == "c_down":
        mouve_y_plus(dpi)
        await callback.answer(" Вниз")
    elif callback.data == "c_left":
        mouve_x_minus(dpi)
        await callback.answer(" Лево")

    elif callback.data == "c_right":
        mouve_x_plus(dpi)
        await callback.answer(" Право")


@dp.callback_query_handler(
    text=["c_left_button", "c_right_button", "c_plus", "c_minus", "c_wright"]
)
async def controler_x_y_callback(callback: types.CallbackQuery):
    global dpi
    if callback.data == "c_left_button":
        LKM()
        await callback.answer(" ЛКМ")

    elif callback.data == "c_right_button":
        PKM()
        await callback.answer(" ПКМ")

    elif callback.data == "c_plus":
        dpi = plus_dpi(dpi)
        await callback.answer(f"Теперь dpi [{dpi}]")

    elif callback.data == "c_minus":
        if dpi <= 15:
            await callback.answer(f"dpi уже на минимуме]")
        elif dpi > 15:
            dpi = minus_dpi(dpi)
            await callback.answer(f"Теперь dpi [{dpi}]")

    elif callback.data == "c_wright":
        await callback.answer(" Пока нету")


@dp.callback_query_handler(
    text=["d5", "d15", "d45", "d75", "d105", "d135", "d180", "d225", "d345"]
)
async def edit_dpi_callback(callback: types.CallbackQuery):
    global dpi
    if callback.data == "d5":
        dpi = 5
        await callback.answer(f"Теперь dpi [{dpi}]")
    elif callback.data == "d15":
        dpi = 15
        await callback.answer(f"Теперь dpi [{dpi}]")
    elif callback.data == "d45":
        dpi = 45
        await callback.answer(f"Теперь dpi [{dpi}]")
    elif callback.data == "d75":
        dpi = 75
        await callback.answer(f"Теперь dpi [{dpi}]")
    elif callback.data == "d105":
        dpi = 105
        await callback.answer(f"Теперь dpi [{dpi}]")
    elif callback.data == "d135":
        dpi = 135
        await callback.answer(f"Теперь dpi [{dpi}]")
    elif callback.data == "d180":
        dpi = 180
        await callback.answer(f"Теперь dpi [{dpi}]")
    elif callback.data == "d225":
        dpi = 225
        await callback.answer(f"Теперь dpi [{dpi}]")
    elif callback.data == "d345":
        dpi = 345
        await callback.answer(f"Теперь dpi [{dpi}]")


@dp.callback_query_handler(text=["Включение кликера", "Выключение кликера"])
async def clicker_callback(callback: types.CallbackQuery):
    global ggg
    if callback.data == "Включение кликера":
        ggg = True
    elif callback.data == "Выключение кликера":
        ggg = False


if __name__ == "__main__":
    executor.start_polling(
        dp,
        on_startup=start_up,
        skip_updates=True,
    )
