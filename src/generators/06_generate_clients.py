"""
Generate Clients.

Each client represents a restaurant business using the platform.
"""

import random

import pandas as pd

from src.config import COUNTRY_CURRENCY
from src.utils.faker_utils import get_faker
from src.utils.helpers import save_csv, print_summary

random.seed(42)

clients = []

client_id = 1001

subscription_ids = [1, 2, 3, 4, 5]

industries = [
    "Restaurant",
    "Cafe",
    "Cloud Kitchen",
    "Bakery",
    "Food Court"
]

languages = {
    "UK": "English",
    "India": "English"
}

timezones = {
    "UK": "Europe/London",
    "India": "Asia/Kolkata"
}

for i in range(30):

    country = "UK" if i < 20 else "India"

    fake = get_faker(country)

    activation_date = fake.date_between(
        start_date="-4y",
        end_date="-2y"
    )

    active = random.random() > 0.10

    clients.append({

        "client_id": client_id,

        "client_name": fake.company(),

        "industry": random.choice(industries),

        "country": country,

        "currency": COUNTRY_CURRENCY[country],

        "language": languages[country],

        "timezone": timezones[country],

        "subscription_id": random.choice(subscription_ids),

        "registration_number": fake.bothify(
            text="??######"
        ),

        "vat_number": fake.bothify(
            text="VAT######"
        ),

        "financial_year_start": "01-Apr",

        "status": "Active" if active else "Inactive",

        "activation_date": activation_date,

        "inactivation_date":
            None if active else fake.date_between(
                start_date=activation_date,
                end_date="-30d"
            )
    })

    client_id += 1

df = pd.DataFrame(clients)

save_csv(df, "clients.csv")

print_summary(df, "Clients")