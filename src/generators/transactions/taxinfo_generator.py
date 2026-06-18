import random
from datetime import datetime

import pandas as pd

from src.utils.helpers import load_csv, save_csv

random.seed(42)

restaurants = load_csv("restaurants.csv")

rows = []

tax_id = 1

tax_rates = {
    "United Kingdom": 20.0,
    "India": 18.0,
}

for _, restaurant in restaurants.iterrows():

    rows.append({

        "id": tax_id,

        "restaurant_id": restaurant["id"],

        "tax_name": "VAT" if restaurant["country"] == "United Kingdom" else "GST",

        "tax_percentage": tax_rates.get(
            restaurant["country"],
            18.0
        ),

        "tax_registration_number": f"TAX{tax_id:08d}",

        "effective_from": "2025-01-01",

        "status": "Active",

        "created_at": datetime.now(),

        "updated_at": datetime.now()

    })

    tax_id += 1

df = pd.DataFrame(rows)

save_csv(df, "taxinfo.csv")

print(f"Generated {len(df)} tax records.")
