"""
Generate Restaurants
"""

import random
from datetime import datetime

import pandas as pd
from faker import Faker

from src.utils.helpers import load_csv, save_csv

random.seed(42)

fake_uk = Faker("en_GB")
fake_in = Faker("en_IN")

clients = load_csv("clients.csv")

restaurant_types = [
    "Fine Dining",
    "Casual Dining",
    "Cafe",
    "Fast Food",
    "Cloud Kitchen",
    "Bakery",
]

cuisines = [
    "Indian",
    "Italian",
    "Chinese",
    "Mexican",
    "Thai",
    "Japanese",
    "British",
    "American",
]

restaurants = []

restaurant_id = 1

for _, client in clients.iterrows():

    fake = fake_uk if client["country"] == "United Kingdom" else fake_in

    count = random.randint(1, 4)

    for _ in range(count):

        restaurants.append({

            "id": restaurant_id,

            "client_id": client["id"],

            "restaurant_name": fake.company(),

            "restaurant_type": random.choice(restaurant_types),

            "cuisine": random.choice(cuisines),

            "country": client["country"],

            "currency": client["currency"],

            "city": fake.city(),

            "postcode": fake.postcode(),

            "address": fake.address().replace("\n", ", "),

            "phone": fake.phone_number(),

            "email": fake.company_email(),

            "opening_time": "09:00",

            "closing_time": "22:00",

            "seating_capacity": random.randint(30, 250),

            "delivery_available": random.choice([True, False]),

            "takeaway_available": random.choice([True, False]),

            "average_daily_customers": random.randint(80, 600),

            "average_order_value": round(
                random.uniform(12, 60),
                2
            ),

            "google_rating": round(
                random.uniform(3.5, 5.0),
                1
            ),

            "status": "Active",

            "created_at": datetime.now(),

            "updated_at": datetime.now()

        })

        restaurant_id += 1

df = pd.DataFrame(restaurants)

save_csv(df, "restaurants.csv")

print(f"Generated {len(df)} restaurants.")
print(df.head())