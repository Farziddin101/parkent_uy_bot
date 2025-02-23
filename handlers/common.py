from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from keyboards.inline.inline import start_keyboard
from states.states import Form
import logging
from keyboards.inline.inline import (parkent_main_keyboard, parkent_ready_keyboard, parkent_under_construction_keyboard,
    lakeside_main_keyboard, lakeside_purchase_options, full_payment_options, discount_payment_options, credit_payment_options
)

@dp.callback_query_handler(lambda c: c.data == "main_menu", state="*")
async def back_to_main_menu(call: types.CallbackQuery, state: FSMContext):
    """Bosh menyuga qaytganda rasmlar va tugmalar xabarlarini o‘chirib tashlash."""
    user_data = await state.get_data()
    message_ids = user_data.get("gallery_messages", [])
    data = await state.get_data()
    location_messages = data.get("location_messages", [])

    for msg_did in message_ids:
        try:
            await bot.delete_message(chat_id=call.message.chat.id, message_id=msg_did)
        except Exception as e:
            logging.error(f"Xabarni o‘chirishda xatolik: {e}")

    await state.update_data(gallery_messages=[])

    await bot.send_message(
        chat_id=call.message.chat.id,
        text="*Ушбу бот орқали сизга Тошкент "
        "вилоятининг Паркент туманидаги турар жой мажмуалари "
        "тўғрисида маълумот берилади.*",
        parse_mode="Markdown",
        reply_markup=start_keyboard()
    )
@dp.message_handler(content_types=types.ContentType.TEXT)
async def only_buttons(message: types.Message):
    await message.answer("❌ *Илтимос, тугмалардан фойдаланинг!*", parse_mode="Markdown")

