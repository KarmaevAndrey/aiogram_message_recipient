from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from bot.misc.util import MY_BOT, IS_FIRST_MESSAGE_TO_SET_FILL_DESCRIPTION
from bot.handlers.main import register_all_handlers
from bot.filters import register_all_filters

from bot.misc import *
from bot.utils.set_me import set_me


async def in_start(bot: Bot):
    # if IS_FIRST_MESSAGE_TO_SET_FILL_DESCRIPTION:
    await set_me(bot)
    print(f"✅ Бот {MY_BOT} запущен")


async def in_stop():
    print(f"❌ Бот {MY_BOT} остановлен")


async def start_bot():
    bot = Bot(token=TgKeys.TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.startup.register(in_start)
    dp.shutdown.register(in_stop)
    register_all_handlers(dp)
    register_all_filters(dp)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
