from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp
from users import save_user, get_all_users
from keyboards.inline.inline import start_keyboard
from config import ADMINS


# /start komandasi
@dp.message_handler(Command("start"), state="*")
async def start(message: types.Message):
    print("✅ /start komandasi ishladi!")  # Konsolda tekshirish uchun

    save_user(message.from_user)  # Foydalanuvchini JSON faylga yozish
    await message.answer(
        "*Ассалому алайкум !\nУшбу бот орқали сизга Тошкент вилоятининг Паркент туманидаги турар жой мажмуалари тўғрисида маълумот берилади.*",
        parse_mode="Markdown",
        reply_markup=start_keyboard()  # Tugmalarni qo'shish
    )

# /users komandasi faqat adminlar uchun!
@dp.message_handler(Command("users"), state="*")
async def get_users(message: types.Message):
    user_id = message.from_user.id  # 👤 Foydalanuvchi ID sini olish

    if user_id not in ADMINS:  # 🔒 Agar foydalanuvchi admin bo'lmasa
        await message.answer("❌ Сизга бу буйруқдан фойдаланишга рухсат йўқ !")
        return

    users = get_all_users()

    if not users:
        await message.answer("👤  Ҳали ҳеч ким рўйхатдан ўтмаган..")
        return

    user_list = "\n".join([
        f"{u.get('full_name', 'Nomalum')} (@{u.get('username', 'Nomalum')}) (ID: <code>{u['id']}</code>)"
        for u in users
    ])

    response = f"👥 Умумий фойдаланувчилар сони: {len(users)}\n\n📜 Фойдаланувчилар рўйхати:\n{user_list}"
    
    await message.answer(response, parse_mode="HTML")
