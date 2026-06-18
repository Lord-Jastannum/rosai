"""
Reusable helper functions.
"""

from pathlib import Path

import pandas as pd

from src.config import GENERATED_DATA_DIR


def load_csv(filename: str) -> pd.DataFrame:
    """
    Load CSV from generated folder.
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


def print_summary(df: pd.DataFrame, table_name: str):

    print("\n------------------------------")

    print(table_name)

    print("------------------------------")

    print(df.head())

    print()

    print(df.info())

    print()

    print(df.describe(include="all"))