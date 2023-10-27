from aiogram import Bot
from aiogram.types import BotCommand

from bot.misc.util import langs


async def set_my_commands(bot: Bot):
    cmd_ru = []
    cmd_en = []

    for name_cmd in langs["ru"]["edit_commands"]:
        cmd_ru.append(
            BotCommand(
                command=name_cmd,
                description=langs["ru"]["edit_commands"][name_cmd]
            )
        )
    for name_cmd in langs["en"]["edit_commands"]:
        cmd_en.append(
            BotCommand(
                command=name_cmd,
                description=langs["en"]["edit_commands"][name_cmd]
            )
        )

    await bot.set_my_commands(cmd_ru, language_code="ru")
    await bot.set_my_commands(cmd_en, language_code="en")


async def set_name_bot(bot: Bot):
    await bot.set_my_name(langs["en"]["edit_name"], language_code="en")
    await bot.set_my_name(langs["ru"]["edit_name"], language_code="ru")


async def set_description(bot: Bot):
    await bot.set_my_description(langs["ru"]["edit_description"], language_code="ru")
    await bot.set_my_description(langs["en"]["edit_description"], language_code="en")


async def set_short_description(bot: Bot):
    await bot.set_my_short_description(langs["ru"]["edit_about"], language_code="ru")
    await bot.set_my_short_description(langs["en"]["edit_about"], language_code="en")


async def set_me(bot: Bot):
    # вызов всех функций для изменения базовых значений на разных языках
    await set_my_commands(bot)
    await set_name_bot(bot)
    await set_description(bot)
    await set_short_description(bot)
