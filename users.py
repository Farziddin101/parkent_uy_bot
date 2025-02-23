import json
from aiogram import types

USER_DATA_FILE = "users.json"

# Foydalanuvchini JSON faylga saqlash
def save_user(user: types.User):
    try:
        try:
            with open(USER_DATA_FILE, "r", encoding="utf-8") as f:
                users = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            users = []

        new_user = {
            "id": user.id,
            "full_name": user.full_name,
            "username": user.username or "Noma'lum"
        }

        if not any(u["id"] == new_user["id"] for u in users):
            users.append(new_user)
            with open(USER_DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(users, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Foydalanuvchini saqlashda xatolik: {e}")

# Barcha foydalanuvchilarni olish
def get_all_users():
    try:
        with open(USER_DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
