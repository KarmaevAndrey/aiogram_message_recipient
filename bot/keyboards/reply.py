from aiogram import Bot
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from bot.misc.util import *


async def menu(my_user, text_menu, bot: Bot):
    # Создание Reply кнопок (не используется)
    reply_keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=langs[my_user.language]["reply_keyboards_test_1"])],
        [KeyboardButton(text=langs[my_user.language]["reply_keyboards_test_2"])],
        [KeyboardButton(text=langs[my_user.language]["reply_keyboards_test_3"])]],
        resize_keyboard=True)
    await bot.send_message(my_user.u_id, text_menu, reply_markup=reply_keyboard)
