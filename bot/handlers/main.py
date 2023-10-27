from aiogram import Dispatcher

from bot.handlers.admin.main import register_admin_handlers
from bot.handlers.all_state import register_all_state
from bot.handlers.media import register_all_media
from bot.handlers.user import register_user_handlers
from bot.handlers.user.callback import register_callback_handlers


def register_all_handlers(dp: Dispatcher) -> None:
    # Регистрация всех, всех handlers
    handlers = (
        register_admin_handlers,
        register_user_handlers,
        register_callback_handlers,
        register_all_state,
        register_all_media
    )
    for handler in handlers:
        handler(dp)
