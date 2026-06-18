"""
Generate Roles Table
"""

import pandas as pd

from src.utils.helpers import save_csv

roles = [
    {"id": 1, "department_id": 1, "name": "Admin"},
    {"id": 2, "department_id": 2, "name": "Restaurant Manager"},
    {"id": 3, "department_id": 2, "name": "Assistant Manager"},
    {"id": 4, "department_id": 3, "name": "Head Chef"},
    {"id": 5, "department_id": 3, "name": "Sous Chef"},
    {"id": 6, "department_id": 3, "name": "Chef"},
    {"id": 7, "department_id": 4, "name": "Waiter"},
    {"id": 8, "department_id": 4, "name": "Cashier"},
    {"id": 9, "department_id": 5, "name": "Accountant"},
    {"id": 10, "department_id": 6, "name": "HR Manager"},
    {"id": 11, "department_id": 7, "name": "Inventory Manager"},
    {"id": 12, "department_id": 8, "name": "Purchase Manager"},
    {"id": 13, "department_id": 9, "name": "Delivery Executive"},
    {"id": 14, "department_id": 10, "name": "System Administrator"},
]

df = pd.DataFrame(roles)

save_csv(df, "roles.csv")

print(f"Generated {len(df)} roles.")
print(df.head())