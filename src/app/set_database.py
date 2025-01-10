import sqlite3

from definitions import DATABASE_PATH

if not DATABASE_PATH.exists():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.close()
