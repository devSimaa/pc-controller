from aiogram import types, Dispatcher
from loader import dp, bot
from others import screanshot
from keyboards import screan_ikb


# скриншот
@dp.message_handler(text="🖥 Сделать скриншот")
async def screanshot_command(message: types.Message):
    screanshot.screen()
    await message.answer(
        text=f"Скриншот создан.\n Под именнем [ {screanshot.random_name} ]",
        reply_markup=screan_ikb(),
    )


@dp.callback_query_handler(text="Отправить скриншот")
async def clicker_callback(callback: types.CallbackQuery):
    path = f"{screanshot.path_screan}\{screanshot.random_name}"
    with open(path, "rb") as photo:
        await callback.bot.send_photo(
            chat_id=callback.message.chat.id,
            photo=photo,
        )
