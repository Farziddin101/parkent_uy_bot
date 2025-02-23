from aiogram import types, Dispatcher

async def set_default_commands(dp: Dispatcher):  # ✅ Aiogram 2.9 uchun Dispatcher qabul qilishi kerak
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Botni ishga tushirish"),
        types.BotCommand("help", "Yordam"),
        types.BotCommand("users", "Foydalanuvchilar soni"),

    ])
