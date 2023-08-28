from aiogram import types, Dispatcher
from loader import dp, bot
from app.keyboards.inline_keyboard import volume_ikb


# микшер
@dp.message_handler(text="🔊 Микшер громкости")
async def сom_vmixer(message: types.Message):
    await message.answer(
        text=f"🎚 Микшер громкости: ",
        reply_markup=volume_ikb(),
    )
