from aiogram import Dispatcher
from aiogram import Bot
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.database.methods.get import in_db_dl
from bot.database.models.user import *
from bot.misc.util import langs


def register_user_handlers(dp: Dispatcher):
    # регистрация всех пользовательских команд
    # Пользователь нажал на старт c deep_linking с ref_url
    dp.message.register(cmd_start_handler_deep_linking_ref, CommandStart(deep_link=True))

    # Пользователь нажал на старт без deep_linking
    dp.message.register(cmd_start_handler, CommandStart())


async def cmd_start_handler(msg: Message, bot: Bot) -> None:
    # Пользователь нажал на старт без deep_linking
    my_user = MyUser(msg.from_user.id)
    if my_user.is_new:
        await reg_new_user(my_user, msg.from_user, bot)
        await msg.answer(langs[my_user.language]["cmd_start_first_using_bot"])
        return
    await msg.answer(langs[my_user.language]["cmd_start_already_using_bot"])


async def cmd_start_handler_deep_linking_ref(msg: Message, bot: Bot):
    # Пользователь нажал на старт c deep_linking с ref_url
    my_user = MyUser(msg.from_user.id)
    deep_linking = msg.text.split()[1]
    if my_user.is_new and in_db_dl(deep_linking):
        await reg_new_user(my_user, msg.from_user, bot, deep_linking)
        await msg.answer(langs[my_user.language]["cmd_start_first_using_bot"])
        return
    await msg.answer(langs[my_user.language]["cmd_start_already_using_bot"])
