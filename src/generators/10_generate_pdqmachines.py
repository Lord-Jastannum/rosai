"""
Generate PDQ Machines.
"""

import random

import pandas as pd

from faker import Faker

from src.utils.helpers import (
    load_csv,
    save_csv,
    print_summary,
)

fake = Faker()

random.seed(42)

restaurants = load_csv("restaurants.csv")

machines = []

machine_id = 6001

providers = [
    "Square",
    "Stripe",
    "Worldpay",
    "Barclaycard",
    "Razorpay"
]

statuses = [
    "Active",
    "Maintenance",
    "Inactive"
]

for _, restaurant in restaurants.iterrows():

    count = random.randint(1, 3)

    for _ in range(count):

        machines.append({

            "machine_id": machine_id,

            "restaurant_id": restaurant["restaurant_id"],

            "provider": random.choice(providers),

            "serial_number": fake.unique.bothify(
                text="PDQ########"
            ),

            "installation_date": fake.date_between(
                start_date="-4y",
                end_date="-1y"
            ),

            "status": random.choices(
                statuses,
                weights=[90, 8, 2]
            )[0]

        })

        machine_id += 1

df = pd.DataFrame(machines)

save_csv(df, "pdqmachines.csv")

print_summary(df, "PDQ Machines")
