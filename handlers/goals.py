from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from data.texts import t
from services.user_service import get_language
from services.goal_service import set_goal, get_goals_summary

router = Router()

GOAL_VALUES = {
    "daily": [5, 10, 20],
    "weekly": [25, 50, 100],
    "monthly": [100, 200, 500],
}


def _goals_keyboard(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t("btn_goal_daily", lang), callback_data="goal:daily")],
        [InlineKeyboardButton(text=t("btn_goal_weekly", lang), callback_data="goal:weekly")],
        [InlineKeyboardButton(text=t("btn_goal_monthly", lang), callback_data="goal:monthly")],
        [InlineKeyboardButton(text=t("btn_back_menu", lang), callback_data="back:menu")],
    ])


@router.callback_query(F.data == "menu:goals")
async def on_goals_menu(callback: CallbackQuery) -> None:
    await callback.answer()
    user_id = callback.from_user.id
    lang = get_language(user_id)

    summary = get_goals_summary(user_id)
    lines = [t("goals_menu", lang), ""]
    for period in ("daily", "weekly", "monthly"):
        g = summary[period]
        period_name = t(f"period_{period}", lang)
        if g["target"] > 0:
            lines.append(t("goal_progress", lang, period=period_name, done=g["done"], target=g["target"]))
        else:
            lines.append(f"{period_name}: --")

    await callback.message.edit_text(
        "\n".join(lines), reply_markup=_goals_keyboard(lang)
    )


@router.callback_query(F.data.startswith("goal:"))
async def on_goal_period(callback: CallbackQuery) -> None:
    await callback.answer()
    user_id = callback.from_user.id
    lang = get_language(user_id)
    period = callback.data.split(":")[1]

    if period not in GOAL_VALUES:
        return

    period_name = t(f"period_{period}", lang)
    values = GOAL_VALUES[period]
    buttons = [
        [InlineKeyboardButton(text=str(v), callback_data=f"goalset:{period}:{v}")]
        for v in values
    ]
    buttons.append([InlineKeyboardButton(text=t("btn_back_menu", lang), callback_data="menu:goals")])
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)

    await callback.message.edit_text(
        t("goal_pick_value", lang, period=period_name), reply_markup=kb
    )


@router.callback_query(F.data.startswith("goalset:"))
async def on_goal_set(callback: CallbackQuery) -> None:
    await callback.answer()
    user_id = callback.from_user.id
    lang = get_language(user_id)

    try:
        parts = callback.data.split(":")
        period = parts[1]
        target = int(parts[2])
    except (IndexError, ValueError):
        return

    set_goal(user_id, period, target)
    period_name = t(f"period_{period}", lang)

    back_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t("btn_back_menu", lang), callback_data="back:menu")],
    ])
    await callback.message.edit_text(
        t("goal_set", lang, period=period_name, target=target), reply_markup=back_kb
    )
