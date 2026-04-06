import logging

from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton

from data.texts import t
from services.user_service import get_language, get_user

logger = logging.getLogger(__name__)

router = Router()

# In-memory feedback storage
_feedback: list[dict] = []


@router.callback_query(F.data == "menu:feedback")
async def on_feedback_menu(callback: CallbackQuery) -> None:
    await callback.answer()
    user_id = callback.from_user.id
    lang = get_language(user_id)
    get_user(user_id)["awaiting_feedback"] = True
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t("btn_back_menu", lang), callback_data="back:menu")],
    ])
    await callback.message.edit_text(t("feedback_prompt", lang), reply_markup=kb)


async def handle_feedback_message(message: Message) -> bool:
    """Check if user is sending feedback. Returns True if handled."""
    user_id = message.from_user.id
    user = get_user(user_id)

    if not user.get("awaiting_feedback"):
        return False

    user["awaiting_feedback"] = False
    lang = get_language(user_id)

    # Store feedback
    _feedback.append({
        "user_id": user_id,
        "text": message.text,
    })
    logger.info("Feedback from user %s: %s", user_id, message.text)

    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t("btn_back_menu", lang), callback_data="back:menu")],
    ])
    await message.answer(t("feedback_thanks", lang), reply_markup=kb)
    return True
