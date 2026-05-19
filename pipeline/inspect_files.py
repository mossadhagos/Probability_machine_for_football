import pandas as pd
from pathlib import Path

ROOT = Path ("lillmossi/Documents/github/Probability_model_for_football") # <-- fix bug

ROOT = Path(__file__).resolve().parents[1]

files = list((ROOT / "data").glob("*.csv"))
print(f"Found {len(files)} files")   # sanity check — should print 34


for f in files:
    df = pd.read_csv(f)
    dates = pd.to_datetime(df["Date"], format="%Y %m %d", errors="coerce")
    dates = pd.to_datetime(df["Date"], dayfirst=True, errors="coerce")
    print(f"{f.name:20s} rows: {len(df):4d} first= {dates.min().date} last={dates.max().date()}")
    #                                                              ^
    #                                                       missing () here


