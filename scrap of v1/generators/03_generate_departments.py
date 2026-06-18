"""
Generate Departments table.
"""

import pandas as pd

from src.config import RAW_EXCEL_FILE
from src.utils.helpers import (
    clean_dataframe,
    save_csv,
    print_summary
)

df = pd.read_excel(
    RAW_EXCEL_FILE,
    sheet_name="Departments"
)

df = clean_dataframe(df)

save_csv(df, "departments.csv")

print_summary(df, "Departments")