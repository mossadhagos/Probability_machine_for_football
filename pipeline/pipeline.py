from pathlib import Path
import pandas as pd


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



