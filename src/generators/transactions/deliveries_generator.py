import random
from datetime import timedelta

import pandas as pd

from src.utils.helpers import load_csv, append_csv

random.seed(42)

orders = load_csv("orders.csv")

CHUNK_SIZE = 5000

delivery_id = 1

buffer = []

partners = [
    "Uber Eats",
    "Zomato",
    "Swiggy",
    "Deliveroo",
    "Just Eat",
    "In House"
]

for _, order in orders.iterrows():

    if order["order_type"] != "Delivery":
        continue

    order_time = pd.to_datetime(order["order_datetime"])

    distance = round(random.uniform(1, 12), 2)

    eta = random.randint(20, 60)

    actual = eta + random.randint(-5, 15)

    charge = round(distance * random.uniform(1.2, 2.5), 2)

    buffer.append({

        "id": delivery_id,

        "order_id": order["id"],

        "delivery_partner": random.choice(partners),

        "delivery_status": "Delivered",

        "delivery_distance_km": distance,

        "estimated_minutes": eta,

        "actual_minutes": actual,

        "delivery_charge": charge,

        "pickup_time": order_time + timedelta(minutes=10),

        "delivered_time": order_time + timedelta(minutes=actual),

        "created_at": order_time,

        "updated_at": order_time + timedelta(minutes=actual)

    })

    delivery_id += 1

    if len(buffer) >= CHUNK_SIZE:

        append_csv(
            pd.DataFrame(buffer),
            "deliveries.csv"
        )

        print(f"Saved {delivery_id-1} deliveries")

        buffer.clear()

if buffer:

    append_csv(
        pd.DataFrame(buffer),
        "deliveries.csv"
    )

print(f"Finished : {delivery_id-1} deliveries")