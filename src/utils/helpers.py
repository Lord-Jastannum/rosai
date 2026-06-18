import os
import pandas as pd

from src.config import GENERATED_DIR


def save_csv(df, filename):

    GENERATED_DIR.mkdir(parents=True, exist_ok=True)

    path = GENERATED_DIR / filename

    df.to_csv(path, index=False)


def append_csv(df, filename):

    GENERATED_DIR.mkdir(parents=True, exist_ok=True)

    path = GENERATED_DIR / filename

    if path.exists():

        df.to_csv(
            path,
            mode="a",
            header=False,
            index=False,
        )

    else:

        df.to_csv(
            path,
            index=False,
        )


def load_csv(filename):

    path = GENERATED_DIR / filename

    return pd.read_csv(path)