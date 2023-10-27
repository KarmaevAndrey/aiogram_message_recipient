from .main import register_all_my_filters
from aiogram import Dispatcher


def register_all_filters(dp: Dispatcher) -> None:
    handlers = (
        register_all_my_filters,
    )
    for handler in handlers:
        handler(dp)
