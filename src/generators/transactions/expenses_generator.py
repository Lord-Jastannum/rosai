import random
from datetime import datetime, timedelta

import pandas as pd

from src.utils.helpers import load_csv, append_csv

random.seed(42)

restaurants = load_csv("restaurants.csv")
users = load_csv("users.csv")

expense_categories = {
    "Rent": (2000, 10000),
    "Electricity": (300, 2000),
    "Water": (100, 500),
    "Gas": (200, 1500),
    "Ingredients": (500, 5000),
    "Cleaning": (50, 500),
    "Maintenance": (100, 3000),
    "Internet": (50, 300),
    "Marketing": (200, 2000),
    "Miscellaneous": (20, 500),
}

CHUNK_SIZE = 5000

expense_id = 1

buffer = []

start_date = datetime(2025, 1, 1)

for day in range(30):

    current_date = start_date + timedelta(days=day)

    for _, restaurant in restaurants.iterrows():

        restaurant_users = users[
            users["restaurant_id"] == restaurant["id"]
        ]

        expense_count = random.randint(3, 8)

        for _ in range(expense_count):

            category = random.choice(
                list(expense_categories.keys())
            )

            minimum, maximum = expense_categories[category]

            employee = restaurant_users.sample(1).iloc[0]

            amount = round(
                random.uniform(minimum, maximum),
                2
            )

            buffer.append({

                "id": expense_id,

                "restaurant_id": restaurant["id"],

                "user_id": employee["id"],

                "expense_date": current_date,

                "expense_category": category,

                "amount": amount,

                "payment_method": random.choice([
                    "Cash",
                    "Card",
                    "Bank Transfer",
                    "UPI"
                ]),

                "description": f"{category} Expense",

                "status": "Approved",

                "created_at": current_date,

                "updated_at": current_date

            })

            expense_id += 1

            if len(buffer) >= CHUNK_SIZE:

                append_csv(
                    pd.DataFrame(buffer),
                    "expenses.csv"
                )

                print(f"Saved {expense_id-1} expenses")

                buffer.clear()

if buffer:

    append_csv(
        pd.DataFrame(buffer),
        "expenses.csv"
    )

print(f"Finished : {expense_id-1} expenses")