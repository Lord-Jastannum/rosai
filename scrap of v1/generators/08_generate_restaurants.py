"""
Generate Restaurants.
"""

import random

import pandas as pd

from src.config import COUNTRY_CURRENCY
from src.utils.faker_utils import get_faker
from src.utils.helpers import (
    load_csv,
    save_csv,
    print_summary,
)

random.seed(42)

clients = load_csv("clients.csv")

restaurant_types = [
    "Fine Dining",
    "Casual Dining",
    "Cafe",
    "Fast Food",
    "Cloud Kitchen",
]

cuisines = [
    "Indian",
    "Chinese",
    "Italian",
    "Mexican",
    "Thai",
    "Japanese",
    "British",
    "American",
]

restaurants = []

restaurant_id = 2001

for _, client in clients.iterrows():

    if client["status"] != "Active":
        continue

    if client["country"] == "UK":
        count = random.randint(2, 4)
    else:
        count = random.randint(1, 3)

    fake = get_faker(client["country"])

    for _ in range(count):

        restaurants.append({

            "restaurant_id": restaurant_id,

            "client_id": client["client_id"],

            "restaurant_name": fake.company() + " Restaurant",

            "restaurant_type": random.choice(
                restaurant_types
            ),

            "cuisine": random.choice(cuisines),

            "country": client["country"],

            "currency": COUNTRY_CURRENCY[
                client["country"]
            ],

            "city": fake.city(),

            "postcode": fake.postcode(),

            "address": fake.address().replace("\n", ", "),

            "phone": fake.phone_number(),

            "email": fake.company_email(),

            "opening_time": "09:00",

            "closing_time": "22:00",

            "seating_capacity": random.randint(
                20,
                200
            ),

            "delivery_available": random.choice([
                True,
                False
            ]),

            "takeaway_available": random.choice([
                True,
                False
            ]),

            "average_daily_customers": random.randint(
                80,
                500
            ),

            "rating": round(
                random.uniform(3.5, 5.0),
                1
            ),

            "status": "Active",

            "activation_date": client[
                "activation_date"
            ]

        })

        restaurant_id += 1

df = pd.DataFrame(restaurants)

save_csv(df, "restaurants.csv")

print_summary(df, "Restaurants")
