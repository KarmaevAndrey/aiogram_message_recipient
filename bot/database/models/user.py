import json
import time

from aiogram import html
from aiogram.enums import ParseMode
from bot.misc.util import MAIN_ADMIN_ID
import bot.database as bd
from bot.misc.util import send_special_id, language_cach, MY_BOT, ALL_LANGUAGE_CODES
from bot.utils.remaining_time import remaining_time


class MyUser:
    def __init__(self, u_id, username: str = None, first_name: str = None, last_name: str = None,
                 first_language: str = None, connection_time: str = None, level: int = None,
                 operations_done: int = None, info: str = None, now_use: int = None, qr_parameters: str = None):
        self.u_id: int = u_id
        self.username: str = username
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.first_language: str = first_language
        self.connection_time: str = connection_time
        self.level: int = level
        self.operations_done: int = operations_done
        self.info: str = info
        self.now_use: int = now_use
        self.qr_parameters: str = qr_parameters

    def add_user(self, msg):
        # Добавление пользователя НУЖНО ПРОПИСАТЬ все поля
        connection_time = time.strftime('%H:%M %d.%m.%Y')
        user_info = (self.u_id, f"@{str(msg.username)}", str(msg.first_name), str(msg.last_name), str(self.language),
                     str(msg.language_code), connection_time, 0, 1, "30.10.2017 10.10")
        bd.main_set_select("users", *user_info)

    @property
    def language(self):
        # Получаем и сохраняем в language_cach язык пользователя
        if self.u_id in language_cach:
            return language_cach[self.u_id]
        elif not self.is_new:
            language = bd.get_language(self.u_id)
            language_cach[self.u_id] = language
            return language
        else:
            if self.first_language in ALL_LANGUAGE_CODES:
                language_cach[self.u_id] = self.first_language
                return self.first_language
        language_cach[self.u_id] = "en"
        return "en"

    @property
    def is_new(self):
        """
        Пользовался ли user ботом или заблокировал
        :return: True - да, False - нет
        """
        try:
            if bd.get_select(self.u_id, "users", "now_use")[0][0] != 1:
                return True
            return False
        except Exception:
            return True

    def is_blocked_bot(self):
        """
        Пользовался ли user ботом И заблокировал
        :return: True - да, False - нет
        """
        try:
            if bd.get_select(self.u_id, "users", "now_use")[0][0] == 0:
                return True
            return False
        except Exception:
            return False

    @property
    def path_cash(self):
        return str(self.u_id % 10 + self.u_id // 10 % 10 + self.u_id // 100 % 10)

    def get_premium(self):
        data = bd.get_select(self.u_id, "users", "qr_parameters")[0][0]
        return json.loads(data)

    def have_premium(self):
        """
        У user есть премиум?
        :return: True - да, False - нет
        """
        return bd.get_select(self.u_id, "users", "level")[0][0] == 1

    async def user_have_avatar(self, msg):
        photos = await msg.from_user.get_profile_photos()
        return photos.photos != []

    def in_ban(self):
        try:
            if bd.get_select(self.u_id, "users", "now_use")[0][0] == 1:
                return remaining_time(bd.get_unblock_time(self.u_id))
            return [False]
        except Exception:
            return [False]


async def reg_new_user(my_user: MyUser, msg, bot, ref_url=None) -> None:
    #  Регистрация пользователя + отправка уведомления
    if send_special_id:
        special_id = f'<a href="tg://user?id={my_user.u_id}">Id:</a> {html.code(my_user.u_id)}'
    else:
        special_id = f'<Id: {html.code(my_user.u_id)}'
    admin_msg = f"""❗ NEW USER: @{str(msg.username)}
       First name: {msg.first_name}
       Last name: {msg.last_name}
       {special_id}
       First language: {html.bold(msg.language_code)}
       Bot: @{MY_BOT}"""
    if not (ref_url is None):
        info_dl = bd.get_dl(ref_url)
        admin_msg += f"""\nℹ️  Deep linking info: 
       Description: {html.bold(info_dl[1])}
       Quantity of visitors: {html.underline(info_dl[2])}
    """
        bd.main_cpp(ref_url, "invitation_links", "come_number", "code_links")
        bd.main_add(my_user.u_id, ref_url, "invitation_links", "who_switched", "code_links")

    if my_user.is_blocked_bot():
        admin_msg += html.bold("\n       I come back 😎")
        bd.main_update_value(1, my_user.u_id, "users", "now_use", "now_use")
        await bot.send_message(MAIN_ADMIN_ID, admin_msg, parse_mode=ParseMode.HTML)
        return
    await bot.send_message(MAIN_ADMIN_ID, admin_msg, parse_mode=ParseMode.HTML)
    my_user.add_user(msg)
