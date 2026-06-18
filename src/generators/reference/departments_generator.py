"""
Generate Departments Table
"""

import pandas as pd

from src.utils.helpers import save_csv

departments = [
    {"id": 1, "name": "Administration", "status": "Active"},
    {"id": 2, "name": "Operations", "status": "Active"},
    {"id": 3, "name": "Kitchen", "status": "Active"},
    {"id": 4, "name": "Service", "status": "Active"},
    {"id": 5, "name": "Finance", "status": "Active"},
    {"id": 6, "name": "Human Resources", "status": "Active"},
    {"id": 7, "name": "Inventory", "status": "Active"},
    {"id": 8, "name": "Procurement", "status": "Active"},
    {"id": 9, "name": "Delivery", "status": "Active"},
    {"id": 10, "name": "IT", "status": "Active"},
]

df = pd.DataFrame(departments)

save_csv(df, "departments.csv")

print(f"Generated {len(df)} departments.")
print(df.head())