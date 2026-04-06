from datetime import date

from services.user_service import get_user

GOAL_BONUSES = {"daily": 20, "weekly": 100, "monthly": 500}


def _reset_if_needed(goal: dict, period: str) -> None:
    """Reset goal progress if the period has elapsed."""
    today = date.today()
    last = date.fromisoformat(goal["last_reset"])

    should_reset = False
    if period == "daily" and last < today:
        should_reset = True
    elif period == "weekly" and (today - last).days >= 7:
        should_reset = True
    elif period == "monthly" and (today.year, today.month) != (last.year, last.month):
        should_reset = True

    if should_reset:
        goal["done"] = 0
        goal["reached"] = False
        goal["last_reset"] = today.isoformat()


def set_goal(user_id: int, period: str, target: int) -> None:
    user = get_user(user_id)
    goal = user["goals"][period]
    goal["target"] = target
    goal["done"] = 0
    goal["reached"] = False
    goal["last_reset"] = date.today().isoformat()


def increment_progress(user_id: int) -> list[str]:
    """Increment question count for all active goals.
    Returns list of period names where the goal was just reached.
    """
    user = get_user(user_id)
    reached = []
    for period in ("daily", "weekly", "monthly"):
        goal = user["goals"][period]
        if goal["target"] <= 0:
            continue
        _reset_if_needed(goal, period)
        goal["done"] += 1
        if goal["done"] >= goal["target"] and not goal["reached"]:
            goal["reached"] = True
            reached.append(period)
    return reached


def get_goal_bonus(period: str) -> int:
    return GOAL_BONUSES.get(period, 0)


def get_goals_summary(user_id: int) -> dict[str, dict]:
    user = get_user(user_id)
    result = {}
    for period in ("daily", "weekly", "monthly"):
        goal = user["goals"][period]
        _reset_if_needed(goal, period)
        result[period] = {"target": goal["target"], "done": goal["done"]}
    return result
