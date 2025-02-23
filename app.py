import logging
from aiogram import Bot, Dispatcher, executor
from handlers import start, parkent_village, common
from loader import bot, dp
from data.config import ADMINS
from utils.set_bot_commands import set_default_commands
from handlers import start, parkent_village, common

async def on_startup(dispatcher):
    """Bot ishga tushganda bajariladigan amallar."""
    logging.info("Bot ishga tushmoqda...")
    # Bot buyruqlarini o‘rnatish
    await set_default_commands(dispatcher)

    # Adminlarga xabar yuborish (agar adminlar bo‘lsa)
    if ADMINS:
        for admin in ADMINS:
            try:
                await bot.send_message(admin, "✅ *Бот ишга тушди!*", parse_mode="Markdown")
            except Exception as e:
                logging.error(f"Admin {admin} ga xabar yuborishda xatolik: {e}")

async def on_shutdown(dispatcher):
    """Bot to‘xtaganda bajariladigan amallar."""
    logging.info("Bot to‘xtamoqda...")

    # Adminlarga xabar yuborish (agar adminlar bo‘lsa)
    if ADMINS:
        for admin in ADMINS:
            try:
                await bot.send_message(admin, "⚠️ *Bot to‘xtadi!*", parse_mode="Markdown")
            except Exception as e:
                logging.error(f"Admin {admin} ga xabar yuborishda xatolik: {e}")

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
