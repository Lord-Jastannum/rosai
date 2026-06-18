import random
from datetime import datetime

import pandas as pd

from src.utils.helpers import load_csv, save_csv

random.seed(42)

cashups = load_csv("cashup.csv")

notes = [
    "Cash verified successfully.",
    "Minor cash variance observed.",
    "Manager approved closing balance.",
    "PDQ totals reconciled.",
    "Cash deposited to bank.",
    "Closing completed without issues.",
    "Customer refund processed.",
    "Additional float added.",
    "Variance investigated.",
    "Daily reconciliation completed."
]

rows = []

note_id = 1

for _, cashup in cashups.iterrows():

    count = random.randint(1, 3)

    for _ in range(count):

        rows.append({

            "id": note_id,

            "cashup_id": cashup["id"],

            "note": random.choice(notes),

            "created_by": cashup["user_id"],

            "created_at": datetime.now()

        })

        note_id += 1

df = pd.DataFrame(rows)

save_csv(df, "cashup_notes.csv")

print(f"Generated {len(df)} cashup notes.")