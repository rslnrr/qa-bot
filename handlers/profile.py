from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from data.texts import t
from services.user_service import get_language, get_user
from services.pet_service import get_pet_display, get_active_pet

router = Router()


@router.callback_query(F.data == "menu:profile")
async def on_profile(callback: CallbackQuery) -> None:
    await callback.answer()
    user_id = callback.from_user.id
    lang = get_language(user_id)
    user = get_user(user_id)

    answered = user["questions_answered"]
    correct = user["correct_answers"]
    accuracy = round(correct / answered * 100) if answered else 0
    pet = get_pet_display(get_active_pet(user_id))
    badges = ", ".join(user["badges"]) if user["badges"] else "—"

    back_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t("btn_back_menu", lang), callback_data="back:menu")],
    ])

    await callback.message.edit_text(
        t(
            "profile", lang,
            score=user["score"],
            answered=answered,
            correct=correct,
            accuracy=accuracy,
            pet=pet,
            badges=badges,
        ),
        reply_markup=back_kb,
    )
