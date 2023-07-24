from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove,
)


def base_kb():
    kb = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text="🖥 Сделать скриншот"),
            ],
            [
                KeyboardButton(text="🔊 Микшер громкости"),
            ],
            [
                KeyboardButton(text="🕹 Контролер пк"),
            ],
            [
                KeyboardButton(text="♾ Кликер"),
            ],
        ],
    )
    return kb
