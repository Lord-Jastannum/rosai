import random
from datetime import timedelta

import pandas as pd

from src.utils.helpers import load_csv, append_csv

random.seed(42)

sales = load_csv("sales.csv")
orders = load_csv("orders.csv")
pdq = load_csv("pdqmachines.csv")

CHUNK_SIZE = 5000

payment_id = 1

buffer = []

methods = ["Card", "Cash", "UPI", "Online"]
weights = [55, 15, 20, 10]

for _, sale in sales.iterrows():

    order = orders.loc[
        orders["id"] == sale["order_id"]
    ].iloc[0]

    restaurant_pdq = pdq[
        pdq["restaurant_id"] == order["restaurant_id"]
    ]

    method = random.choices(
        methods,
        weights=weights
    )[0]

    machine_id = None

    if method == "Card" and not restaurant_pdq.empty:

        machine_id = restaurant_pdq.sample(1).iloc[0]["id"]

    payment_time = (
        pd.to_datetime(sale["sale_datetime"])
        + timedelta(minutes=random.randint(1, 10))
    )

    buffer.append({

        "id": payment_id,

        "sale_id": sale["id"],

        "restaurant_id": order["restaurant_id"],

        "pdq_machine_id": machine_id,

        "payment_method": method,

        "transaction_reference": f"TXN{payment_id:010d}",

        "payment_datetime": payment_time,

        "amount": sale["net_sales"],

        "payment_status": "Success"

    })

    payment_id += 1

    if len(buffer) >= CHUNK_SIZE:

        append_csv(
            pd.DataFrame(buffer),
            "payments.csv"
        )

        print(f"Saved {payment_id-1} payments")

        buffer.clear()

if buffer:

    append_csv(
        pd.DataFrame(buffer),
        "payments.csv"
    )

print(f"Finished : {payment_id-1} payments")