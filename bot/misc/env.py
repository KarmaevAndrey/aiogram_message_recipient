from os import environ
from typing import Final
from bot.misc.util import *


class TgKeys:
    # Переменные окружения
    if MY_BOT == "msg_rpt_bot":
        TOKEN: Final = environ.get('MAIN_TOKEN')
    else:
        TOKEN: Final = environ.get('TEST_TOKEN')
