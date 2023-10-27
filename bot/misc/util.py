import string
import pytz

MY_BOT = "msg_rpt_bot"
BOT_VERSION = "BOT VERSION: 0.0.1"
IS_FIRST_MESSAGE_TO_SET_FILL_DESCRIPTION = True  # Изменить на true если нужно изменить описание бота
timezone = pytz.timezone('Europe/Moscow')
MAIN_ADMIN_ID = 912185600
ALL_LANGUAGE_CODES = ["ru", "en", "de"]
send_special_id = True  # Отправлять ссылку на акант пользователя через chat_id (! ВОЗМОЖНЫ ошибки)
language_cach = {}
CHARACTERS = string.ascii_lowercase + string.ascii_uppercase + string.digits
# резервирование спец символов (не используется)
for char_to_remove in "ABCDEFG":
    CHARACTERS = CHARACTERS.replace(char_to_remove, '')

ru_lang = {
    "edit_name": "Главное имя бота",
    "edit_about": "Описание вверху или при в предпросмотре ссылки",
    "edit_description": "Описание, которое видит пользователь даже не нажав /start",
    "edit_botpic": "Красивый QR-код",
    "edit_commands": {
        "start": "🚀 старт",
        "cmd": "📍 Команды для администратора"},

    "reply_keyboards_test_1": "1 кнопка",
    "reply_keyboards_test_2": "Пример state, введите текст:",
    "reply_keyboards_test_3": "пример клавиатуры",
    "example_inline_text": "пример",
    "example_inline_url": "ссылка",
    "cmd_start_already_using_bot": "Ты уже активировал бота",
    "cmd_start_first_using_bot": "1 сообщение после активации бота",

    "error_no_license": "❌ Недостаточно прав доступа",

    "MyName": "Получатель сообщений",
    "main_start_msg": "Привет, напиши мне сообщение и я его передам владельцу бота",
    "in_ban_msg": "⚠️ Сообщения не будут передаваться администратору ещё {} дней {} часа {} минуты"
}

en_lang = {
    "edit_name": "Bot's Main Name",
    "edit_about": "Description at the top or in the link preview",
    "edit_description": "Description that the user sees without even clicking /start",
    "edit_botpic": "Beautiful QR Code",
    "edit_commands": {
        "start": "🚀 start",
        "cmd": "📍 Commands for the administrator"
    },

    "reply_keyboards_test_1": "1 Button",
    "reply_keyboards_test_2": "Example state, enter text:",
    "reply_keyboards_test_3": "Keyboard example",
    "example_inline_text": "Example",
    "example_inline_url": "Link",
    "cmd_start_already_using_bot": "You've already activated the bot",
    "cmd_start_first_using_bot": "1 message after activating the bot",

    "error_no_license": "❌ Insufficient access rights",

    "MyName": "Message Recipient",
    "main_start_msg": "Hi, send me a message, and I will forward it to the bot owner",
    "in_ban_msg": "⚠️ Messages won't be forwarded to the administrator for another {} days {} hours {} minutes"
}

# Создания массива с разными языками
langs = {
    "ru": ru_lang,
    "en": ru_lang,
}
ALL_KEYBOARD = []  # словарь со всеми кнопками
for l in langs:
    ALL_KEYBOARD.append(langs[l]["reply_keyboards_test_1"])
    ALL_KEYBOARD.append(langs[l]["reply_keyboards_test_2"])
    ALL_KEYBOARD.append(langs[l]["reply_keyboards_test_3"])
