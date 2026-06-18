"""
Generate Currencies table.
"""

import pandas as pd

from src.config import RAW_EXCEL_FILE
from src.utils.helpers import (
    clean_dataframe,
    save_csv,
    print_summary
)

# -----------------------------------------------------

df = pd.read_excel(
    RAW_EXCEL_FILE,
    sheet_name="Currencies"
)

df = clean_dataframe(df)

save_csv(df, "currencies.csv")

print_summary(df, "Currencies")