import pandas as pd


REQUIRED_COLUMNS = [
    "day",
    "activity",
    "hours",
    "category",
    "priority"
]


def normalize_dataframe(df):
    """Normalize CSV column names and safely standardize common aliases."""

    normalized = df.copy()
    normalized.columns = (
        normalized.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(r"\s+", "_", regex=True)
    )

    if "date" in normalized.columns and "day" not in normalized.columns:
        normalized = normalized.rename(columns={"date": "day"})

    return normalized


def validate_dataframe(df):
    """Return required CSV columns that are missing."""

    return [column for column in REQUIRED_COLUMNS if column not in df.columns]


def calculate_metrics(df):
    """Calculate workload KPIs without failing on missing or invalid hours."""

    if "hours" not in df.columns:
        return {
            "total_hours": 0.0,
            "academic_hours": 0.0,
            "development_hours": 0.0,
            "high_priority": 0,
        }

    metrics_df = df.copy()
    metrics_df["hours"] = pd.to_numeric(
        metrics_df["hours"], errors="coerce"
    ).fillna(0)

    category = metrics_df.get("category", pd.Series(index=metrics_df.index, dtype="object"))
    priority = metrics_df.get("priority", pd.Series(index=metrics_df.index, dtype="object"))

    return {
        "total_hours": round(metrics_df["hours"].sum(), 1),
        "academic_hours": round(
            metrics_df.loc[category.astype(str).str.lower() == "academic", "hours"].sum(), 1
        ),
        "development_hours": round(
            metrics_df.loc[category.astype(str).str.lower() == "development", "hours"].sum(), 1
        ),
        "high_priority": int(
            (priority.astype(str).str.lower() == "high").sum()
        ),
    }