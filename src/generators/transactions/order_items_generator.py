import random

import pandas as pd

from src.utils.helpers import load_csv, append_csv

random.seed(42)

orders = load_csv("orders.csv")
menu_items = load_csv("menu_items.csv")

CHUNK_SIZE = 5000

order_item_id = 1

buffer = []

for _, order in orders.iterrows():

    restaurant_menu = menu_items[
        menu_items["restaurant_id"] == order["restaurant_id"]
    ]

    item_count = random.randint(1, 6)

    chosen_items = restaurant_menu.sample(
        n=item_count,
        replace=True
    )

    for _, item in chosen_items.iterrows():

        quantity = random.randint(1, 3)

        unit_price = item["price"]

        total_price = round(
            quantity * unit_price,
            2
        )

        buffer.append({

            "id": order_item_id,

            "order_id": order["id"],

            "menu_item_id": item["id"],

            "quantity": quantity,

            "unit_price": unit_price,

            "total_price": total_price

        })

        order_item_id += 1

        if len(buffer) >= CHUNK_SIZE:

            append_csv(
                pd.DataFrame(buffer),
                "order_items.csv"
            )

            print(f"Saved {order_item_id-1} order items")

            buffer.clear()

if buffer:

    append_csv(
        pd.DataFrame(buffer),
        "order_items.csv"
    )

print(f"Finished : {order_item_id-1} order items")