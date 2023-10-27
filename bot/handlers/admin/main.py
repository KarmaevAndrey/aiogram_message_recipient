import asyncio

from aiogram import Dispatcher
from aiogram import F
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command, CommandObject
from bot.database.methods import PATH_BAZE
from bot.database.models.user import MyUser
from bot.misc.env import *
from bot.misc.util import langs, BOT_VERSION
import bot.database as db
from bot.utils.remaining_time import remaining_time

loop = asyncio.get_event_loop()


def register_admin_handlers(dp: Dispatcher):
    dp.message.register(i_not_admin, F.from_user.id.not_in({MAIN_ADMIN_ID}) & (F.text.in_({"/v", "/send_baze", "/cmd", "create_ref", "ban"})))
    dp.message.register(admin_cmd, F.from_user.id.in_({MAIN_ADMIN_ID}), Command("cmd"))
    dp.message.register(send_baze, F.from_user.id.in_({MAIN_ADMIN_ID}), Command("send_baze"))
    dp.message.register(send_version, F.from_user.id.in_({MAIN_ADMIN_ID}), Command("v"))
    dp.message.register(ban_user, F.from_user.id.in_({MAIN_ADMIN_ID}), Command("ban"))
    dp.message.register(create_ref, F.from_user.id.in_({MAIN_ADMIN_ID}), Command("create_ref"))
    # dp.message.register(ban_user, Command("ban"))


async def admin_cmd(msg: Message):
    cmd = """
/send_baze - отправить базу\n\n
/v - версия бота\n\n
/ban - забанить пользователя\n\n
/create_ref - создать рефералку
"""
    await msg.answer(cmd)


async def i_not_admin(msg: Message):
    # Если пользователь нажал на команду админа, без должных прав
    await msg.answer(langs[MyUser(msg.from_user.id).language]["error_no_license"])


async def send_baze(msg: Message):
    await msg.answer_document(FSInputFile(PATH_BAZE))


async def send_version(msg: Message):
    await msg.answer(BOT_VERSION)


async def ban_user(msg: Message):
    args = msg.text.split()
    if len(args) == 4:
        u_id = int(args[1])
        time = ' '.join(args[2:])
        try:
            db.set_ban(u_id, time)
            time = remaining_time(time)
            if time[0]:
                await msg.answer(f"✅ Получилось, вы забанили {u_id} на дней: {time[1][0]}, часов {time[1][1]}, мин {time[1][2]}")
            else:
                await msg.answer(f"✅ Получилось, вы разабанили {u_id}")
        except Exception as e:
            await msg.answer(f"❌ Используйте команду так: /ban user_id block_duration \n(/ban 123 31.12.2023 23.59)\n\nОшибка:\n{e}")
    else:
        await msg.answer("❌ Используйте команду так: /ban user_id block_duration \n(/ban 123 31.12.2023 23.59)")


async def create_ref(msg: Message):
    args = msg.text.split()
    if len(args) > 2:
        main_name = args[1]
        description = ' '.join(args[2:])
        db.create_ref_url(main_name, description)
        await msg.answer(f"✅ Получилось -> https://t.me/{MY_BOT}?start={main_name}")
    else:
        await msg.answer("❌ Используйте команду так: /create_ref имя описание \n(/ban ytb трафик с youtube)")
