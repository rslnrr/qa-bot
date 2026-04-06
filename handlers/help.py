from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from data.texts import t
from services.user_service import get_language

router = Router()


def _help_kb(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t("btn_back_menu", lang), callback_data="back:menu")],
    ])


@router.message(Command("help"))
async def cmd_help(message: Message) -> None:
    lang = get_language(message.from_user.id)
    await message.answer(t("help_text", lang), reply_markup=_help_kb(lang))


@router.callback_query(F.data == "menu:help")
async def on_help(callback: CallbackQuery) -> None:
    await callback.answer()
    lang = get_language(callback.from_user.id)
    await callback.message.edit_text(t("help_text", lang), reply_markup=_help_kb(lang))
