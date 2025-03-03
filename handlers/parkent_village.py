import asyncio
import json
import logging
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from keyboards.inline.inline import (
    credit_ready_keyboard, parkent_main_keyboard, parkent_ready_keyboard,
    subsidya_ready_keyboard, full_payment_keyboard,
    parkent_under_construction_keyboard, subsidya_under_construction_keyboard, full_payment_under_construction_keyboard,
)
from states.states import Form
from aiogram.types import InputFile



@dp.callback_query_handler(lambda c: c.data == "parkent_village", state="*")
async def parkent_main(call: types.CallbackQuery, state: FSMContext):
    """Parkent Village haqida ma'lumot beruvchi asosiy menyu."""
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="*Parkent Village - турар жой мажмуаси Тошкент вилояти Паркент тумани "
        "«Сой» МФЙ Тамбалак кўчаси ҳудудида жойлашган бўлиб, ушбу мажмуада "
        "5 қаватли турар уй-жой бинолари мавжуд.*",
        reply_markup=parkent_main_keyboard(),
        parse_mode="Markdown"
    )
    await state.set_state(Form.PARKENT_MAIN.state)


@dp.callback_query_handler(lambda c: c.data == "parkent_village_ready", state="*")
async def parkent_ready(call: types.CallbackQuery, state: FSMContext):
    """Tayyor uylar haqida ma'lumot beruvchi menyu."""
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="*Тайёр кадастрли хонадонлар:*",
        parse_mode="Markdown",
        reply_markup=parkent_ready_keyboard()
    )
    await Form.PARKENT_READY.set()

@dp.callback_query_handler(lambda c: c.data == "parkent_village_under_construction", state="*")
async def parkent_under_construction(call: types.CallbackQuery, state: FSMContext):
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="*Битказилаётган хонадонлар ҳақида маълумот:*",
        parse_mode="Markdown",
        reply_markup=parkent_under_construction_keyboard()
    )
    await Form.PARKENT_UNDER_CONSTRUCTION.set()

@dp.callback_query_handler(lambda c: c.data == "parkent_village_gallery", state=Form.PARKENT_MAIN)
async def send_parkent_gallery(call: types.CallbackQuery, state: FSMContext):
    """Фото галарея bosilganda JSON'dagi barcha rasmlarni guruh bo‘lib yuborish."""
    await call.answer()

    try:
        with open("image_path.json", "r", encoding="utf-8") as file:
            IMAGE_PATHS = json.load(file)

        media_group = []
        message_ids = []  # Yuborilgan xabar ID'larini saqlash

        for key, image_path in IMAGE_PATHS.items():
            if key.startswith("parkent"):
                try:
                    photo = types.InputFile(image_path)
                    media_group.append(types.InputMediaPhoto(photo))
                except Exception as e:
                    logging.error(f"Rasm yuklashda xatolik: {e}")

        if media_group:
            messages = await bot.send_media_group(chat_id=call.message.chat.id, media=media_group)
            message_ids.extend([msg.message_id for msg in messages])  # Rasmlar ID larini saqlash

        # Inline tugmalar bilan rasmni qo'shib matn yuborish
        menu_msg = await bot.send_message(
            chat_id=call.message.chat.id,
            text="📸 *Фото лавхалар* 🏡",
            parse_mode="Markdown",
            reply_markup=parkent_main_keyboard()
        )

        message_ids.append(menu_msg.message_id)  # Tugmalar xabarining ID sini ham saqlaymiz
        await state.update_data(gallery_messages=message_ids)

    except Exception as e:
        logging.error(f"JSON faylni o'qishda xatolik: {e}")


@dp.callback_query_handler(lambda c: c.data == "parkent_village_location", state=Form.PARKENT_MAIN)
async def send_parkent_location(call: types.CallbackQuery, state: FSMContext):
    """Parkent Village joylashuvini yuborish."""
    await call.answer()
    location = {
        'latitude': 41.300889,
        'longitude': 69.696638
    }

    location_msg = await bot.send_location(
        chat_id=call.message.chat.id,
        latitude=location['latitude'],
        longitude=location['longitude']
    )

    menu_msg = await bot.send_message(
        chat_id=call.message.chat.id,
        text="📍 *Parkent village - жойлашуви*",
        parse_mode="Markdown",
        reply_markup=parkent_main_keyboard()
    )

    await state.update_data(location_messages=[location_msg.message_id, menu_msg.message_id])


import logging
logging.basicConfig(level=logging.INFO)

@dp.callback_query_handler(lambda c: c.data == "subsidya_ready", state=Form.PARKENT_READY)
async def subsidya_ready_info(call: types.CallbackQuery, state: FSMContext):
    logging.info("subsidya_ready tugmasi bosildi")
    await call.answer()

    message_text = "*Субсидия асосида сотиб олиш:*"
    await call.message.edit_text(
        text=message_text,
        parse_mode="Markdown",
        reply_markup=subsidya_ready_keyboard()
    )


@dp.callback_query_handler(lambda c: c.data == "full_payment_ready", state=Form.PARKENT_READY)
async def full_payment_ready_info(call: types.CallbackQuery, state: FSMContext):
    """100%лик тўлов асосида сотиб олиш tugmasi bosilganda ishlaydi."""
    await call.answer()

    message_text = "*💰 100% тўлов асосида сотиб олиш:*"

    await call.message.edit_text(
        text=message_text,
        parse_mode="Markdown",
        reply_markup=full_payment_keyboard()
    )

async def update_photo(call, photo_path, caption_text, markup):
    """Xabarni rasm yoki matnga qarab yangilash."""
    if call.message.photo:
        try:
            photo = types.InputMediaPhoto(media=types.InputFile(photo_path), caption=caption_text, parse_mode="Markdown")
            await call.message.edit_media(photo, reply_markup=markup)
        except Exception:
            pass
    else:
        try:
            await bot.send_photo(
                chat_id=call.message.chat.id,
                photo=InputFile(photo_path),
                caption=caption_text,
                parse_mode="Markdown",
                reply_markup=markup,
            )
            await call.message.delete()
        except Exception:
            pass

@dp.callback_query_handler(lambda c: c.data == "subsidya_2_rooms_ready", state=Form.PARKENT_READY)
async def subsidya_2_rooms(call: types.CallbackQuery, state: FSMContext):
    """2 хонали хонадон (Субсидия асосида) rasmni yuborish yoki yangilash."""
    await call.answer()

    photo_path = "images/2xonaSubsidiya.jpg"
    caption_text = "🏠 *2 хонали хонадон*"

    # Inline tugmalarni saqlash
    markup = subsidya_ready_keyboard()

    if call.message.photo:
        # Agar xabar allaqachon rasm bo‘lsa, rasmni yangilaymiz
        try:
            photo = types.InputMediaPhoto(media=types.InputFile(photo_path), caption=caption_text, parse_mode="Markdown")
            await call.message.edit_media(photo, reply_markup=markup)
        except Exception:
            pass  # Xatolik yuz bersa, davom etamiz
    else:
        # Agar xabar matn bo‘lsa, uni rasmga almashtiramiz
        try:
            await bot.send_photo(
                chat_id=call.message.chat.id,
                photo=InputFile(photo_path),
                caption=caption_text,
                parse_mode="Markdown",
                reply_markup=markup,  # Tugmalarni qayta qo‘shamiz
            )
            await call.message.delete()  # Eski xabarni o‘chiramiz
        except Exception:
            pass


@dp.callback_query_handler(lambda c: c.data == "subsidya_3_rooms_ready", state=Form.PARKENT_READY)
async def subsidya_3_rooms(call: types.CallbackQuery, state: FSMContext):
    """3 хонали хонадон (Субсидия асосида) rasmni yuborish yoki yangilash."""
    await call.answer()

    photo_path = "images/3xonaSubsidiya.jpg"
    caption_text = "🏠 *3 хонали хонадон*"

    markup = subsidya_ready_keyboard()

    if call.message.photo:
        try:
            photo = types.InputMediaPhoto(media=types.InputFile(photo_path), caption=caption_text, parse_mode="Markdown")
            await call.message.edit_media(photo, reply_markup=markup)
        except Exception:
            pass
    else:
        try:
            await bot.send_photo(
                chat_id=call.message.chat.id,
                photo=InputFile(photo_path),
                caption=caption_text,
                parse_mode="Markdown",
                reply_markup=markup,
            )
            await call.message.delete()
        except Exception:
            pass


# @dp.callback_query_handler(lambda c: c.data == "full_payment_2_rooms_ready", state=Form.PARKENT_READY)
# async def full_payment_2_rooms(call: types.CallbackQuery, state: FSMContext):
#     """2 хонали хонадон (100% тўлов) rasmni yuborish yoki yangilash."""
#     await call.answer()
#     await update_photo(call, "images/2xona100tayyor.jpg", "🏠 *2 хонали хонадон*", markup=full_payment_keyboard())
#
#
# @dp.callback_query_handler(lambda c: c.data == "full_payment_3_rooms_ready", state=Form.PARKENT_READY)
# async def full_payment_3_rooms(call: types.CallbackQuery, state: FSMContext):
#     """3 хонали хонадон (100% тўлов) rasmni yuborish yoki yangilash."""
#     await call.answer()
#     await update_photo(call, "images/3xona100tayyor.jpg", "🏠 *3 хонали хонадон*", full_payment_keyboard())


@dp.callback_query_handler(lambda c: c.data == "subsidya_under_construction", state=Form.PARKENT_UNDER_CONSTRUCTION)
async def subsidya_under_construction(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(
        "*Бошлангич тўлов асосида сотиб олиш учун хонадонлар:*",
        parse_mode="Markdown",
        reply_markup=subsidya_under_construction_keyboard()
    )


@dp.callback_query_handler(lambda c: c.data == "full_payment_under_construction", state=Form.PARKENT_UNDER_CONSTRUCTION)
async def full_payment_under_construction(call: types.CallbackQuery, state:FSMContext):
    await call.message.edit_text(
        "*100% тўлов асосида сотиб олиш учун хонадонлар:*",
        parse_mode="Markdown",
        reply_markup=full_payment_under_construction_keyboard()
    )


@dp.callback_query_handler(lambda c: c.data == "subsidya_2_rooms_under_construction", state=Form.PARKENT_UNDER_CONSTRUCTION)
async def subsidya_2_rooms_under_construction(call: types.CallbackQuery, state: FSMContext):
    """2 хонали хонадон (бошлангич тўлов асосида) rasmni yuborish yoki yangilash."""
    await call.answer()
    await update_photo(call, "images/2xonaboshlangich.jpg", "🏠 *2 хонали хонадон (бошлангич тўлов асосида)*", subsidya_under_construction_keyboard())


@dp.callback_query_handler(lambda c: c.data == "subsidya_3_rooms_under_construction", state=Form.PARKENT_UNDER_CONSTRUCTION)
async def subsidya_3_rooms_under_construction(call: types.CallbackQuery, state: FSMContext):
    """3 хонали хонадон (бошлангич тўлов асосида) rasmni yuborish yoki yangilash."""
    await call.answer()
    await update_photo(call, "images/3xonaboshlangich.jpg", "🏠 *3 хонали хонадон (бошлангич тўлов асосида)*", subsidya_under_construction_keyboard())


@dp.callback_query_handler(lambda c: c.data == "full_payment_2_rooms_under_construction", state=Form.PARKENT_UNDER_CONSTRUCTION)
async def full_payment_2_rooms_under_construction(call: types.CallbackQuery, state: FSMContext):
    """2 хонали хонадон (100% тўлов асосида) rasmni yuborish yoki yangilash."""
    await call.answer()
    await update_photo(call, "images/2xona100bitayotgan.jpg",
                       "💰 *2 хонали хонадон (100% тўлов асосида)*",
                       full_payment_under_construction_keyboard())


@dp.callback_query_handler(lambda c: c.data == "full_payment_3_rooms_under_construction", state=Form.PARKENT_UNDER_CONSTRUCTION)
async def full_payment_3_rooms_under_construction(call: types.CallbackQuery, state: FSMContext):
    """3 хонали хонадон (100% тўлов асосида) rasmni yuborish yoki yangilash."""
    await call.answer()
    await update_photo(call, "images/3xona100bitayotgan.jpg", "💰 *3 хонали хонадон (100% тўлов асосида)*", full_payment_under_construction_keyboard())


@dp.callback_query_handler(lambda c: c.data == "full_payment_2_rooms_ready", state=Form.PARKENT_READY)
async def full_payment_2_rooms(call: types.CallbackQuery, state: FSMContext):
    """2 хонали хонадон (100% тўлов) rasmni yuborish."""
    await call.answer()

    photo_path = "images/2xona1001.jpg"
    caption_text = "🏠 *2 хонали хонадон*"
    markup = full_payment_keyboard()

    if call.message.photo:
        try:
            photo = types.InputMediaPhoto(media=types.InputFile(photo_path), caption=caption_text, parse_mode="Markdown")
            await call.message.edit_media(photo, reply_markup=markup)
        except Exception:
            pass
    else:
        try:
            await bot.send_photo(
                chat_id=call.message.chat.id,
                photo=InputFile(photo_path),
                caption=caption_text,
                parse_mode="Markdown",
                reply_markup=markup,
            )
            await call.message.delete()
        except Exception:
            pass


@dp.callback_query_handler(lambda c: c.data == "full_payment_3_rooms_ready", state=Form.PARKENT_READY)
async def full_payment_3_rooms(call: types.CallbackQuery, state: FSMContext):
    """3 хонали хонадон (100% тўлов) rasmni yuborish."""
    await call.answer()


    photo_path = "images/3xona1001.jpg"
    caption_text = "🏠 *3 хонали хонадон*"
    markup = full_payment_keyboard()

    if call.message.photo:
        try:
            photo = types.InputMediaPhoto(media=types.InputFile(photo_path), caption=caption_text, parse_mode="Markdown")
            await call.message.edit_media(photo, reply_markup=markup)
        except Exception:
            pass
    else:
        try:
            await bot.send_photo(
                chat_id=call.message.chat.id,
                photo=InputFile(photo_path),
                caption=caption_text,
                parse_mode="Markdown",
                reply_markup=markup,
            )
            await call.message.delete()
        except Exception:
            pass


@dp.callback_query_handler(lambda c: c.data == "credit_ready", state=Form.PARKENT_READY)
async def credit_ready_info(call: types.CallbackQuery, state: FSMContext):
    """Кредит асосда сотиб олиш tugmasi bosilganda ishlaydi."""
    await call.answer()

    message_text = "*💳 Кредит асосда сотиб олиш учун маълумот:*"

    await call.message.edit_text(
        text=message_text,
        parse_mode="Markdown",
        reply_markup=credit_ready_keyboard()  # Yangi tugmalar qatori
    )

@dp.callback_query_handler(lambda c: c.data == "credit_2_rooms_ready", state=Form.PARKENT_READY)
async def credit_2_rooms(call: types.CallbackQuery, state: FSMContext):
    """2 хонали хонадон (Кредит асосда) rasmni yuborish yoki yangilash."""
    await call.answer()

    photo_path = "images/2xonakreditt.jpg"  # Yangi rasm manzili
    caption_text = "🏠 *2 хонали хонадон (Кредит асосида)*"
    markup = credit_ready_keyboard()

    if call.message.photo:
        try:
            photo = types.InputMediaPhoto(media=types.InputFile(photo_path), caption=caption_text, parse_mode="Markdown")
            await call.message.edit_media(photo, reply_markup=markup)
        except Exception:
            pass
    else:
        try:
            await bot.send_photo(
                chat_id=call.message.chat.id,
                photo=InputFile(photo_path),
                caption=caption_text,
                parse_mode="Markdown",
                reply_markup=markup,
            )
            await call.message.delete()
        except Exception:
            pass


@dp.callback_query_handler(lambda c: c.data == "credit_3_rooms_ready", state=Form.PARKENT_READY)
async def credit_3_rooms(call: types.CallbackQuery, state: FSMContext):
    """3 хонали хонадон (Кредит асосида) rasmni yuborish yoki yangilash."""
    await call.answer()

    photo_path = "images/3xonakreditt.jpg"  # Yangi rasm manzili
    caption_text = "🏠 *3 хонали хонадон (Кредит асосда)*"
    markup = credit_ready_keyboard()

    if call.message.photo:
        try:
            photo = types.InputMediaPhoto(media=types.InputFile(photo_path), caption=caption_text, parse_mode="Markdown")
            await call.message.edit_media(photo, reply_markup=markup)
        except Exception:
            pass
    else:
        try:
            await bot.send_photo(
                chat_id=call.message.chat.id,
                photo=InputFile(photo_path),
                caption=caption_text,
                parse_mode="Markdown",
                reply_markup=markup,
            )
            await call.message.delete()
        except Exception:
            pass