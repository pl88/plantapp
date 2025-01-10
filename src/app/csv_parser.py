import sqlite3
import pandas as pd

from definitions import DATABASE_PATH, PLANTS_CSVTABLE_PATH

if DATABASE_PATH.exists():
    conn = sqlite3.connect(DATABASE_PATH)
else:
    print("No database file found")
    exit()

if PLANTS_CSVTABLE_PATH.exists():
    plant_data = pd.read_csv(PLANTS_CSVTABLE_PATH)
    plant_data.to_sql("plants", conn, if_exists="replace", index=False)
else:
    print("No csv file found")
    conn.close()
    exit()

cur = conn.cursor()

print(cur.execute("SELECT * FROM plants").fetchall())

conn.close()
