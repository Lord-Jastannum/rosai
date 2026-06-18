import random
from datetime import datetime, timedelta

import pandas as pd

from src.utils.helpers import load_csv, append_csv

random.seed(42)

restaurants = load_csv("restaurants.csv")
customers = load_csv("customers.csv")
users = load_csv("users.csv")

START_DATE = datetime(2025, 1, 1)
DAYS = 30
CHUNK_SIZE = 5000

order_id = 1
buffer = []

for day in range(DAYS):

    current_date = START_DATE + timedelta(days=day)

    weekend = current_date.weekday() >= 5

    print(f"Day {day+1}/{DAYS}")

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
            random.randint(60, 100)
            if weekend
            else random.randint(30, 60)
        )

        for _ in range(orders_today):

            customer = restaurant_customers.sample(1).iloc[0]
            employee = restaurant_users.sample(1).iloc[0]

            hour = random.choices(
                [9,10,11,12,13,14,18,19,20,21],
                weights=[2,3,4,9,10,7,10,12,8,5]
            )[0]

            minute = random.randint(0,59)

            order_time = current_date.replace(
                hour=hour,
                minute=minute
            )

            subtotal = round(random.uniform(15,120),2)

            discount = round(
                subtotal * random.choice([0,0,0.05,0.10]),
                2
            )

            tax = round((subtotal-discount)*0.05,2)

            total = round(
                subtotal-discount+tax,
                2
            )

            order_type = random.choices(
                ["Dine In","Takeaway","Delivery"],
                weights=[55,20,25]
            )[0]

            buffer.append({

                "id":order_id,

                "restaurant_id":restaurant["id"],

                "customer_id":customer["id"],

                "user_id":employee["id"],

                "order_datetime":order_time,

                "order_type":order_type,

                "subtotal":subtotal,

                "discount":discount,

                "tax":tax,

                "total_amount":total,

                "payment_status":"Paid",

                "status":"Completed"

            })

            order_id += 1

            if len(buffer) >= CHUNK_SIZE:

                append_csv(
                    pd.DataFrame(buffer),
                    "orders.csv"
                )

                print(f"Saved {order_id-1} orders")

                buffer.clear()

if buffer:

    append_csv(
        pd.DataFrame(buffer),
        "orders.csv"
    )

print(f"Finished. Total Orders : {order_id-1}")