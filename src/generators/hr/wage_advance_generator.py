import random
from datetime import datetime, timedelta

import pandas as pd

from src.utils.helpers import load_csv, save_csv

random.seed(42)

users = load_csv("users.csv")

rows = []

advance_id = 1

for _, user in users.iterrows():

    if random.random() > 0.15:
        continue

    request = datetime.now() - timedelta(
        days=random.randint(1,180)
    )

    approval = request + timedelta(
        days=random.randint(0,5)
    )

    amount = round(
        user["salary"] * random.uniform(0.1,0.5),
        2
    )

    rows.append({

        "id": advance_id,

        "user_id": user["id"],

        "request_date": request.date(),

        "approved_date": approval.date(),

        "amount": amount,

        "reason": random.choice([
            "Medical",
            "Emergency",
            "Education",
            "Family",
            "Personal"
        ]),

        "approved_by": random.randint(1,50),

        "status": random.choice([
            "Approved",
            "Approved",
            "Rejected"
        ]),

        "created_at": request,

        "updated_at": approval

    })

    advance_id += 1

df = pd.DataFrame(rows)

save_csv(df, "wage_advance.csv")

print(f"Generated {len(df)} wage advances.")