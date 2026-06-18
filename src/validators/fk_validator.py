import pandas as pd

from src.utils.helpers import load_csv

tables = {
    "clients": load_csv("clients.csv"),
    "restaurants": load_csv("restaurants.csv"),
    "users": load_csv("users.csv"),
    "customers": load_csv("customers.csv"),
    "orders": load_csv("orders.csv"),
    "order_items": load_csv("order_items.csv"),
    "sales": load_csv("sales.csv"),
    "payments": load_csv("payments.csv"),
}

checks = [

    ("restaurants","client_id","clients"),

    ("users","restaurant_id","restaurants"),

    ("customers","restaurant_id","restaurants"),

    ("orders","restaurant_id","restaurants"),

    ("orders","customer_id","customers"),

    ("orders","user_id","users"),

    ("order_items","order_id","orders"),

    ("sales","order_id","orders"),

    ("payments","sale_id","sales")

]

print("="*60)

print("FOREIGN KEY VALIDATION")

print("="*60)

for child,fk,parent in checks:

    parent_ids = set(tables[parent]["id"])

    invalid = ~tables[child][fk].isin(parent_ids)

    errors = invalid.sum()

    print(f"{child}.{fk} -> {parent}.id : {errors} errors")