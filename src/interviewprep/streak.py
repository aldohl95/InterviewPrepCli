from datetime import date
from interviewprep.storage import load_streak, save_streak


def update_streak() -> dict:
    streak = load_streak()
    today = date.today()

    if streak["last_completed"]:
        last = date.fromisoformat(streak["last_completed"])
        diff = (today - last).days

        if diff == 1:
            streak["current_streak"] += 1
            streak["longest_streak"] = max(
                streak["current_streak"], streak["longest_streak"]
            )
        elif diff == 0:
            return streak
        else:
            streak["current_streak"] = 1

    else:
        streak["current_streak"] = 1
        streak["longest_streak"] = 1
        streak["last_completed"] = today.isoformat()

    streak["last_completed"] = today.isoformat()

    save_streak(streak)

    return streak
