import random

import pandas as pd

from src.utils.helpers import load_csv, save_csv

random.seed(42)

cashups = load_csv("cashup.csv")
pdq = load_csv("pdqmachines.csv")

rows = []

record_id = 1

for _, cashup in cashups.iterrows():

    restaurant_pdq = pdq[
        pdq["restaurant_id"] == cashup["restaurant_id"]
    ]

    if restaurant_pdq.empty:
        continue

    for _, machine in restaurant_pdq.iterrows():

        card_sales = round(
            cashup["card_sales"] / len(restaurant_pdq),
            2
        )

        rows.append({

            "id": record_id,

            "cashup_id": cashup["id"],

            "pdq_machine_id": machine["id"],

            "cash_amount": round(cashup["cash_sales"], 2),

            "card_amount": card_sales,

            "upi_amount": round(cashup["upi_sales"], 2),

            "online_amount": round(cashup["online_sales"], 2),

            "total_amount": round(
                cashup["cash_sales"]
                + card_sales
                + cashup["upi_sales"]
                + cashup["online_sales"],
                2
            )

        })

        record_id += 1

df = pd.DataFrame(rows)

save_csv(df, "cash_pdq.csv")

print(f"Generated {len(df)} Cash & PDQ records.")
