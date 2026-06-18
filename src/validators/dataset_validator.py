from pathlib import Path

import pandas as pd

DATA_DIR = Path("data/generated")

tables = {}

for file in DATA_DIR.glob("*.csv"):

    try:
        df = pd.read_csv(file)

        tables[file.stem] = df

    except Exception as e:

        print(f"Could not read {file.name}: {e}")

print("=" * 60)
print("DATASET REPORT")
print("=" * 60)

for name, df in tables.items():

    print(f"\n{name}")

    print(f"Rows      : {len(df)}")

    print(f"Columns   : {len(df.columns)}")

    print(f"Nulls     : {df.isnull().sum().sum()}")

    print(f"Duplicates: {df.duplicated().sum()}")

    if "id" in df.columns:

        dup = df["id"].duplicated().sum()

        print(f"Duplicate IDs : {dup}")

print("\nValidation Complete")