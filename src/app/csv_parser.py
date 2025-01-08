import sqlite3
import pandas as pd

from pathlib import Path

from definitions import ROOT_DIR

DATASETS_DIR = ROOT_DIR / "datasets"

database_path = DATASETS_DIR / "plants.db"
plants_csvtable_path = DATASETS_DIR / "plantInfo-clean.csv"

if not database_path.exists():
    conn = sqlite3.connect(database_path)

if plants_csvtable_path.exists():
    plant_data = pd.read_csv(plants_csvtable_path)
    plant_data.to_sql("plants", conn, if_exists="replace", index=False)
else:
    print("No csv file found")
    conn.close()
    exit()

cur = conn.cursor()

print(cur.execute("SELECT * FROM plants").fetchall())

conn.close()
