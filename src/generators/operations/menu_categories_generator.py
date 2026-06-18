"""
Generate Menu Categories
"""

from datetime import datetime

import pandas as pd

from src.utils.helpers import load_csv, save_csv

restaurants = load_csv("restaurants.csv")

categories = [
    "Starters",
    "Soups",
    "Salads",
    "Main Course",
    "Rice",
    "Noodles",
    "Pizza",
    "Burgers",
    "Desserts",
    "Beverages",
    "Kids Menu",
    "Combos",
]

rows = []

category_id = 1

for _, restaurant in restaurants.iterrows():

    for category in categories:

        rows.append({

            "id": category_id,

            "restaurant_id": restaurant["id"],

            "category_name": category,

            "display_order": category_id,

            "status": "Active",

            "created_at": datetime.now(),

            "updated_at": datetime.now()

        })

        category_id += 1

df = pd.DataFrame(rows)

save_csv(df, "menu_categories.csv")

print(f"Generated {len(df)} categories.")
print(df.head())