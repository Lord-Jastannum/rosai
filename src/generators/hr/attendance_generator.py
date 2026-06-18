import random
from datetime import datetime, timedelta

import pandas as pd

from src.utils.helpers import load_csv, save_csv

random.seed(42)

users = load_csv("users.csv")

rows = []

attendance_id = 1

start_date = datetime(2025, 1, 1)

for day in range(30):

    current_date = start_date + timedelta(days=day)

    for _, user in users.iterrows():

        if random.random() < 0.05:
            status = "Absent"
            check_in = None
            check_out = None
            hours = 0

        else:

            status = "Present"

            check_in = current_date.replace(
                hour=random.randint(8,10),
                minute=random.randint(0,59)
            )

            check_out = check_in + timedelta(
                hours=random.randint(8,10),
                minutes=random.randint(0,59)
            )

            hours = round(
                (check_out-check_in).total_seconds()/3600,
                2
            )

        rows.append({

            "id": attendance_id,

            "user_id": user["id"],

            "attendance_date": current_date.date(),

            "check_in": check_in,

            "check_out": check_out,

            "working_hours": hours,

            "status": status,

            "created_at": current_date,

            "updated_at": current_date

        })

        attendance_id += 1

df = pd.DataFrame(rows)

save_csv(df, "attendance.csv")

print(f"Generated {len(df)} attendance records.")