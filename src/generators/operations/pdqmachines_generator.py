import random
from datetime import datetime

import pandas as pd

from src.utils.helpers import load_csv, save_csv

random.seed(42)

restaurants = load_csv("restaurants.csv")

providers = [
    "Square",
    "Stripe",
    "Worldpay",
    "Barclays",
    "Razorpay",
]

rows = []

machine_id = 1

for _, restaurant in restaurants.iterrows():

    count = random.randint(1, 3)

    for _ in range(count):

        rows.append({

            "id": machine_id,

            "restaurant_id": restaurant["id"],

            "provider": random.choice(providers),

            "serial_number": f"PDQ{machine_id:08d}",

            "installation_date": datetime.now().date(),

            "status": "Active",

            "created_at": datetime.now(),

            "updated_at": datetime.now()

        })

        machine_id += 1

df = pd.DataFrame(rows)

save_csv(df, "pdqmachines.csv")

print(f"Generated {len(df)} PDQ Machines.")