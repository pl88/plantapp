from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.parent
DATASETS_DIR = ROOT_DIR / "datasets"

DATABASE_PATH = DATASETS_DIR / "plants.db"
PLANTS_CSVTABLE_PATH = DATASETS_DIR / "plantInfo-clean.csv"
