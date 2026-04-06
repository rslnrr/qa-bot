def normalize(text: str) -> str:
    """Lowercase, strip whitespace and common punctuation."""
    return text.strip().lower().strip(".,!?;:'\"()[]")


def levenshtein(a: str, b: str) -> int:
    """Compute Levenshtein edit distance between two strings."""
    if len(a) < len(b):
        return levenshtein(b, a)
    if not b:
        return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a):
        curr = [i + 1]
        for j, cb in enumerate(b):
            cost = 0 if ca == cb else 1
            curr.append(min(curr[j] + 1, prev[j + 1] + 1, prev[j] + cost))
        prev = curr
    return prev[-1]


def is_close_match(user_answer: str, accepted: list[str], threshold: float = 0.75) -> bool:
    """Check if user's answer approximately matches any accepted answer.

    Uses normalized exact match first, then Levenshtein similarity.
    threshold: minimum similarity ratio (0.0 to 1.0) to consider a match.
    """
    user_norm = normalize(user_answer)
    if not user_norm:
        return False

    for ans in accepted:
        ans_norm = normalize(ans)
        # Exact match after normalization
        if user_norm == ans_norm:
            return True
        # Check if one contains the other
        if user_norm in ans_norm or ans_norm in user_norm:
            return True
        # Levenshtein similarity
        max_len = max(len(user_norm), len(ans_norm))
        if max_len == 0:
            continue
        similarity = 1 - levenshtein(user_norm, ans_norm) / max_len
        if similarity >= threshold:
            return True

    return False
