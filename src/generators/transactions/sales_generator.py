import random
from datetime import timedelta

import pandas as pd

from src.utils.helpers import load_csv, append_csv

random.seed(42)

orders = load_csv("orders.csv")

CHUNK_SIZE = 5000

sale_id = 1

buffer = []

for _, order in orders.iterrows():

    sale_time = pd.to_datetime(order["order_datetime"]) + timedelta(
        minutes=random.randint(5, 45)
    )

    gross = round(order["subtotal"], 2)

    discount = round(order["discount"], 2)

    tax = round(order["tax"], 2)

    net = round(order["total_amount"], 2)

    buffer.append({

        "id": sale_id,

        "order_id": order["id"],

        "sale_datetime": sale_time,

        "gross_sales": gross,

        "discount_amount": discount,

        "tax_amount": tax,

        "net_sales": net,

        "status": "Completed"

    })

    sale_id += 1

    if len(buffer) >= CHUNK_SIZE:

        append_csv(
            pd.DataFrame(buffer),
            "sales.csv"
        )

        print(f"Saved {sale_id-1} sales")

        buffer.clear()

if buffer:

    append_csv(
        pd.DataFrame(buffer),
        "sales.csv"
    )

print(f"Finished : {sale_id-1} sales")
