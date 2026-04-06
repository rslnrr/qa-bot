from services.user_service import get_user, DEFAULT_PETS

PET_PRICES = {"Cat": 0, "Dog": 50, "Dragon": 150, "Bunny": 80}

PET_EMOJIS = {"Cat": "🐱", "Dog": "🐶", "Dragon": "🐉", "Bunny": "🐰"}


def get_pet_emoji(name: str) -> str:
    return PET_EMOJIS.get(name, "🐾")


def get_pet_display(name: str) -> str:
    return f"{get_pet_emoji(name)} {name}"


def get_owned_pets(user_id: int) -> list[str]:
    return get_user(user_id)["pets"]


def get_active_pet(user_id: int) -> str:
    return get_user(user_id)["active_pet"]


def select_pet(user_id: int, pet_name: str) -> bool:
    user = get_user(user_id)
    if pet_name not in user["pets"]:
        return False
    user["active_pet"] = pet_name
    return True


def buy_pet(user_id: int, pet_name: str) -> tuple[bool, str]:
    """Try to buy a pet. Returns (success, error_key)."""
    user = get_user(user_id)
    if pet_name in user["pets"]:
        return False, "pet_already_owned"
    price = PET_PRICES.get(pet_name, 100)
    if user["points"] < price:
        return False, "pet_not_enough_points"
    user["points"] -= price
    user["pets"].append(pet_name)
    return True, ""


def get_buyable_pets(user_id: int) -> list[tuple[str, int]]:
    """Return list of (pet_name, price) for pets the user doesn't own."""
    owned = set(get_owned_pets(user_id))
    return [(p, PET_PRICES.get(p, 100)) for p in DEFAULT_PETS if p not in owned]


def get_pet_price(pet_name: str) -> int:
    return PET_PRICES.get(pet_name, 100)
