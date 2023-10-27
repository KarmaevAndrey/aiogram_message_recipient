import pathlib
import sys

from aiogram import Dispatcher
from aiogram import F, Bot
from aiogram.types import ContentType
from aiogram.types import Message
from bot.database.models.user import MyUser
import bot.database as db
from bot.misc.util import MAIN_ADMIN_ID
import bot.utils.all_state as my_states

script_dir = pathlib.Path(sys.argv[0]).parent
PATH_USER_PHOTO = str(script_dir / 'bot/media/cash/from_user_{}_photo.jpg')


def register_all_media(dp: Dispatcher) -> None:
    # Регистрация всех, всех handlers на медиа
    # Если медиа отправил админ
    dp.message.register(get_text_admin, F.from_user.id.in_({MAIN_ADMIN_ID}) & F.content_type == ContentType.TEXT)
    dp.message.register(get_photo_admin, F.from_user.id.in_({MAIN_ADMIN_ID}) & F.content_type == ContentType.PHOTO)
    dp.message.register(get_video_admin, F.from_user.id.in_({MAIN_ADMIN_ID}) & F.content_type == ContentType.VIDEO)
    dp.message.register(get_document_admin, F.from_user.id.in_({MAIN_ADMIN_ID}) & F.content_type == ContentType.DOCUMENT)
    dp.message.register(get_sticker_admin, F.from_user.id.in_({MAIN_ADMIN_ID}) & F.content_type == ContentType.STICKER)
    dp.message.register(get_animation_admin, F.from_user.id.in_({MAIN_ADMIN_ID}) & F.content_type == ContentType.ANIMATION)
    dp.message.register(get_voice_admin, F.from_user.id.in_({MAIN_ADMIN_ID}) & F.content_type == ContentType.VOICE)
    # Если медиа отправил пользователь
    dp.message.register(get_text, F.content_type == ContentType.TEXT)
    dp.message.register(get_photo, F.content_type == ContentType.PHOTO)
    dp.message.register(get_video, F.content_type == ContentType.VIDEO)
    dp.message.register(get_document, F.content_type == ContentType.DOCUMENT)
    dp.message.register(get_sticker, F.content_type == ContentType.STICKER)
    dp.message.register(get_animation, F.content_type == ContentType.ANIMATION)
    dp.message.register(get_voice, F.content_type == ContentType.VOICE)


async def get_text(msg: Message, bot: Bot):
    # Если медиа == текст
    my_user = MyUser(msg.from_user.id)
    u_text = msg.text
    db.save_user_data(my_user, u_text, None, "TEXT")
    await bot.send_message(MAIN_ADMIN_ID, u_text + f"\n\n#<code>{my_user.u_id}</code>")


async def get_photo(msg: Message, bot: Bot):
    # Если медиа == фото
    file = await bot.get_file(msg.photo[-1].file_id)
    file_id = file.file_id
    my_user = MyUser(msg.from_user.id)
    db.save_user_data(my_user, None, file_id, "PHOTO")
    await bot.send_photo(MAIN_ADMIN_ID, file_id, caption=f"#<code>{my_user.u_id}</code>")


async def get_video(msg: Message, bot: Bot):
    file_id = msg.video.file_id
    my_user = MyUser(msg.from_user.id)
    db.save_user_data(my_user, None, file_id, "VIDEO")
    await bot.send_video(MAIN_ADMIN_ID, file_id, caption=f"#<code>{my_user.u_id}</code>")


async def get_document(msg: Message, bot: Bot):
    file_id = msg.document.file_id
    my_user = MyUser(msg.from_user.id)
    db.save_user_data(my_user, None, file_id, "DOCUMENT")
    await bot.send_document(MAIN_ADMIN_ID, file_id, caption=f"#<code>{my_user.u_id}</code>")


async def get_sticker(msg: Message, bot: Bot):
    file_id = msg.sticker.file_id
    my_user = MyUser(msg.from_user.id)
    db.save_user_data(my_user, None, file_id, "STICKER")
    msg_id = await bot.send_sticker(MAIN_ADMIN_ID, file_id)
    await bot.send_message(MAIN_ADMIN_ID, f"#<code>{my_user.u_id}</code>", reply_to_message_id=msg_id.message_id)


async def get_animation(msg: Message, bot: Bot):
    file_id = msg.animation.file_id
    my_user = MyUser(msg.from_user.id)
    db.save_user_data(my_user, None, file_id, "ANIMATION")
    msg_id = await bot.send_animation(MAIN_ADMIN_ID, file_id)
    await bot.send_message(MAIN_ADMIN_ID, f"#<code>{my_user.u_id}</code>", reply_to_message_id=msg_id.message_id)


async def get_voice(msg: Message, bot: Bot):
    file_id = msg.voice.file_id
    my_user = MyUser(msg.from_user.id)
    db.save_user_data(my_user, None, file_id, "VOICE")
    try:
        msg_id = await bot.send_voice(chat_id=MAIN_ADMIN_ID, voice=file_id)
        await bot.send_message(MAIN_ADMIN_ID, f"#<code>{my_user.u_id}</code>", reply_to_message_id=msg_id.message_id)
    except Exception:
        await bot.send_message(MAIN_ADMIN_ID, f"ОТКЛЮЧИ ОГРАНИЧЕНИЯ НА ОТПРАВКУ ГОЛОСОВЫХ, ИЛИ ДОБАВЬ БОТА В КОНТАКТЫ")


async def get_text_admin(msg: Message, state: my_states.FSMContext):
    await state.update_data(text=msg.text)
    await msg.answer("Отправьте ID получателя")
    await state.set_state(my_states.GetTextAdmin.id_send_text.state)


async def get_photo_admin(msg: Message, state: my_states.FSMContext):
    await state.update_data(photo=msg.photo[-1].file_id)
    await msg.answer("Отправьте ID получателя")
    await state.set_state(my_states.GetPhotoAdmin.id_send_photo.state)


async def get_video_admin(msg: Message, state: my_states.FSMContext):
    await state.update_data(video=msg.video.file_id)
    await msg.answer("Отправьте ID получателя")
    await state.set_state(my_states.GetVideoAdmin.id_send_video.state)


async def get_document_admin(msg: Message, state: my_states.FSMContext):
    await state.update_data(document=msg.document.file_id)
    await msg.answer("Отправьте ID получателя")
    await state.set_state(my_states.GetDocumentAdmin.id_send_document.state)


async def get_sticker_admin(msg: Message, state: my_states.FSMContext):
    await state.update_data(sticker=msg.sticker.file_id)
    await msg.answer("Отправьте ID получателя")
    await state.set_state(my_states.GetStickerAdmin.id_send_sticker.state)


async def get_animation_admin(msg: Message, state: my_states.FSMContext):
    await state.update_data(animation=msg.animation.file_id)
    await msg.answer("Отправьте ID получателя")
    await state.set_state(my_states.GetAnimationAdmin.id_send_animation.state)


async def get_voice_admin(msg: Message, state: my_states.FSMContext):
    await state.update_data(voice=msg.voice.file_id)
    await msg.answer("Отправьте ID получателя")
    await state.set_state(my_states.GetVoiceAdmin.id_send_voice.state)
