"""
Generate Restaurant Users.
"""

import random

import pandas as pd

from src.utils.faker_utils import get_faker
from src.utils.helpers import (
    load_csv,
    save_csv,
    print_summary,
)

random.seed(42)

restaurants = load_csv("restaurants.csv")
departments = load_csv("departments.csv")
roles = load_csv("roles.csv")

users = []

user_id = 3001

employment_types = [
    "Full Time",
    "Part Time"
]

genders = [
    "Male",
    "Female"
]

for _, restaurant in restaurants.iterrows():

    fake = get_faker(restaurant["country"])

    manager_count = 1
    cashier_count = random.randint(2, 4)
    chef_count = random.randint(3, 8)
    waiter_count = random.randint(5, 15)
    delivery_count = random.randint(2, 8)

    staff = [
        ("Manager", manager_count),
        ("Cashier", cashier_count),
        ("Chef", chef_count),
        ("Waiter", waiter_count),
        ("Delivery Executive", delivery_count),
    ]

    for role_name, count in staff:

        role_row = roles[
            roles["role_name"] == role_name
        ]

        if role_row.empty:
            continue

        role_id = role_row.iloc[0]["role_id"]

        department_id = role_row.iloc[0]["department_id"]

        for _ in range(count):

            users.append({

                "user_id": user_id,

                "restaurant_id": restaurant["restaurant_id"],

                "department_id": department_id,

                "role_id": role_id,

                "first_name": fake.first_name(),

                "last_name": fake.last_name(),

                "gender": random.choice(genders),

                "email": fake.email(),

                "phone": fake.phone_number(),

                "employment_type": random.choice(
                    employment_types
                ),

                "salary": random.randint(
                    22000,
                    90000
                ),

                "joining_date": fake.date_between(
                    start_date="-3y",
                    end_date="-30d"
                ),

                "status": "Active"

            })

            user_id += 1

df = pd.DataFrame(users)

save_csv(df, "users.csv")

print_summary(df, "Users")
