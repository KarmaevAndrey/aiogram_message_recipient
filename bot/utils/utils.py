import pathlib
import sys

from aiogram import Bot
from aiogram.types import Message

from bot.database.models.user import MyUser

script_dir = pathlib.Path(sys.argv[0]).parent
PATH_USER_PHOTO = str(script_dir / 'bot/media/cash/from_user_{}_photo')


async def uploading_fils(my_user, path, msg: Message, bot: Bot):
    """
    Загружает любые фалы по заданому пути

    :param my_user: пользователь
    :param path: Путь
    :param msg: Объект класса Message
    :param bot: Объект класса Bot
    """
    if not (msg.photo is None):
        file = await bot.get_file(msg.photo[-1].file_id)
        path_to_uploading = f"{PATH_USER_PHOTO.format(my_user.path_cash)}.jpg"
        expansion = "jpg"
        await bot.download_file(file.file_path, path_to_uploading)
    else:
        expansion = msg.document.mime_type.split("/")[-1]
        file = await bot.get_file(msg.document.file_id)
        path_to_uploading = f"{PATH_USER_PHOTO.format(my_user.path_cash)}.{expansion}"
        await bot.download_file(file.file_path, path_to_uploading)
    return path_to_uploading, expansion


async def uploading_photos(my_user, msg: Message, bot: Bot):
    """
    Загружает фотографии (jpg, png, jpeg ...) по заданному пути

    :param my_user: пользователь
    :param msg: Объект класса Message
    :param bot: Объект класса Bot
    :return: Путь к загруженному изображению
    """

    path_to_uploading, expansion = await uploading_fils(my_user, PATH_USER_PHOTO, msg, bot)
    return path_to_uploading




async def get_last_user_avatar(msg: Message, bot: Bot):
    try:
        my_user = MyUser(msg.from_user.id)
        photos = await msg.from_user.get_profile_photos()
        file = await bot.get_file(photos.photos[-1][-1].file_id)
        path_to_uploading = f"{PATH_USER_PHOTO.format(my_user.path_cash)}.jpg"
        await bot.download_file(file.file_path, path_to_uploading)
        return path_to_uploading
    except Exception:
        return None
