from bot.database.models.user import MyUser
from bot.database.methods import *


def main_set_select(table: str, *args) -> None:
    """
    Главная функция для добавления информации в БД


    :param table: Таблица куда будем добавлять
    :param args: Значение каждой ячейки
    :return: None
    """
    with sq.connect(PATH_BAZE) as con:
        placeholders = ', '.join(['?'] * len(args))
        sql_query = f"INSERT INTO {table} VALUES({placeholders})"
        con.executemany(sql_query, [args])


def main_update_value(new_value, key: str, table: str, cell: str, name_input_key: str) -> None:
    """
    Изменяем 1 значение

    Пример с изменением now_use на 1:

    Укажи новое значение new_value (1)
    Укажи уникальный параметр чтобы я мог найти нужный ряд (my_user.u_id)
    Укажи таблицу где я буду изменять значение (users)
    Укажи колонку где я буду изменять значение (now_use)
    Укажи колонку по которой я буду определять уникальное значение (u_id)

    main_update_value(1, my_user.u_id, "users", "now_use", "u_id")


    :param new_value Новое значение
    :param key:   Уникальный ключ (u_id)
    :param table: Таблица откуда будем брать
    :param cell:  Значение которое хотим изменить
    :param name_input_key: Название колонки для определения ряда
    :return: None
    """
    with sq.connect(PATH_BAZE) as con:
        sql_query = f"UPDATE {table} SET {cell} = ? WHERE {name_input_key} = ?"
        cur = con.cursor()
        cur.execute(sql_query, (new_value, key))


def main_cpp(key: str, table: str, cell: str, name_input_key: str) -> None:
    """
    Прибавляем к значению в ячейки 1 (для статистики)

    :param key:   Уникальный ключ (ref_url)
    :param table: Таблица откуда будем брать (invitation_links)
    :param cell:  Значение которое хотим обновить на 1 (come_number)
    :param name_input_key: Название колонки для ref_url (code_links)
    :return: None
    """

    c = get_select(key, table, cell, name_input_key)[0][0]
    main_update_value(c + 1, key, table, cell, name_input_key)


def main_add(new_value, key: str, table: str, cell: str, name_input_key: str) -> None:
    """
    Прибавляем к значению в ячейки 1 новое значение
    :param new_value: Значение которое добавляем
    :param key:   Уникальный ключ (ref_url)
    :param table: Таблица откуда будем брать (invitation_links)
    :param cell:  Значение которое хотим обновить (come_number)
    :param name_input_key: Название колонки для ref_url (code_links)
    :return: None
    """
    c = get_select(key, table, cell, name_input_key)[0][0]
    main_update_value(f"{c} {new_value}", key, table, cell, name_input_key)


def main_update(table: str, column_to_update: str, new_value, unique_column: str, unique_value) -> None:
    """
    Главная функция для обновления информации в БД

    :param table: Таблица, которую будем обновлять
    :param column_to_update: Столбец, который нужно обновить
    :param new_value: Новое значение для обновления
    :param unique_column: Столбец, содержащий уникальное значение (условие WHERE)
    :param unique_value: Уникальное значение для выборки записи, которую нужно обновить
    :return: None

    main_UPDATE("text_user", "photo_id", "новое_значение_photo_id", "unique_code", "значение_unique_code (tcROXe)")

    """
    with sq.connect(PATH_BAZE) as con:
        cursor = con.cursor()
        update_query = f"""
            UPDATE {table}
            SET {column_to_update} = ?
            WHERE {unique_column} = ?
        """

        cursor.execute(update_query, (new_value, unique_value))
        con.commit()


def save_user_data(my_user: MyUser, u_text, file_id, type_file):
    """
    Сохранение информации о тексте в таблицу data_user
    """
    user_id = my_user.u_id
    text = str(u_text)
    table_name = "data_user"
    unique_code = get_unique_code()
    datetime = time.strftime('%H:%M %d.%m.%Y')
    main_set_select(table_name, user_id, text, unique_code, datetime, file_id, type_file)


def set_ban(u_id: int, time: str):
    main_update_value(time, u_id, "users", "unblock_time", "u_id")
