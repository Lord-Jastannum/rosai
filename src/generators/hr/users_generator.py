"""
Generate Restaurant Users
"""

import random
from datetime import datetime

import pandas as pd
from faker import Faker

from src.utils.helpers import load_csv, save_csv

random.seed(42)

fake_uk = Faker("en_GB")
fake_in = Faker("en_IN")

restaurants = load_csv("restaurants.csv")
departments = load_csv("departments.csv")
roles = load_csv("roles.csv")

users = []

employment_types = ["Full Time", "Part Time", "Contract"]

genders = ["Male", "Female"]

salary_ranges = {
    "Restaurant Manager": (60000, 90000),
    "Assistant Manager": (45000, 65000),
    "Head Chef": (50000, 80000),
    "Sous Chef": (40000, 60000),
    "Chef": (30000, 45000),
    "Waiter": (22000, 32000),
    "Cashier": (22000, 32000),
    "Accountant": (40000, 60000),
    "HR Manager": (45000, 65000),
    "Inventory Manager": (35000, 50000),
    "Purchase Manager": (35000, 50000),
    "Delivery Executive": (20000, 30000),
    "System Administrator": (50000, 70000),
    "Admin": (50000, 70000),
}

staff_structure = {
    "Restaurant Manager": 1,
    "Assistant Manager": 1,
    "Head Chef": 1,
    "Sous Chef": 2,
    "Chef": (3, 6),
    "Waiter": (6, 15),
    "Cashier": (2, 4),
    "Accountant": 1,
    "HR Manager": 1,
    "Inventory Manager": 1,
    "Purchase Manager": 1,
    "Delivery Executive": (3, 8),
    "System Administrator": 1,
}

user_id = 1

for _, restaurant in restaurants.iterrows():

    fake = fake_uk if restaurant["country"] == "United Kingdom" else fake_in

    for _, role in roles.iterrows():

        role_name = role["name"]

        if role_name not in staff_structure:
            continue

        qty = staff_structure[role_name]

        if isinstance(qty, tuple):
            qty = random.randint(qty[0], qty[1])

        salary_min, salary_max = salary_ranges[role_name]

        department_id = departments[
            departments["id"] == role["department_id"]
        ].iloc[0]["id"]

        for _ in range(qty):

            first = fake.first_name()
            last = fake.last_name()

            users.append({

                "id": user_id,

                "restaurant_id": restaurant["id"],

                "department_id": department_id,

                "role_id": role["id"],

                "employee_code": f"EMP{user_id:06d}",

                "first_name": first,

                "last_name": last,

                "full_name": f"{first} {last}",

                "gender": random.choice(genders),

                "email": fake.email(),

                "phone": fake.phone_number(),

                "employment_type": random.choice(employment_types),

                "salary": random.randint(
                    salary_min,
                    salary_max
                ),

                "joining_date": fake.date_between(
                    start_date="-5y",
                    end_date="-30d"
                ),

                "date_of_birth": fake.date_of_birth(
                    minimum_age=18,
                    maximum_age=60
                ),

                "status": "Active",

                "created_at": datetime.now(),

                "updated_at": datetime.now()

            })

            user_id += 1

df = pd.DataFrame(users)

save_csv(df, "users.csv")

print(f"Generated {len(df)} users.")
print(df.head())