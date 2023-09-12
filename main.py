from aiogram import Bot, Dispatcher, executor
from app import middlewares, filters, handlers

from loader import dp, bot
from app.others.create_folder import create_folder

async def start_up(_):
    print(" PC Controller-Bot | start ")


if __name__ == "__main__":
    create_folder("screanshots")
    create_folder("lnk")

    executor.start_polling(
        dp,
        on_startup=start_up,
        skip_updates=True,
    )
