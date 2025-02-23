import json
from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp
from config import ADMINS  # Admin ID larni import qilamiz

USER_DATA_FILE = "users.json"  # Foydalanuvchilar ro‘yxatini saqlash fayli

@dp.message_handler(Command("users"), state="*")
async def get_users(message: types.Message):
    admin_id = message.from_user.id  # Foydalanuvchi ID sini olamiz

    if admin_id not in ADMINS:  # 

        
        await message.answer("❌ Сизга бу буйруқдан фойдаланишга рухсат йўқ!")
        return

    try:
        with open(USER_DATA_FILE, "r", encoding="utf-8") as f:
            users = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        users = []

    if not users:
        await message.answer("👤 Ҳали ҳеч ким рўйхатдан ўтмаган.")
        return

    user_list = "\n".join([
        f"{u.get('full_name', 'Nomalum')} (@{u.get('username', 'Nomalum')}) (ID: <code>{u['id']}</code>)"
        for u in users
    ])

    response = f"👥 Умумий фойдаланувчилар сони: {len(users)}\n\n📜 Фойдаланувчилар рўйхати:\n{user_list}"
    
    await message.answer(response, parse_mode="HTML")
