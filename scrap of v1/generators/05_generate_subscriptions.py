"""
Generate Subscription Plans.
"""

import pandas as pd

from src.utils.helpers import save_csv, print_summary

subscriptions = [
    {
        "subscription_id": 1,
        "plan_name": "Starter",
        "monthly_price": 29,
        "currency": "GBP",
        "max_restaurants": 1,
        "max_users": 10,
        "support_level": "Email",
        "analytics": False,
        "ai_features": False,
        "status": "Active"
    },
    {
        "subscription_id": 2,
        "plan_name": "Growth",
        "monthly_price": 79,
        "currency": "GBP",
        "max_restaurants": 3,
        "max_users": 30,
        "support_level": "Priority Email",
        "analytics": True,
        "ai_features": False,
        "status": "Active"
    },
    {
        "subscription_id": 3,
        "plan_name": "Professional",
        "monthly_price": 199,
        "currency": "GBP",
        "max_restaurants": 10,
        "max_users": 100,
        "support_level": "Phone",
        "analytics": True,
        "ai_features": True,
        "status": "Active"
    },
    {
        "subscription_id": 4,
        "plan_name": "Enterprise",
        "monthly_price": None,
        "currency": "GBP",
        "max_restaurants": None,
        "max_users": None,
        "support_level": "Dedicated Manager",
        "analytics": True,
        "ai_features": True,
        "status": "Custom"
    },
    {
        "subscription_id": 5,
        "plan_name": "Franchise",
        "monthly_price": None,
        "currency": "GBP",
        "max_restaurants": None,
        "max_users": None,
        "support_level": "Enterprise SLA",
        "analytics": True,
        "ai_features": True,
        "status": "Custom"
    }
]

df = pd.DataFrame(subscriptions)

save_csv(df, "subscriptions.csv")

print_summary(df, "Subscriptions")