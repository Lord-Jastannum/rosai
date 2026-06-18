"""
Generate Subscription Plans
"""

import pandas as pd

from src.utils.helpers import save_csv

subscriptions = [
    {
        "id": 1,
        "plan_name": "Starter",
        "monthly_price": 29.99,
        "currency": "GBP",
        "max_restaurants": 1,
        "max_users": 10,
        "analytics_enabled": False,
        "ai_enabled": False,
        "support_level": "Email",
        "status": "Active",
    },
    {
        "id": 2,
        "plan_name": "Growth",
        "monthly_price": 79.99,
        "currency": "GBP",
        "max_restaurants": 3,
        "max_users": 50,
        "analytics_enabled": True,
        "ai_enabled": False,
        "support_level": "Priority Email",
        "status": "Active",
    },
    {
        "id": 3,
        "plan_name": "Professional",
        "monthly_price": 199.99,
        "currency": "GBP",
        "max_restaurants": 10,
        "max_users": 200,
        "analytics_enabled": True,
        "ai_enabled": True,
        "support_level": "Phone",
        "status": "Active",
    },
    {
        "id": 4,
        "plan_name": "Enterprise",
        "monthly_price": 499.99,
        "currency": "GBP",
        "max_restaurants": 50,
        "max_users": 1000,
        "analytics_enabled": True,
        "ai_enabled": True,
        "support_level": "Dedicated Manager",
        "status": "Active",
    },
    {
        "id": 5,
        "plan_name": "Custom",
        "monthly_price": None,
        "currency": "GBP",
        "max_restaurants": None,
        "max_users": None,
        "analytics_enabled": True,
        "ai_enabled": True,
        "support_level": "Custom SLA",
        "status": "Custom",
    },
]

df = pd.DataFrame(subscriptions)

save_csv(df, "subscriptions.csv")

print(f"Generated {len(df)} subscriptions.")
print(df.head())