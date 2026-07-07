import datetime
import sqlite3 as pl
from pathlib import Path
import pandas as pd
import psycopg2

ROOT = Path ("lillmossi/Documents/github/Probability_model_for_football")

ROOT = Path(__file__).resolve().parents[1]

files = list((ROOT / "data").glob("*.csv"))
print(f"Found {len(files)} files")
frames = []
for f in files:
    try:
        df = pd.read_csv(f)
        df["source_file"] = f.name
        frames.append(df)

    except Exception as e:
        print(f"failed on {f.name}: {e}")
        raise

# 4. Combine into one DataFrame
all_data = pd.concat(frames, ignore_index=True)

# 5. Sanity check
print(f"Total rows: {len(all_data)}")
print(f"Columns: {all_data.shape[1]}")
print(all_data["source_file"].value_counts().head())

#### connection to supabase data base
conn = psycopg2.connect(
    host="db.ajhirbjxovrabofnbpgl.supabase.co",
    port=5432,
    db="postgresql+psycopg://postgres:[Lillmossi12?]@db.ajhirbjxovrabofnbpgl.supabase.co:5432/postgres",
    user="postgres",
    password="",
)
query = """""SELECT * FROM web_logs WHERE timestamp >= NOW() - INTERVAL '24 hours'"""""
df_logs = pl.read_database(query=query, connection=conn)

conn.close()

print(df_logs.shape)

def valdate(df):
    try:
