from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from data.texts import t
from services.user_service import get_language, get_user
from services.pet_service import (
    get_owned_pets,
    get_active_pet,
    get_buyable_pets,
    get_pet_display,
    get_pet_price,
    select_pet,
    buy_pet,
)

router = Router()


def _pets_menu_kb(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t("btn_select_pet", lang), callback_data="pet:select")],
        [InlineKeyboardButton(text=t("btn_buy_pet", lang), callback_data="pet:buy")],
        [InlineKeyboardButton(text=t("btn_back_menu", lang), callback_data="back:menu")],
    ])


@router.callback_query(F.data == "menu:pets")
async def on_pets_menu(callback: CallbackQuery) -> None:
    await callback.answer()
    user_id = callback.from_user.id
    lang = get_language(user_id)
    user = get_user(user_id)

    active = get_pet_display(get_active_pet(user_id))
    owned = ", ".join(get_pet_display(p) for p in get_owned_pets(user_id))
    points = user["points"]

    await callback.message.edit_text(
        t("pets_menu", lang, active=active, owned=owned, points=points),
        reply_markup=_pets_menu_kb(lang),
    )


@router.callback_query(F.data == "pet:select")
async def on_pet_select_list(callback: CallbackQuery) -> None:
    await callback.answer()
    user_id = callback.from_user.id
    lang = get_language(user_id)
    owned = get_owned_pets(user_id)

    buttons = [
        [InlineKeyboardButton(
            text=get_pet_display(p), callback_data=f"petpick:{p}"
        )]
        for p in owned
    ]
    buttons.append([InlineKeyboardButton(text=t("btn_back_menu", lang), callback_data="menu:pets")])
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.message.edit_text(t("btn_select_pet", lang), reply_markup=kb)


@router.callback_query(F.data.startswith("petpick:"))
async def on_pet_pick(callback: CallbackQuery) -> None:
    await callback.answer()
    user_id = callback.from_user.id
    lang = get_language(user_id)
    pet_name = callback.data.split(":")[1]

    select_pet(user_id, pet_name)
    back_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t("btn_back_menu", lang), callback_data="menu:pets")],
    ])
    await callback.message.edit_text(
        t("pet_selected", lang, pet=get_pet_display(pet_name)), reply_markup=back_kb
    )


@router.callback_query(F.data == "pet:buy")
async def on_pet_buy_list(callback: CallbackQuery) -> None:
    await callback.answer()
    user_id = callback.from_user.id
    lang = get_language(user_id)
    buyable = get_buyable_pets(user_id)

    if not buyable:
        back_kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=t("btn_back_menu", lang), callback_data="menu:pets")],
        ])
        await callback.message.edit_text(
            t("all_pets_owned", lang), reply_markup=back_kb
        )
        return

    buttons = [
        [InlineKeyboardButton(
            text=f"{get_pet_display(name)} — {price} pts",
            callback_data=f"petbuy:{name}",
        )]
        for name, price in buyable
    ]
    buttons.append([InlineKeyboardButton(text=t("btn_back_menu", lang), callback_data="menu:pets")])
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.message.edit_text(t("btn_buy_pet", lang), reply_markup=kb)


@router.callback_query(F.data.startswith("petbuy:"))
async def on_pet_buy(callback: CallbackQuery) -> None:
    await callback.answer()
    user_id = callback.from_user.id
    lang = get_language(user_id)
    pet_name = callback.data.split(":")[1]

    success, error_key = buy_pet(user_id, pet_name)
    back_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t("btn_back_menu", lang), callback_data="menu:pets")],
    ])

    if success:
        price = get_pet_price(pet_name)
        text = t("pet_bought", lang, pet=get_pet_display(pet_name), price=price)
    elif error_key == "pet_already_owned":
        text = t("pet_already_owned", lang)
    else:
        user = get_user(user_id)
        text = t("pet_not_enough_points", lang, price=get_pet_price(pet_name), have=user["points"])

    await callback.message.edit_text(text, reply_markup=back_kb)
