"""
Generate Primary Contacts.
Each client gets one primary business contact.
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

clients = load_csv("clients.csv")

designations = [
    "Owner",
    "Managing Director",
    "CEO",
    "Finance Manager",
    "Operations Manager",
]

contacts = []

contact_id = 5001

for _, client in clients.iterrows():

    fake = get_faker(client["country"])

    contacts.append({

        "contact_id": contact_id,

        "client_id": client["client_id"],

        "first_name": fake.first_name(),

        "last_name": fake.last_name(),

        "designation": random.choice(designations),

        "email": fake.company_email(),

        "phone": fake.phone_number(),

        "secondary_phone": fake.phone_number(),

        "preferred_contact_method": random.choice([
            "Email",
            "Phone"
        ]),

        "verified": random.choice([
            True,
            True,
            True,
            False
        ]),

        "status": "Active"

    })

    contact_id += 1

df = pd.DataFrame(contacts)

save_csv(df, "primary_contacts.csv")

print_summary(df, "Primary Contacts")
