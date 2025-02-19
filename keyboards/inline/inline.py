from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def start_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Parkent Village", callback_data="parkent_village"))
    keyboard.add(InlineKeyboardButton("Lakeside Residence", callback_data="lakeside_residence"))
    return keyboard

def parkent_main_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Тайёр кадастрли хонадонлар", callback_data="parkent_village_ready"))
    keyboard.add(InlineKeyboardButton("Битказилаётган хонадонлар", callback_data="parkent_village_under_construction"))
    keyboard.add(InlineKeyboardButton("Фото лавҳалар", callback_data="parkent_village_gallery"))
    keyboard.add(InlineKeyboardButton("Жойлашув 🌍", callback_data="parkent_village_location"))
    keyboard.add(InlineKeyboardButton("⬅️ Орқага", callback_data='main_menu'))
    keyboard.add(InlineKeyboardButton("🏠 Бош сахифа", callback_data="main_menu"))
    return keyboard

def parkent_ready_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton("Субсидия асосида сотиб олиш", callback_data="subsidya_ready"))
    keyboard.add(InlineKeyboardButton("100%лик тўлов асосида сотиб олиш", callback_data="full_payment_ready"))
    keyboard.add(InlineKeyboardButton("⬅️ Орқага", callback_data="parkent_village"))
    keyboard.add(InlineKeyboardButton("🏠 Бош сахифа", callback_data="main_menu"))
    return keyboard

def parkent_under_construction_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Бошлангич тўлов асосида сотиб олиш:", callback_data="subsidya_under_construction"))
    keyboard.add(InlineKeyboardButton("100%лик тўлов асосида сотиб олиш", callback_data="full_payment_under_construction"))
    keyboard.add(InlineKeyboardButton("⬅️ Орқага", callback_data="parkent_village"))
    keyboard.add(InlineKeyboardButton("🏠 Бош сахифа", callback_data="main_menu"))
    return keyboard

def subsidya_ready_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("2 хонали хонадон", callback_data="subsidya_2_rooms_ready"))
    keyboard.add(InlineKeyboardButton('3 хонали хонадон', callback_data='subsidya_3_rooms_ready'))
    keyboard.add(InlineKeyboardButton("⬅️ Орқага", callback_data="parkent_village_ready"))
    keyboard.add(InlineKeyboardButton("🏠 Бош сахифа", callback_data="main_menu"))
    return keyboard

def full_payment_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("2 хонали хонадон", callback_data="full_payment_2_rooms_ready"))
    keyboard.add(InlineKeyboardButton('3 хонали хонадон', callback_data='full_payment_3_rooms_ready'))
    keyboard.add(InlineKeyboardButton("⬅️ Орқага", callback_data="parkent_village_ready"))
    keyboard.add(InlineKeyboardButton("🏠 Бош сахифа", callback_data="main_menu"))
    return keyboard


def subsidya_under_construction_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("2 хонали хонадон", callback_data="subsidya_2_rooms_under_construction"))
    keyboard.add(InlineKeyboardButton("3 хонали хонадон", callback_data="subsidya_3_rooms_under_construction"))
    keyboard.add(InlineKeyboardButton("⬅️ Орқага", callback_data="parkent_village_under_construction"))
    keyboard.add(InlineKeyboardButton("🏠 Бош сахифа", callback_data="main_menu"))
    return keyboard

def full_payment_under_construction_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("2 хонали хонадон", callback_data="full_payment_2_rooms_under_construction"))
    keyboard.add(InlineKeyboardButton("3 хонали хонадон", callback_data="full_payment_3_rooms_under_construction"))
    keyboard.add(InlineKeyboardButton("⬅️ Орқага", callback_data="parkent_village_under_construction"))
    keyboard.add(InlineKeyboardButton("🏠 Бош сахифа", callback_data="main_menu"))
    return keyboard


def lakeside_main_keyboard():
    """Lakeside Residence asosiy menyusi tugmalari."""
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("Сотиб олиш учун", callback_data="lakeside_residence_under_construction"),
        InlineKeyboardButton("Фото лавҳалар", callback_data="lakeside_residence_gallery"),
        InlineKeyboardButton("Жойлашув 🌍", callback_data="lakeside_residence_location"),
        InlineKeyboardButton("⬅️ Орқага", callback_data="main_menu"),
        InlineKeyboardButton("🏠 Бош сахифа", callback_data="main_menu"),
    )
    return keyboard


def lakeside_purchase_options():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("100%лик тўлов асосида сотиб олиш", callback_data="full_payment_lakeside"),
        InlineKeyboardButton("5%лик чегирма асосида сотиб олиш", callback_data="discount_payment_lakeside"),
        InlineKeyboardButton("Кредит асосида сотиб олиш", callback_data="credit_payment_lakeside"),
        InlineKeyboardButton("⬅️ Орқага", callback_data="lakeside_residence"),
        InlineKeyboardButton("🏠 Бош сахифа", callback_data="main_menu"),
    )
    return keyboard


def create_payment_options(prefix: str) -> InlineKeyboardMarkup:
    """Turli to'lov turlari uchun tugmalar yaratadi."""
    options = [
        ("56.98", "2 хонали хонадон"),
        ("57.49", "3 хонали хонадон"),
        ("62.00", "2 хонали хонадон"),
        ("80.26", "3 хонали хонадон"),
        ("83.57", "3 хонали хонадон"),
        ("87.94", "3 хонали хонадон"),
    ]

    keyboard = InlineKeyboardMarkup(row_width=1)

    for size, rooms in options:
        callback_data = f"{prefix}_{size.replace('.', '_')}"
        keyboard.add(InlineKeyboardButton(f"🏗 {size} m² - {rooms}", callback_data=callback_data))

    keyboard.add(InlineKeyboardButton("⬅️ Орқага", callback_data="lakeside_residence_under_construction"))
    keyboard.add(InlineKeyboardButton("🏠 Бош сахифа", callback_data="main_menu"))
    return keyboard

def full_payment_options() -> InlineKeyboardMarkup:
    return create_payment_options("full_payment")

def discount_payment_options() -> InlineKeyboardMarkup:
    return create_payment_options("discount")

def credit_payment_options() -> InlineKeyboardMarkup:
    return create_payment_options("credit")
# def full_payment_options():
#     keyboard = InlineKeyboardMarkup(row_width=1)
#     keyboard.add(
#         InlineKeyboardButton("🏗 56.98 m² - 2 xona", callback_data="full_payment_1_rooms"),
#         InlineKeyboardButton("🏗 57.49 m² - 2 xona", callback_data="full_payment_2_rooms"),
#         InlineKeyboardButton("🏗 62.00 m² - 2 xona", callback_data="full_payment_3_rooms"),
#         InlineKeyboardButton("🏗 80.26 m² - 3 xona", callback_data="full_payment_4_rooms"),
#         InlineKeyboardButton("🏗 83.57 m² - 3 xona", callback_data="full_payment_5_rooms"),
#         InlineKeyboardButton("🏗 87.94 m² - 3 xona", callback_data="full_payment_6_rooms"),
#         InlineKeyboardButton("⬅️ Orqaga", callback_data="main_menu")
#     )
#     return keyboard
#
#
# def discount_payment_options():
#     keyboard = InlineKeyboardMarkup(row_width=1)
#     keyboard.add(
#         InlineKeyboardButton("🏗 56.98 m² - 2 xona", callback_data="discount_1_rooms"),
#         InlineKeyboardButton("🏗 57.49 m² - 2 xona", callback_data="discount_2_rooms"),
#         InlineKeyboardButton("🏗 62.00 m² - 2 xona", callback_data="discount_3_rooms"),
#         InlineKeyboardButton("🏗 80.26 m² - 3 xona", callback_data="discount_4_rooms"),
#         InlineKeyboardButton("🏗 83.57 m² - 3 xona", callback_data="discount_5_rooms"),
#         InlineKeyboardButton("🏗 87.94 m² - 3 xona", callback_data="discount_6_rooms"),
#         InlineKeyboardButton("⬅️ Orqaga", callback_data="main_menu")
#     )
#     return keyboard
#
#
# def credit_payment_options():
#     keyboard = InlineKeyboardMarkup(row_width=1)
#     keyboard.add(
#         InlineKeyboardButton("💳 Kredit shartlari haqida", callback_data="credit_terms"),
#         InlineKeyboardButton("🏗 56.98 m² - 2 xona", callback_data="credit_1_rooms"),
#         InlineKeyboardButton("🏗 57.49 m² - 2 xona", callback_data="credit_2_rooms"),
#         InlineKeyboardButton("🏗 62.00 m² - 2 xona", callback_data="credit_3_rooms"),
#         InlineKeyboardButton("🏗 80.26 m² - 3 xona", callback_data="credit_4_rooms"),
#         InlineKeyboardButton("🏗 83.57 m² - 3 xona", callback_data="credit_5_rooms"),
#         InlineKeyboardButton("🏗 87.94 m² - 3 xona", callback_data="credit_6_rooms"),
#         InlineKeyboardButton("⬅️ Orqaga", callback_data="main_menu")
#     )
#     return keyboard