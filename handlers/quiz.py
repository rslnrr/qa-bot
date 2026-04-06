import logging

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from data.texts import t
from services.user_service import get_language, get_user, add_score, record_answer
from services.quiz_service import (
    start_quiz,
    get_current_question,
    check_mc_answer,
    check_open_answer,
    advance_quiz,
    get_quiz_results,
    end_quiz,
)
from services.goal_service import increment_progress, get_goal_bonus
from services.pet_service import get_active_pet, get_pet_display

logger = logging.getLogger(__name__)

router = Router()


def _back_menu_kb(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t("btn_back_menu", lang), callback_data="back:menu")],
    ])


def _results_keyboard(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t("btn_restart", lang), callback_data="menu:quiz")],
        [InlineKeyboardButton(text=t("btn_back_menu", lang), callback_data="back:menu")],
    ])


async def _send_question(message: Message, user_id: int) -> None:
    """Send the current question to the user."""
    lang = get_language(user_id)
    question = get_current_question(user_id)
    if question is None:
        return

    user = get_user(user_id)
    quiz = user["quiz"]
    current = quiz["current_index"] + 1
    total = len(quiz["questions"])

    # Header
    topic_key = f"topic_{question['topic']}"
    diff_key = f"difficulty_{question['difficulty']}"
    header = t("question_number", lang, current=current, total=total)
    meta = t("topic_label", lang, topic=t(topic_key, lang), difficulty=t(diff_key, lang))
    q_text = question["question"].get(lang, question["question"]["en"])

    text = f"{header}\n{meta}\n\n{q_text}"

    exit_btn = [InlineKeyboardButton(text=t("btn_exit_quiz", lang), callback_data="quiz:exit")]

    if question["type"] == "multiple_choice":
        options = question["options"]
        if isinstance(options, dict):
            options = options.get(lang, options.get("en", []))
        buttons = []
        for i, opt in enumerate(options):
            buttons.append([InlineKeyboardButton(text=opt, callback_data=f"ans:{i}")])
        buttons.append(exit_btn)
        kb = InlineKeyboardMarkup(inline_keyboard=buttons)
        await message.answer(text, reply_markup=kb)
    else:
        # Open-ended — show exit button, user types answer as text
        user["awaiting_open_answer"] = True
        text += f"\n\n{t('open_ended_prompt', lang)}"
        kb = InlineKeyboardMarkup(inline_keyboard=[exit_btn])
        await message.answer(text, reply_markup=kb)


def _build_goal_notifications(user_id: int, lang: str, reached: list[str]) -> str:
    """Build goal congratulation text and add bonus points."""
    parts = []
    for period in reached:
        bonus = get_goal_bonus(period)
        add_score(user_id, bonus)
        period_name = t(f"period_{period}", lang)
        parts.append(t("goal_reached", lang, period=period_name, bonus=bonus))
    return "\n".join(parts)


async def _process_answer(message: Message, user_id: int, is_correct: bool, question: dict) -> None:
    """Show feedback, advance quiz, check goals."""
    lang = get_language(user_id)
    pet = get_active_pet(user_id)
    pet_display = get_pet_display(pet)

    # Feedback
    if is_correct:
        feedback = t("correct", lang)
        pet_msg = t("pet_reaction_correct", lang, pet=pet_display)
    else:
        feedback = t("incorrect", lang)
        pet_msg = t("pet_reaction_incorrect", lang, pet=pet_display)

    explanation = question["explanation"].get(lang, question["explanation"]["en"])
    text = f"{feedback}\n{t('explanation', lang, text=explanation)}\n\n{pet_msg}"

    record_answer(user_id, is_correct)

    # Goal progress — check EVERY question, not just the last
    reached = increment_progress(user_id)
    if reached:
        text += "\n\n" + _build_goal_notifications(user_id, lang, reached)

    # Advance quiz
    finished = advance_quiz(user_id, is_correct)

    if finished:
        results = get_quiz_results(user_id)
        add_score(user_id, results["points"])

        pet_done = t("pet_reaction_quiz_done", lang, pet=pet_display)
        result_text = t(
            "quiz_finished", lang,
            correct=results["correct"],
            total=results["total"],
            pct=results["pct"],
            points=results["points"],
        )
        text += f"\n\n{result_text}\n{pet_done}"

        end_quiz(user_id)
        await message.answer(text, reply_markup=_results_keyboard(lang))
    else:
        await message.answer(text)
        await _send_question(message, user_id)


async def start_quiz_for_user(message: Message, user_id: int) -> None:
    """Start a quiz session. Reusable from callback or command."""
    lang = get_language(user_id)
    questions = start_quiz(user_id)
    if not questions:
        await message.answer(t("no_questions", lang), reply_markup=_back_menu_kb(lang))
        return
    await message.answer(t("quiz_start", lang, n=len(questions)))
    await _send_question(message, user_id)


# --- Command: /quiz ---
@router.message(Command("quiz"))
async def cmd_quiz(message: Message) -> None:
    await start_quiz_for_user(message, message.from_user.id)


# --- Callback: start quiz ---
@router.callback_query(F.data == "menu:quiz")
async def on_quiz_start(callback: CallbackQuery) -> None:
    await callback.answer()
    user_id = callback.from_user.id
    lang = get_language(user_id)
    questions = start_quiz(user_id)
    if not questions:
        await callback.message.edit_text(
            t("no_questions", lang), reply_markup=_back_menu_kb(lang)
        )
        return
    await callback.message.edit_text(t("quiz_start", lang, n=len(questions)))
    await _send_question(callback.message, user_id)


# --- Callback: exit quiz ---
@router.callback_query(F.data == "quiz:exit")
async def on_quiz_exit(callback: CallbackQuery) -> None:
    await callback.answer()
    user_id = callback.from_user.id
    lang = get_language(user_id)
    end_quiz(user_id)
    await callback.message.edit_text(
        t("quiz_exited", lang), reply_markup=_back_menu_kb(lang)
    )


# --- Callback: multiple-choice answer ---
@router.callback_query(F.data.startswith("ans:"))
async def on_mc_answer(callback: CallbackQuery) -> None:
    await callback.answer()
    user_id = callback.from_user.id

    # Validate callback data
    try:
        answer_idx = int(callback.data.split(":")[1])
    except (ValueError, IndexError):
        return

    result = check_mc_answer(user_id, answer_idx)
    if result is None:
        return

    is_correct, question = result
    await callback.message.edit_reply_markup(reply_markup=None)
    await _process_answer(callback.message, user_id, is_correct, question)


# --- Message: open-ended answer ---
async def handle_open_answer(message: Message) -> bool:
    """Check if this message is an open-ended quiz answer. Returns True if handled."""
    user_id = message.from_user.id
    user = get_user(user_id)

    if not user.get("awaiting_open_answer"):
        return False

    result = check_open_answer(user_id, message.text or "")
    if result is None:
        user["awaiting_open_answer"] = False
        return False

    is_correct, question = result
    await _process_answer(message, user_id, is_correct, question)
    return True
