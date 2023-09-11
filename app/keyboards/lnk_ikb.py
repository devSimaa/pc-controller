from aiogram.types import (
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from app.others.lnk_control import get_file_list

lnk_list = get_file_list()
def lnk():
    ikb =  InlineKeyboardMarkup()
    for item in lnk_list:
        # print(item)
        b = InlineKeyboardButton(text=item, callback_data=f"{item}.lnk")
        ikb.add(b)
    return ikb
