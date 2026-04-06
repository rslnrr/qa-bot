from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from data.texts import t
from services.user_service import set_language, get_language
from handlers.menu import send_main_menu

router = Router()


def _language_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="English", callback_data="lang:en"),
            InlineKeyboardButton(text="Русский", callback_data="lang:ru"),
            InlineKeyboardButton(text="Українська", callback_data="lang:ua"),
        ]
    ])


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    text = (
        "Welcome to QA & Python Training Bot!\n"
        "Добро пожаловать в QA & Python Training Bot!\n"
        "Ласкаво просимо до QA & Python Training Bot!\n\n"
        "Please choose your language / Выберите язык / Оберіть мову:"
    )
    await message.answer(text, reply_markup=_language_keyboard())


@router.message(Command("menu"))
async def cmd_menu(message: Message) -> None:
    await send_main_menu(message, message.from_user.id)


@router.callback_query(F.data.startswith("lang:"))
async def on_language_selected(callback: CallbackQuery) -> None:
    await callback.answer()
    lang = callback.data.split(":")[1]
    user_id = callback.from_user.id
    set_language(user_id, lang)
    await callback.message.edit_text(t("language_set", lang))
    await send_main_menu(callback.message, user_id)


# --- Callback: change language from menu ---
@router.callback_query(F.data == "menu:change_lang")
async def on_change_lang(callback: CallbackQuery) -> None:
    await callback.answer()
    lang = get_language(callback.from_user.id)
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="English", callback_data="lang:en"),
            InlineKeyboardButton(text="Русский", callback_data="lang:ru"),
            InlineKeyboardButton(text="Українська", callback_data="lang:ua"),
        ],
        [InlineKeyboardButton(text=t("btn_back_menu", lang), callback_data="back:menu")],
    ])
    await callback.message.edit_text(t("choose_language", lang), reply_markup=kb)
