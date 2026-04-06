"""Mock AI question generation service.

For MVP, this generates questions from templates. The interface is designed
so that a real AI API (e.g., Anthropic, OpenAI) can be plugged in later.
"""

import random

_TEMPLATES = {
    "python_basics": [
        {
            "type": "multiple_choice",
            "question": {
                "en": "What will `len('{obj}')` return?",
                "ru": "Что вернёт `len('{obj}')`?",
                "ua": "Що поверне `len('{obj}')`?",
            },
            "make": lambda: _len_question(),
        },
    ],
    "oop": [
        {
            "type": "multiple_choice",
            "question": {
                "en": "Which of these is a pillar of OOP?",
                "ru": "Что из перечисленного — принцип ООП?",
                "ua": "Що з переліченого — принцип ООП?",
            },
            "make": lambda: _oop_pillar_question(),
        },
    ],
}


def _len_question() -> dict:
    obj = random.choice(["hello", "python", "test", "abc", "selenium"])
    correct_len = len(obj)
    wrong = [correct_len + i for i in [1, -1, 2]]
    options = [str(correct_len)] + [str(w) for w in wrong]
    random.shuffle(options)
    correct_idx = options.index(str(correct_len))
    return {
        "id": f"ai_len_{obj}",
        "topic": "python_basics",
        "difficulty": random.choice(["easy", "medium"]),
        "type": "multiple_choice",
        "question": {
            "en": f"What will `len('{obj}')` return?",
            "ru": f"Что вернёт `len('{obj}')`?",
            "ua": f"Що поверне `len('{obj}')`?",
        },
        "options": options,
        "correct": correct_idx,
        "explanation": {
            "en": f"The string '{obj}' has {correct_len} characters.",
            "ru": f"Строка '{obj}' содержит {correct_len} символов.",
            "ua": f"Рядок '{obj}' містить {correct_len} символів.",
        },
    }


def _oop_pillar_question() -> dict:
    pillars = ["Encapsulation", "Inheritance", "Polymorphism", "Abstraction"]
    correct = random.choice(pillars)
    wrong = ["Compilation", "Serialization", "Recursion", "Iteration"]
    options = [correct] + random.sample(wrong, 3)
    random.shuffle(options)
    correct_idx = options.index(correct)
    return {
        "id": f"ai_oop_{correct.lower()}",
        "topic": "oop",
        "difficulty": "medium",
        "type": "multiple_choice",
        "question": {
            "en": "Which of these is a pillar of OOP?",
            "ru": "Что из перечисленного — принцип ООП?",
            "ua": "Що з переліченого — принцип ООП?",
        },
        "options": options,
        "correct": correct_idx,
        "explanation": {
            "en": f"{correct} is one of the four pillars of OOP.",
            "ru": f"{correct} — один из четырёх принципов ООП.",
            "ua": f"{correct} — один із чотирьох принципів ООП.",
        },
    }


def generate_question(topic: str = "python_basics", difficulty: str = "medium") -> dict:
    """Generate a question for the given topic.

    MVP: picks from random templates.
    Future: call AI API here (Anthropic/OpenAI) to generate novel questions.
    """
    templates = _TEMPLATES.get(topic)
    if templates:
        template = random.choice(templates)
        return template["make"]()
    # Fallback: return a generic len question
    return _len_question()
