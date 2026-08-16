import pandas as pd


REQUIRED_COLUMNS = [
    "date",
    "activity",
    "hours",
    "category",
    "priority"
]


def process_uploaded_csv(uploaded_file):
    """Read and clean an uploaded CSV file."""

    df = pd.read_csv(uploaded_file)

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    return df


def validate_dataframe(df):
    """Check whether the uploaded dataset has the required columns."""

    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    return missing_columns


def prepare_dataframe(df):
    """Clean and prepare the dataframe for analysis."""

    df = df.copy()

    if "date" in df.columns:
        df["date"] = pd.to_datetime(
            df["date"],
            errors="coerce"
        )

    if "hours" in df.columns:
        df["hours"] = pd.to_numeric(
            df["hours"],
            errors="coerce"
        ).fillna(0)

    return df


def calculate_metrics(df):
    """Calculate dashboard KPIs."""

    total_hours = round(df["hours"].sum(), 1)

    academic_hours = round(
        df.loc[
            df["category"].str.lower() == "academic",
            "hours"
        ].sum(),
        1
    )

    development_hours = round(
        df.loc[
            df["category"].str.lower() == "development",
            "hours"
        ].sum(),
        1
    )

    high_priority = int(
        (
            df["priority"].str.lower() == "high"
        ).sum()
    )

    return {
        "total_hours": total_hours,
        "academic_hours": academic_hours,
        "development_hours": development_hours,
        "high_priority": high_priority,
    }