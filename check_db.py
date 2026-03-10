import sqlite3
import pandas as pd

conn = sqlite3.connect('compdb.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print(f"Tables: {tables}")

if ('roster_details',) in tables:
    cursor.execute("PRAGMA table_info(roster_details);")
    columns = cursor.fetchall()
    print(f"Columns in roster_details: {columns}")
else:
    print("roster_details table not found")

conn.close()
