"""
Common helper functions.
"""

import pandas as pd

from src.config import GENERATED_DIR


def save_csv(df: pd.DataFrame, filename: str):

    GENERATED_DIR.mkdir(parents=True, exist_ok=True)

    output = GENERATED_DIR / filename

    df.to_csv(output, index=False)

    print(f"Saved -> {output}")


def load_csv(filename: str) -> pd.DataFrame:

    path = GENERATED_DIR / filename

    if not path.exists():
        raise FileNotFoundError(f"{filename} not found.")

    return pd.read_csv(path)