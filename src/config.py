"""
Global project configuration.

Every generator imports this file instead of hardcoding paths.
"""

from pathlib import Path

# -----------------------------------------------------------------------------
# Base Directories
# -----------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

CLEANED_DATA_DIR = DATA_DIR / "cleaned"

GENERATED_DATA_DIR = DATA_DIR / "generated"

# -----------------------------------------------------------------------------
# Dataset
# -----------------------------------------------------------------------------

RAW_EXCEL_FILE = RAW_DATA_DIR / "ROS_Dataset.xlsx"

# -----------------------------------------------------------------------------
# Countries
# -----------------------------------------------------------------------------

SUPPORTED_COUNTRIES = [
    "UK",
    "India"
]

COUNTRY_CURRENCY = {
    "UK": "GBP",
    "India": "INR"
}

COUNTRY_LOCALE = {
    "UK": "en_GB",
    "India": "en_IN"
}

# -----------------------------------------------------------------------------
# Randomness
# -----------------------------------------------------------------------------

RANDOM_SEED = 42

# -----------------------------------------------------------------------------
# Generation Years
# -----------------------------------------------------------------------------

START_YEAR = 2022
END_YEAR = 2025