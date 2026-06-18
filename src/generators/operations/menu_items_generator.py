"""
Generate Menu Items
"""

import random
from datetime import datetime

import pandas as pd

from src.utils.helpers import load_csv, save_csv

random.seed(42)

restaurants = load_csv("restaurants.csv")
categories = load_csv("menu_categories.csv")

menu_items = [
    ("Margherita Pizza","Pizza",12,8),
    ("Pepperoni Pizza","Pizza",15,10),
    ("Veg Burger","Burgers",8,5),
    ("Chicken Burger","Burgers",10,6),
    ("French Fries","Starters",5,2),
    ("Garlic Bread","Starters",6,2),
    ("Paneer Butter Masala","Main Course",14,8),
    ("Butter Chicken","Main Course",16,9),
    ("Chicken Biryani","Rice",15,8),
    ("Veg Fried Rice","Rice",10,5),
    ("Hakka Noodles","Noodles",11,5),
    ("Chocolate Brownie","Desserts",7,3),
    ("Ice Cream","Desserts",5,2),
    ("Coffee","Beverages",4,1),
    ("Tea","Beverages",3,1),
    ("Fresh Lime Soda","Beverages",5,2),
]

rows=[]

item_id=1

for _, restaurant in restaurants.iterrows():

    restaurant_categories = categories[
        categories["restaurant_id"]==restaurant["id"]
    ]

    for _ in range(random.randint(80,120)):

        item=random.choice(menu_items)

        category = restaurant_categories[
            restaurant_categories["category_name"]==item[1]
        ]

        if category.empty:
            continue

        category_id=category.iloc[0]["id"]

        selling=round(random.uniform(item[2],item[2]+10),2)

        cost=round(random.uniform(item[3],selling-1),2)

        rows.append({

            "id":item_id,

            "restaurant_id":restaurant["id"],

            "category_id":category_id,

            "item_name":item[0],

            "description":f"Freshly prepared {item[0]}",

            "price":selling,

            "cost_price":cost,

            "profit":round(selling-cost,2),

            "prep_time":random.randint(5,30),

            "calories":random.randint(150,900),

            "is_veg":random.choice([True,False]),

            "is_available":True,

            "status":"Active",

            "created_at":datetime.now(),

            "updated_at":datetime.now()

        })

        item_id+=1

df=pd.DataFrame(rows)

save_csv(df,"menu_items.csv")

print(f"Generated {len(df)} menu items.")
print(df.head())