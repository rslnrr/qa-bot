from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from data.texts import t
from services.user_service import get_language, get_user

router = Router()


def _menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t("btn_quiz", lang), callback_data="menu:quiz")],
        [InlineKeyboardButton(text=t("btn_profile", lang), callback_data="menu:profile")],
        [
            InlineKeyboardButton(text=t("btn_goals", lang), callback_data="menu:goals"),
            InlineKeyboardButton(text=t("btn_pets", lang), callback_data="menu:pets"),
        ],
        [InlineKeyboardButton(text=t("btn_feedback", lang), callback_data="menu:feedback")],
        [
            InlineKeyboardButton(text=t("btn_change_lang", lang), callback_data="menu:change_lang"),
            InlineKeyboardButton(text=t("btn_help", lang), callback_data="menu:help"),
        ],
    ])


def _clear_awaiting(user_id: int) -> None:
    """Clear any 'awaiting input' flags when returning to menu."""
    user = get_user(user_id)
    user["awaiting_open_answer"] = False
    user["awaiting_feedback"] = False


async def send_main_menu(message: Message, user_id: int) -> None:
    """Send the main menu as a NEW message. Called from other handlers."""
    _clear_awaiting(user_id)
    lang = get_language(user_id)
    await message.answer(t("main_menu", lang), reply_markup=_menu_keyboard(lang))


async def edit_main_menu(message: Message, user_id: int) -> None:
    """Edit an existing message to show the main menu."""
    _clear_awaiting(user_id)
    lang = get_language(user_id)
    await message.edit_text(t("main_menu", lang), reply_markup=_menu_keyboard(lang))


@router.callback_query(F.data == "back:menu")
async def on_back_menu(callback: CallbackQuery) -> None:
    await callback.answer()
    await edit_main_menu(callback.message, callback.from_user.id)
