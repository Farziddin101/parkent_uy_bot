from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command('help'), state="*")
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/users - Bot foydalanuvchilar soni",
            "/help - Yordam")

    await message.answer("\n".join(text))
