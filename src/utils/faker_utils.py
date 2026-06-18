"""
Central Faker configuration.

Never instantiate Faker inside generators.
Import from this module instead.
"""

import random

from faker import Faker

from src.config import RANDOM_SEED

# --------------------------------------------------------------------------

random.seed(RANDOM_SEED)

Faker.seed(RANDOM_SEED)

# --------------------------------------------------------------------------

fake_uk = Faker("en_GB")
fake_india = Faker("en_IN")

# --------------------------------------------------------------------------

LOCALE_MAP = {
    "UK": fake_uk,
    "India": fake_india
}


def get_faker(country: str) -> Faker:
    """
    Return faker object according to country.
    """

    return LOCALE_MAP[country]
