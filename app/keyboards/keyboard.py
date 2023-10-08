from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove,
)

def cancel_state():
    kb = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text="Выйти")
            ],
        ],
    )
    return kb


def base_kb():
    kb = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text="🖥 Сделать скриншот"),
                KeyboardButton(text="🔊 Микшер громкости")


            ],
            [
                KeyboardButton(text="🗂 Приложения"),
                KeyboardButton(text="🗂 Поиск")
            ],
            [
                KeyboardButton(text="🕹 Управление курсором"),
                # KeyboardButton(text="♾ Кликер"),
            ],
        ],
    )
    return kb
