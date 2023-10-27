from aiogram import Dispatcher
from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message
from bot.database.models.user import MyUser
from bot.misc.util import langs


def register_all_my_filters(dp: Dispatcher):
    # Регистрация всех фильтров
    dp.message.middleware(WeekendMessageMiddleware())


class WeekendMessageMiddleware(BaseMiddleware):
    # Фильтр на проверку, что пользователь не заблокирован
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        my_user = MyUser(event.from_user.id)
        info_in_not_ban = my_user.in_ban()
        if info_in_not_ban[0]:
            await event.answer(
                langs[my_user.language]["in_ban_msg"].format(*info_in_not_ban[1]),
                show_alert=True
            )
            return
        return await handler(event, data)
