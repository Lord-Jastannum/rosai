import random
from datetime import datetime

import pandas as pd
from faker import Faker

from src.utils.helpers import load_csv, save_csv

fake = Faker()

restaurants = load_csv("restaurants.csv")

categories = [
    "Vegetables",
    "Meat",
    "Seafood",
    "Dairy",
    "Beverages",
    "Bakery",
    "Cleaning",
    "Packaging",
]

suppliers = []

sid = 1

for _, restaurant in restaurants.iterrows():

    for _ in range(random.randint(8,15)):

        suppliers.append({

            "id": sid,

            "restaurant_id": restaurant["id"],

            "supplier_name": fake.company(),

            "category": random.choice(categories),

            "email": fake.company_email(),

            "phone": fake.phone_number(),

            "city": fake.city(),

            "rating": round(random.uniform(3.5,5.0),1),

            "status":"Active",

            "created_at":datetime.now(),

            "updated_at":datetime.now()

        })

        sid+=1

df=pd.DataFrame(suppliers)

save_csv(df,"suppliers.csv")

print(f"Generated {len(df)} suppliers.")
