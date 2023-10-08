from aiogram.types import (
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


def clicker_ikb():
    ikb = InlineKeyboardMarkup(
        resize_keyboard=True,
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Вкл", callback_data="clicker_on"),
                InlineKeyboardButton(text="Выкл", callback_data="clicker_off"),
            ],
            [InlineKeyboardButton(text="Выйти", callback_data="clicker_exit")],
        ],
    )
    return ikb


def screan_ikb():
    ikb = InlineKeyboardMarkup(
        resize_keyboard=True,
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🖼 Отправить скриншот", callback_data="Отправить скриншот"
                ),
            ],
        ],
    )
    return ikb


def volume_ikb():
    ikb = InlineKeyboardMarkup(
        resize_keyboard=True,
        inline_keyboard=[
            [
                InlineKeyboardButton(text="+", callback_data="+1"),
                InlineKeyboardButton(text="+", callback_data="+2"),
                InlineKeyboardButton(text="+", callback_data="+3"),
                InlineKeyboardButton(text="+", callback_data="+4"),
            ],
            [
                InlineKeyboardButton(text="app", callback_data="app1"),
                InlineKeyboardButton(text="app", callback_data="app2"),
                InlineKeyboardButton(text="app", callback_data="app3"),
                InlineKeyboardButton(text="app", callback_data="app4"),
            ],
            [
                InlineKeyboardButton(text="-", callback_data="-1"),
                InlineKeyboardButton(text="-", callback_data="-2"),
                InlineKeyboardButton(text="-", callback_data="-3"),
                InlineKeyboardButton(text="-", callback_data="-4"),
            ],
        ],
    )
    return ikb


def controler_ikb():
    ikb = InlineKeyboardMarkup(
        resize_keyboard=True,
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✍🏻", callback_data="c_wright"),
                InlineKeyboardButton(text="👆🏻", callback_data="c_up"),
                InlineKeyboardButton(text="✋🏻", callback_data="c_right_button"),
            ],
            [
                InlineKeyboardButton(text="👈🏻", callback_data="c_left"),
                InlineKeyboardButton(text="🫵🏻", callback_data="c_left_button"),
                InlineKeyboardButton(text="👉🏻", callback_data="c_right"),
            ],
            [
                InlineKeyboardButton(text="👎🏻", callback_data="c_minus"),
                InlineKeyboardButton(text="👇🏻", callback_data="c_down"),
                InlineKeyboardButton(text="👍🏻", callback_data="c_plus"),
            ],
            [
                InlineKeyboardButton(text="DPI", callback_data="DPI"),
            ],
        ],
    )
    return ikb


def dpi_ikb():
    ikb = InlineKeyboardMarkup(
        resize_keyboard=True,
        inline_keyboard=[
            [
                InlineKeyboardButton(text="5", callback_data="d5"),
                InlineKeyboardButton(text="15", callback_data="d15"),
                InlineKeyboardButton(text="45", callback_data="d45"),
            ],
            [
                InlineKeyboardButton(text="75", callback_data="d75"),
                InlineKeyboardButton(text="105", callback_data="d105"),
                InlineKeyboardButton(text="135", callback_data="d135"),
            ],
            [
                InlineKeyboardButton(text="180", callback_data="d180"),
                InlineKeyboardButton(text="225", callback_data="d225"),
                InlineKeyboardButton(text="345", callback_data="d345"),
            ],
            [
                InlineKeyboardButton(text="Назад", callback_data="connect"),
            ],
        ],
    )
    return ikb


def connect_ikb():
    ikb = InlineKeyboardMarkup(
        resize_keyboard=True,
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Подключить", callback_data="connect"),
            ],
        ],
    )
    return ikb