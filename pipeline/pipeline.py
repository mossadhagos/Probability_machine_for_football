from pathlib import Path
import pandas as pd

# 1. Anchor the path so it works no matter where you run from
ROOT = Path(__file__)   # <-- fix bug #1

# 2. Find all CSVs
files = list((ROOT / "data").glob("*.csv"))
print(f"Found {len(files)} files")   # sanity check — should print 34

# 3. Read each file into a list of DataFrames
frames = []
for f in files:
    try:
        df = pd.read_csv(f)
        df["source_file"] = f.name        # keep track of which file each row came from
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