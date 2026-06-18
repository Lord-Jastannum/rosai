"""
Common helper functions used across all generators.
"""

from pathlib import Path
import pandas as pd

from src.config import GENERATED_DATA_DIR


# -----------------------------------------------------
# File Handling
# -----------------------------------------------------

def load_csv(filename: str) -> pd.DataFrame:
    """
    Load a CSV from the generated folder.
    """

    path = GENERATED_DATA_DIR / filename

    if not path.exists():
        raise FileNotFoundError(f"{filename} not found.")

    return pd.read_csv(path)


def save_csv(df: pd.DataFrame, filename: str):

    GENERATED_DATA_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    output = GENERATED_DATA_DIR / filename

    df.to_csv(
        output,
        index=False
    )

    print(f"\nSaved -> {output}")


# -----------------------------------------------------
# Cleaning
# -----------------------------------------------------

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standard cleaning for all Excel sheets.
    """

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    df = df.dropna(how="all")
    df = df.drop_duplicates()
    df = df.reset_index(drop=True)

    return df


# -----------------------------------------------------
# Summary
# -----------------------------------------------------

def print_summary(df: pd.DataFrame, table_name: str):

    print("\n" + "=" * 60)
    print(table_name.upper())
    print("=" * 60)

    print(f"Rows    : {len(df)}")
    print(f"Columns : {len(df.columns)}")

    print("\nColumns")

    for col in df.columns:
        print(f"  • {col}")

    print("\nPreview")

    print(df.head())