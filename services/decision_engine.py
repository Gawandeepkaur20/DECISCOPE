def clamp(value, minimum=0, maximum=100):
    return max(minimum, min(maximum, value))


def calculate_decision_score(
    career_value,
    skill_alignment,
    networking_value,
    time_fit,
    deadline_safety
):
    """
    Calculate a transparent decision score.

    Positive factors:
    - Career value
    - Skill alignment
    - Networking value

    Negative/constraint factors:
    - Time fit
    - Deadline safety
    """

    score = (
        career_value * 0.25
        + skill_alignment * 0.25
        + networking_value * 0.15
        + time_fit * 0.20
        + deadline_safety * 0.15
    )

    return round(
        clamp(score)
    )


def get_recommendation(score):

    if score >= 80:
        return "Strongly Consider"

    elif score >= 65:
        return "Consider"

    elif score >= 50:
        return "Review Carefully"

    else:
        return "Probably Skip"


def get_risk_level(score):

    if score >= 80:
        return "Low"

    elif score >= 65:
        return "Moderate"

    elif score >= 50:
        return "High"

    else:
        return "Very High"