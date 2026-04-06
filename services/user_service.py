from datetime import date

# In-memory user storage: {user_id: {...}}
_users: dict[int, dict] = {}

DEFAULT_PETS = ["Cat", "Dog", "Dragon", "Bunny"]
STARTER_PET = "Cat"


def _default_user() -> dict:
    today = date.today().isoformat()
    return {
        "language": None,
        "score": 0,
        "points": 0,
        "questions_answered": 0,
        "correct_answers": 0,
        # Active quiz session
        "quiz": None,
        # Awaiting open-ended answer
        "awaiting_open_answer": False,
        # Awaiting feedback text
        "awaiting_feedback": False,
        # Goals
        "goals": {
            "daily": {"target": 0, "done": 0, "last_reset": today, "reached": False},
            "weekly": {"target": 0, "done": 0, "last_reset": today, "reached": False},
            "monthly": {"target": 0, "done": 0, "last_reset": today, "reached": False},
        },
        # Pets
        "pets": [STARTER_PET],
        "active_pet": STARTER_PET,
        "badges": [],
    }


def get_user(user_id: int) -> dict:
    if user_id not in _users:
        _users[user_id] = _default_user()
    return _users[user_id]


def get_language(user_id: int) -> str:
    return get_user(user_id).get("language") or "en"


def set_language(user_id: int, lang: str) -> None:
    get_user(user_id)["language"] = lang


def add_score(user_id: int, points: int) -> None:
    user = get_user(user_id)
    user["score"] += points
    user["points"] += points


def record_answer(user_id: int, correct: bool) -> None:
    user = get_user(user_id)
    user["questions_answered"] += 1
    if correct:
        user["correct_answers"] += 1
