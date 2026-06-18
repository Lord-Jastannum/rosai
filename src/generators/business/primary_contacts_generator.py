"""
Generate Primary Contacts
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

designations = [
    "Owner",
    "CEO",
    "Managing Director",
    "Operations Manager",
    "Finance Director",
]

contacts = []

for _, client in clients.iterrows():

    fake = fake_uk if client["country"] == "United Kingdom" else fake_in

    contacts.append({

        "id": len(contacts) + 1,

        "client_id": client["id"],

        "first_name": fake.first_name(),

        "last_name": fake.last_name(),

        "designation": random.choice(designations),

        "email": fake.company_email(),

        "phone": fake.phone_number(),

        "alternate_phone": fake.phone_number(),

        "preferred_contact": random.choice(
            ["Email", "Phone"]
        ),

        "verified": random.choice(
            [True, True, True, False]
        ),

        "status": "Active",

        "created_at": datetime.now(),

        "updated_at": datetime.now()

    })

df = pd.DataFrame(contacts)

save_csv(df, "primary_contacts.csv")

print(f"Generated {len(df)} primary contacts.")
print(df.head())