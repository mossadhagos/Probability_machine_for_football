from pathlib import Path
import pandas as pd

# 1. Anchor the path so it works no matter where you run from
ROOT = Path ("lillmossi/Documents/github/Probability_model_for_football") # <-- fix bug

ROOT = Path(__file__).resolve().parents[1]

files = list((ROOT / "data").glob("*.csv"))
print(f"Found {len(files)} files")   # sanity check — should print 34


for f in files:
    df = pd.read_csv(f)
    dates = pd.to_datetime(df["date"], format="%Y, %m, %d", errors="coerce")
    print(f"{f.name:20s} rows: {len(df):4d} first= {dates.min().date} last={dates.max}")

frames = []
for f in files:
    try:
        df = pd.read_csv(f)
        df["source_file"] = f.name
        frames.append(df) # keep track of which file each row came from
                                          # <-- fix bug #2 (add df to frames)
    except Exception as e:
        print(f"failed on {f.name}: {e}")
        raise

# 4. Combine into one DataFrame
all_data = pd.concat(frames, ignore_index=True)

# 5. Sanity check
print(f"Total rows: {len(all_data)}")
print(f"Columns: {all_data.shape[1]}")
print(all_data["source_file"].value_counts().head())


def validate(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    df = df.copy()

