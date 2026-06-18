"""
Generate Clients
"""

import random
from datetime import datetime

import pandas as pd
from faker import Faker

from src.utils.helpers import load_csv, save_csv

random.seed(42)

fake_uk = Faker("en_GB")
fake_in = Faker("en_IN")

subscriptions = load_csv("subscriptions.csv")

industries = [
    "Restaurant Chain",
    "Cafe",
    "Cloud Kitchen",
    "Bakery",
    "Fine Dining",
]

clients = []

for i in range(1, 31):

    country = random.choice(["United Kingdom", "India"])
    fake = fake_uk if country == "United Kingdom" else fake_in

    currency = "GBP" if country == "United Kingdom" else "INR"

    timezone = (
        "Europe/London"
        if country == "United Kingdom"
        else "Asia/Kolkata"
    )

    language = "English"

    subscription = subscriptions.sample(1).iloc[0]["id"]

    clients.append({

        "id": i,

        "client_name": fake.company(),

        "business_type": random.choice(industries),

        "subscription_id": subscription,

        "country": country,

        "currency": currency,

        "timezone": timezone,

        "language": language,

        "registration_number": fake.bothify("??######"),

        "vat_number": fake.bothify("VAT########"),

        "tax_number": fake.bothify("TAX########"),

        "website": fake.url(),

        "email": fake.company_email(),

        "phone": fake.phone_number(),

        "status": random.choice(
            ["Active", "Active", "Active", "Inactive"]
        ),

        "activation_date": fake.date_between(
            start_date="-5y",
            end_date="-1y",
        ),

        "created_at": datetime.now(),

        "updated_at": datetime.now()

    })

df = pd.DataFrame(clients)

save_csv(df, "clients.csv")

print(f"Generated {len(df)} clients.")
print(df.head())