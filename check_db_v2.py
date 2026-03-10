import sqlite3
import pandas as pd

conn = sqlite3.connect('compdb.db')
df = pd.read_sql_query("SELECT * FROM roster_details LIMIT 5", conn)
print("Columns:", df.columns.tolist())
print(df.head())
conn.close()
