from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"

GENERATED_DIR = DATA_DIR / "generated"

RAW_DIR = DATA_DIR / "raw"