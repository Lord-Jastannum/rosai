"""
Central CSV loader.
"""

from src.utils.helpers import load_csv


def restaurants():
    return load_csv("restaurants.csv")


def users():
    return load_csv("users.csv")


def clients():
    return load_csv("clients.csv")


def departments():
    return load_csv("departments.csv")


def roles():
    return load_csv("roles.csv")


def pdq():
    return load_csv("pdqmachines.csv")