from bot.database.methods import *
from bot.misc.util import CHARACTERS
import secrets


def get_select(key, table: str = "user", cell: str = "*", name_input_key: str = "u_id") -> None:
    """
    1 функция для получения значений из БД
    :param key:   Уникальный ключ (u_id)
    :param table: Таблица откуда будем брать
    :param cell:  Значение которое хотим полуить
    :param name_input_key: Название колонки

    :return: Значение из БД
    """
    with sq.connect(PATH_BAZE) as con:
        cur = con.cursor()
        res = cur.execute(f"SELECT {cell} FROM {table} WHERE {name_input_key} = ?", (key,))
        return res.fetchall()


def get_language(u_id):
    # Получаем информацию о реферальной ссылки
    return get_select(u_id, "users", "language")[0][0]


def in_db_dl(dl):
    # Проверяем наличие реферальной ссылки в базе
    return get_select(dl, "invitation_links", "*", "code_links") != []


def get_dl(dl):
    # Получаем информацию о реферальной ссылки
    return get_select(dl, "invitation_links", "*", "code_links")[0]


def generate_unique_code(length=6):
    # Генерируем случайную строку указанной длины
    code = ''.join(secrets.choice(CHARACTERS) for _ in range(length))
    return code


def is_code_unique(code):
    with sq.connect(PATH_BAZE) as con:
        # Проверяем, есть ли код в базе данных
        cursor = con.execute("SELECT COUNT(*) FROM data_user WHERE unique_code = ?", (code,))
        count = cursor.fetchone()[0]
        return count == 0


def get_unique_code(length=6):
    while True:
        code = generate_unique_code(length)
        if is_code_unique(code):
            return code


def get_unblock_time(u_id):
    return get_select(u_id, "users", "unblock_time")[0][0]
