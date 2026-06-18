import random
from datetime import datetime

import pandas as pd

from src.utils.helpers import load_csv, save_csv

random.seed(42)

cashups = load_csv("cashup.csv")

banks = [
    "HSBC",
    "Barclays",
    "Lloyds",
    "NatWest",
    "HDFC Bank",
    "ICICI Bank",
    "SBI",
    "Axis Bank",
]

rows = []

banking_id = 1

for _, cashup in cashups.iterrows():

    if cashup["cash_sales"] <= 0:
        continue

    deposit = round(
        cashup["cash_sales"] - random.uniform(0, 10),
        2
    )

    rows.append({

        "id": banking_id,

        "restaurant_id": cashup["restaurant_id"],

        "cashup_id": cashup["id"],

        "deposit_date": cashup["business_date"],

        "bank_name": random.choice(banks),

        "account_number": f"****{random.randint(1000,9999)}",

        "deposit_amount": deposit,

        "reference_number": f"DEP{banking_id:08d}",

        "status": "Deposited",

        "created_at": datetime.now(),

        "updated_at": datetime.now()

    })

    banking_id += 1

df = pd.DataFrame(rows)

save_csv(df, "banking.csv")

print(f"Generated {len(df)} banking records.")