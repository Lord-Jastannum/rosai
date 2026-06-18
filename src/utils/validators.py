"""
Validation utilities.
"""

import pandas as pd


def check_duplicate_ids(df: pd.DataFrame, column: str):

    duplicates = df[column].duplicated().sum()

    if duplicates:

        raise ValueError(
            f"{duplicates} duplicate IDs found in {column}"
        )


def check_nulls(df: pd.DataFrame):

    missing = df.isnull().sum()

    missing = missing[missing > 0]

    if len(missing):

        print("\nMissing Values\n")

        print(missing)


def validate_foreign_key(
    child_df: pd.DataFrame,
    child_column: str,
    parent_df: pd.DataFrame,
    parent_column: str,
):

    invalid = child_df[
        ~child_df[child_column].isin(parent_df[parent_column])
    ]

    if len(invalid):

        raise ValueError(
            f"Foreign key validation failed for {child_column}"
        )