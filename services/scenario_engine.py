def calculate_scenario_score(
    factors,
    time_multiplier=1.0,
    deadline_multiplier=1.0
):
    """
    Recalculate the decision score under changed conditions.
    """

    adjusted_time_fit = (
        factors["time_fit"] * time_multiplier
    )

    adjusted_deadline_safety = (
        factors["deadline_safety"] * deadline_multiplier
    )

    adjusted_time_fit = max(
        0,
        min(100, adjusted_time_fit)
    )

    adjusted_deadline_safety = max(
        0,
        min(100, adjusted_deadline_safety)
    )

    score = (
        factors["career_value"] * 0.25
        + factors["skill_alignment"] * 0.25
        + factors["networking_value"] * 0.15
        + adjusted_time_fit * 0.20
        + adjusted_deadline_safety * 0.15
    )

    return round(score)


def compare_scores(original_score, scenario_score):

    difference = scenario_score - original_score

    if difference > 0:
        direction = "improved"

    elif difference < 0:
        direction = "declined"

    else:
        direction = "unchanged"

    return {
        "difference": difference,
        "direction": direction
    }