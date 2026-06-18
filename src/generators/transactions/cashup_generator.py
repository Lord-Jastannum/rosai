import random
from datetime import datetime, timedelta

import pandas as pd

from src.utils.helpers import load_csv, append_csv

random.seed(42)

restaurants = load_csv("restaurants.csv")
users = load_csv("users.csv")
sales = load_csv("sales.csv")
payments = load_csv("payments.csv")
expenses = load_csv("expenses.csv")

CHUNK_SIZE = 500

cashup_id = 1

buffer = []

start_date = datetime(2025, 1, 1)

for day in range(30):

    business_date = start_date + timedelta(days=day)

    for _, restaurant in restaurants.iterrows():

        restaurant_sales = sales[
            (pd.to_datetime(sales["sale_datetime"]).dt.date == business_date.date())
        ]

        restaurant_orders = load_csv("orders.csv")

        restaurant_sales = restaurant_sales.merge(
            restaurant_orders[["id", "restaurant_id"]],
            left_on="order_id",
            right_on="id"
        )

        restaurant_sales = restaurant_sales[
            restaurant_sales["restaurant_id"] == restaurant["id"]
        ]

        restaurant_payments = payments[
            payments["restaurant_id"] == restaurant["id"]
        ]

        restaurant_expenses = expenses[
            (expenses["restaurant_id"] == restaurant["id"]) &
            (pd.to_datetime(expenses["expense_date"]).dt.date == business_date.date())
        ]

        restaurant_users = users[
            users["restaurant_id"] == restaurant["id"]
        ]

        if restaurant_users.empty:
            continue

        employee = restaurant_users.sample(1).iloc[0]

        cash_sales = restaurant_payments[
            restaurant_payments["payment_method"] == "Cash"
        ]["amount"].sum()

        card_sales = restaurant_payments[
            restaurant_payments["payment_method"] == "Card"
        ]["amount"].sum()

        upi_sales = restaurant_payments[
            restaurant_payments["payment_method"] == "UPI"
        ]["amount"].sum()

        online_sales = restaurant_payments[
            restaurant_payments["payment_method"] == "Online"
        ]["amount"].sum()

        expense_total = restaurant_expenses["amount"].sum()

        opening_cash = random.randint(200, 1000)

        expected_cash = opening_cash + cash_sales - expense_total

        variance = round(random.uniform(-20, 20), 2)

        closing_cash = round(expected_cash + variance, 2)

        buffer.append({

            "id": cashup_id,

            "restaurant_id": restaurant["id"],

            "user_id": employee["id"],

            "business_date": business_date.date(),

            "opening_cash": round(opening_cash, 2),

            "cash_sales": round(cash_sales, 2),

            "card_sales": round(card_sales, 2),

            "upi_sales": round(upi_sales, 2),

            "online_sales": round(online_sales, 2),

            "expenses": round(expense_total, 2),

            "expected_cash": round(expected_cash, 2),

            "actual_cash": closing_cash,

            "variance": variance,

            "status": "Closed",

            "created_at": business_date,

            "updated_at": business_date

        })

        cashup_id += 1

        if len(buffer) >= CHUNK_SIZE:

            append_csv(
                pd.DataFrame(buffer),
                "cashup.csv"
            )

            print(f"Saved {cashup_id-1} cashups")

            buffer.clear()

if buffer:

    append_csv(
        pd.DataFrame(buffer),
        "cashup.csv"
    )

print(f"Finished : {cashup_id-1} cashups")