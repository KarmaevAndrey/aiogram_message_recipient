from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.database.models.user import MyUser
from bot.misc.util import langs


def example_inline_builder(my_user: MyUser):
    # Создание inline кнопок (не используется)
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text=langs[my_user.language]["example_inline_text"],
        callback_data=f"callback_data_123")
    )
    builder.add(InlineKeyboardButton(
        text=langs[my_user.language]["example_inline_url"],
        url="https://mastergroosha.github.io/aiogram-3-guide/filters-and-middlewares/")
    )

    builder.adjust(1)
    return builder
