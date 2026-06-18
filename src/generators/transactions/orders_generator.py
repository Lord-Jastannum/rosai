"""
Generate Orders
"""

import random
from datetime import datetime, timedelta

import pandas as pd

from src.utils.helpers import load_csv, save_csv

random.seed(42)

restaurants = load_csv("restaurants.csv")
customers = load_csv("customers.csv")
users = load_csv("users.csv")

orders = []

order_id = 1

order_types = [
    ("Dine In", 0.50),
    ("Takeaway", 0.25),
    ("Delivery", 0.25),
]

payment_status = ["Paid", "Paid", "Paid", "Pending"]

start_date = datetime(2024, 1, 1)

days = 365

for day in range(days):

    current_date = start_date + timedelta(days=day)

    weekend = current_date.weekday() >= 5

    for _, restaurant in restaurants.iterrows():

        restaurant_customers = customers[
            customers["restaurant_id"] == restaurant["id"]
        ]

        restaurant_users = users[
            users["restaurant_id"] == restaurant["id"]
        ]

        if restaurant_customers.empty or restaurant_users.empty:
            continue

        orders_today = (
            random.randint(180, 300)
            if weekend
            else random.randint(120, 220)
        )

        for _ in range(orders_today):

            customer = restaurant_customers.sample(1).iloc[0]
            employee = restaurant_users.sample(1).iloc[0]

            order_time = current_date + timedelta(
                minutes=random.randint(540, 1320)
            )

            order_type = random.choices(
                [o[0] for o in order_types],
                weights=[o[1] for o in order_types],
            )[0]

            orders.append({

                "id": order_id,

                "restaurant_id": restaurant["id"],

                "customer_id": customer["id"],

                "user_id": employee["id"],

                "order_datetime": order_time,

                "order_type": order_type,

                "payment_status": random.choice(payment_status),

                "status": "Completed"

            })

            order_id += 1

df = pd.DataFrame(orders)

save_csv(df, "orders.csv")

print(f"Generated {len(df)} orders.")
