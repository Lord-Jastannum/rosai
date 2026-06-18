import random
from datetime import datetime

import pandas as pd
from faker import Faker

from src.utils.helpers import load_csv, save_csv

random.seed(42)

fake_uk = Faker("en_GB")
fake_in = Faker("en_IN")

restaurants = load_csv("restaurants.csv")

customers = []

customer_id = 1

for _, restaurant in restaurants.iterrows():

    fake = fake_uk if restaurant["country"] == "United Kingdom" else fake_in

    count = random.randint(500, 1200)

    for _ in range(count):

        first = fake.first_name()
        last = fake.last_name()

        customers.append({

            "id": customer_id,

            "restaurant_id": restaurant["id"],

            "customer_code": f"CUST{customer_id:07d}",

            "first_name": first,

            "last_name": last,

            "full_name": f"{first} {last}",

            "gender": random.choice(["Male", "Female"]),

            "email": fake.email(),

            "phone": fake.phone_number(),

            "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=80),

            "loyalty_points": random.randint(0, 5000),

            "vip": random.random() < 0.05,

            "status": "Active",

            "created_at": datetime.now(),

            "updated_at": datetime.now()

        })

        customer_id += 1

df = pd.DataFrame(customers)

save_csv(df, "customers.csv")

print(f"Generated {len(df)} customers.")
