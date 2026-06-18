"""
Generate Currency Table
"""

import pandas as pd

from src.utils.helpers import save_csv

currencies = [
    {
        "currency_id": 1,
        "currency_code": "GBP",
        "currency_name": "Pound Sterling",
        "symbol": "£",
        "country": "United Kingdom",
        "status": "Active"
    },
    {
        "currency_id": 2,
        "currency_code": "INR",
        "currency_name": "Indian Rupee",
        "symbol": "₹",
        "country": "India",
        "status": "Active"
    }
]

df = pd.DataFrame(currencies)

save_csv(df, "currencies.csv")

print(f"Generated {len(df)} currencies.")
print(df.head())
