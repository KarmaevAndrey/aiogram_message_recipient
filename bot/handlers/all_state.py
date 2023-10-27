import pathlib
import sys

from aiogram import Bot
from aiogram import Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from bot.misc.util import MAIN_ADMIN_ID
import bot.utils.all_state as my_states

script_dir = pathlib.Path(sys.argv[0]).parent
PATH_USER_PHOTO = str(script_dir / 'bot/media/cash/from_user_{}_photo.jpg')


def register_all_state(dp: Dispatcher) -> None:
    # Регистрация всех state для отправки пользователям нужное сообщение
    dp.message.register(state_text_admin, my_states.GetTextAdmin.id_send_text)
    dp.message.register(state_photo_admin, my_states.GetPhotoAdmin.id_send_photo)
    dp.message.register(state_video_admin, my_states.GetVideoAdmin.id_send_video)
    dp.message.register(state_document_admin, my_states.GetDocumentAdmin.id_send_document)
    dp.message.register(state_sticker_admin, my_states.GetStickerAdmin.id_send_sticker)
    dp.message.register(state_animation_admin, my_states.GetAnimationAdmin.id_send_animation)
    dp.message.register(state_voice_admin, my_states.GetVoiceAdmin.id_send_voice)


async def state_text_admin(msg: Message, bot: Bot, state: FSMContext):
    user_data = await state.get_data()
    test = user_data["text"]
    await state.clear()
    try:
        await bot.send_message(msg.text, test)
    except Exception:
        await bot.send_message(MAIN_ADMIN_ID,
                               "❌ Не получилось отправить сообщение, проверьте ID пользователя или попробуйте заново.\n"
                               "Если сообщение продолжит не отпросятся то вероятнее всего пользователь заблокировал бота")


async def state_photo_admin(msg: Message, bot: Bot, state: FSMContext):
    user_data = await state.get_data()
    photo_file_id = user_data["photo"]
    await state.clear()
    try:
        await bot.send_photo(msg.text, photo_file_id)
    except Exception:
        await bot.send_message(MAIN_ADMIN_ID,
                               "❌ Не получилось отправить сообщение, проверьте ID пользователя или попробуйте заново.\n"
                               "Если сообщение продолжит не отпросятся то вероятнее всего пользователь заблокировал бота")


async def state_video_admin(msg: Message, bot: Bot, state: FSMContext):
    user_data = await state.get_data()
    video_file_id = user_data["video"]
    await state.clear()
    try:
        await bot.send_video(msg.text, video_file_id)
    except Exception:
        await bot.send_message(MAIN_ADMIN_ID,
                               "❌ Не получилось отправить сообщение, проверьте ID пользователя или попробуйте заново.\n"
                               "Если сообщение продолжит не отпросятся то вероятнее всего пользователь заблокировал бота")


async def state_document_admin(msg: Message, bot: Bot, state: FSMContext):
    user_data = await state.get_data()
    document_file_id = user_data["document"]
    await state.clear()
    try:
        await bot.send_document(msg.text, document_file_id)
    except Exception:
        await bot.send_message(MAIN_ADMIN_ID,
                               "❌ Не получилось отправить сообщение, проверьте ID пользователя или попробуйте заново.\n"
                               "Если сообщение продолжит не отпросятся то вероятнее всего пользователь заблокировал бота")


async def state_sticker_admin(msg: Message, bot: Bot, state: FSMContext):
    user_data = await state.get_data()
    sticker_file_id = user_data["sticker"]
    await state.clear()
    try:
        await bot.send_sticker(msg.text, sticker_file_id)
    except Exception:
        await bot.send_message(MAIN_ADMIN_ID,
                               "❌ Не получилось отправить сообщение, проверьте ID пользователя или попробуйте заново.\n"
                               "Если сообщение продолжит не отпросятся то вероятнее всего пользователь заблокировал бота")


async def state_animation_admin(msg: Message, bot: Bot, state: FSMContext):
    user_data = await state.get_data()
    animation_file_id = user_data["animation"]
    await state.clear()
    try:
        await bot.send_animation(msg.text, animation_file_id)
    except Exception:
        await bot.send_message(MAIN_ADMIN_ID,
                               "❌ Не получилось отправить сообщение, проверьте ID пользователя или попробуйте заново.\n"
                               "Если сообщение продолжит не отпросятся то вероятнее всего пользователь заблокировал бота")


async def state_voice_admin(msg: Message, bot: Bot, state: FSMContext):
    user_data = await state.get_data()
    voice_file_id = user_data["voice"]
    await state.clear()
    try:
        await bot.send_animation(msg.text, voice_file_id)
    except Exception:
        await bot.send_message(MAIN_ADMIN_ID,
                               "❌ Не получилось отправить сообщение, проверьте ID пользователя или попробуйте заново.\n"
                               "Если сообщение продолжит не отпросятся то вероятнее всего пользователь заблокировал бота")
