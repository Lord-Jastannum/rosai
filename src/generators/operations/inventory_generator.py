"""
Generate Inventory Items
"""

import random
from datetime import datetime

import pandas as pd

from src.utils.helpers import load_csv, save_csv

random.seed(42)

restaurants = load_csv("restaurants.csv")
suppliers = load_csv("suppliers.csv")

inventory_items = [
    ("Tomatoes", "Vegetables", "kg"),
    ("Onions", "Vegetables", "kg"),
    ("Potatoes", "Vegetables", "kg"),
    ("Chicken Breast", "Meat", "kg"),
    ("Mutton", "Meat", "kg"),
    ("Fish", "Seafood", "kg"),
    ("Rice", "Grains", "kg"),
    ("Flour", "Grains", "kg"),
    ("Sugar", "Groceries", "kg"),
    ("Salt", "Groceries", "kg"),
    ("Milk", "Dairy", "litre"),
    ("Cheese", "Dairy", "kg"),
    ("Butter", "Dairy", "kg"),
    ("Cooking Oil", "Groceries", "litre"),
    ("Eggs", "Dairy", "dozen"),
    ("Coffee Beans", "Beverages", "kg"),
    ("Tea Leaves", "Beverages", "kg"),
    ("Soft Drinks", "Beverages", "case"),
    ("Mineral Water", "Beverages", "case"),
    ("Cleaning Liquid", "Cleaning", "litre"),
]

inventory = []

inventory_id = 1

for _, restaurant in restaurants.iterrows():

    restaurant_suppliers = suppliers[
        suppliers["restaurant_id"] == restaurant["id"]
    ]

    for _ in range(150):

        item = random.choice(inventory_items)

        supplier = restaurant_suppliers.sample(1).iloc[0]

        minimum = random.randint(10, 40)

        maximum = minimum + random.randint(50, 200)

        quantity = random.randint(minimum, maximum)

        cost = round(random.uniform(1, 250), 2)

        inventory.append({

            "id": inventory_id,

            "restaurant_id": restaurant["id"],

            "supplier_id": supplier["id"],

            "item_name": item[0],

            "category": item[1],

            "unit": item[2],

            "quantity": quantity,

            "minimum_stock": minimum,

            "maximum_stock": maximum,

            "unit_cost": cost,

            "inventory_value": round(quantity * cost, 2),

            "status": "Active",

            "created_at": datetime.now(),

            "updated_at": datetime.now()

        })

        inventory_id += 1

df = pd.DataFrame(inventory)

save_csv(df, "inventory.csv")

print(f"Generated {len(df)} inventory items.")
print(df.head())
