from aiogram.fsm.state import StatesGroup, State


class GetTextAdmin(StatesGroup):
    text = State()
    id_send_text = State()


class GetPhotoAdmin(StatesGroup):
    id_send_photo = State()


class GetVideoAdmin(StatesGroup):
    id_send_video = State()


class GetDocumentAdmin(StatesGroup):
    id_send_document = State()


class GetStickerAdmin(StatesGroup):
    id_send_sticker = State()


class GetAnimationAdmin(StatesGroup):
    id_send_animation = State()


class GetVoiceAdmin(StatesGroup):
    id_send_voice = State()
