import random

from config import QUIZ_SIZE
from data.questions import QUESTIONS
from services.user_service import get_user
from utils.matching import is_close_match


def start_quiz(user_id: int) -> list[dict] | None:
    """Create a new quiz session for the user. Returns the question list or None."""
    pool = list(QUESTIONS)
    if not pool:
        return None
    random.shuffle(pool)
    questions = pool[:QUIZ_SIZE]
    user = get_user(user_id)
    user["quiz"] = {
        "questions": questions,
        "current_index": 0,
        "correct": 0,
    }
    user["awaiting_open_answer"] = False
    return questions


def get_current_question(user_id: int) -> dict | None:
    """Get the current question in the user's active quiz."""
    user = get_user(user_id)
    quiz = user.get("quiz")
    if not quiz:
        return None
    idx = quiz["current_index"]
    if idx >= len(quiz["questions"]):
        return None
    return quiz["questions"][idx]


def check_mc_answer(user_id: int, answer_index: int) -> tuple[bool, dict] | None:
    """Check a multiple-choice answer. Returns (is_correct, question) or None."""
    question = get_current_question(user_id)
    if question is None:
        return None
    is_correct = answer_index == question["correct"]
    return is_correct, question


def check_open_answer(user_id: int, user_text: str) -> tuple[bool, dict] | None:
    """Check an open-ended answer. Returns (is_correct, question) or None."""
    question = get_current_question(user_id)
    if question is None:
        return None
    accepted = question.get("accept", [question["correct"]])
    is_correct = is_close_match(user_text, accepted)
    return is_correct, question


def advance_quiz(user_id: int, correct: bool) -> bool:
    """Move to the next question. Returns True if quiz is finished."""
    user = get_user(user_id)
    quiz = user["quiz"]
    if correct:
        quiz["correct"] += 1
    quiz["current_index"] += 1
    user["awaiting_open_answer"] = False
    return quiz["current_index"] >= len(quiz["questions"])


def get_quiz_results(user_id: int) -> dict:
    """Get final quiz results."""
    user = get_user(user_id)
    quiz = user["quiz"]
    total = len(quiz["questions"])
    correct = quiz["correct"]
    pct = round(correct / total * 100) if total else 0
    points = correct * 10
    return {"correct": correct, "total": total, "pct": pct, "points": points}


def end_quiz(user_id: int) -> None:
    """Clear the quiz session."""
    user = get_user(user_id)
    user["quiz"] = None
    user["awaiting_open_answer"] = False
