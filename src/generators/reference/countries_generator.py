"""
Generate Countries Table
"""

import pandas as pd

from src.utils.helpers import save_csv

countries = [
    {
        "country_id": 1,
        "country_name": "United Kingdom",
        "iso2": "GB",
        "iso3": "GBR",
        "currency_code": "GBP",
        "currency_name": "Pound Sterling",
        "phone_code": "+44",
        "timezone": "Europe/London",
        "language": "English",
        "status": "Active"
    },
    {
        "country_id": 2,
        "country_name": "India",
        "iso2": "IN",
        "iso3": "IND",
        "currency_code": "INR",
        "currency_name": "Indian Rupee",
        "phone_code": "+91",
        "timezone": "Asia/Kolkata",
        "language": "English",
        "status": "Active"
    }
]

df = pd.DataFrame(countries)

save_csv(df, "countries.csv")

print(f"Generated {len(df)} countries.")
print(df.head())
