import pandas as pd
from pathlib import Path

from pipeline.pipeline import dates

ROOT = Path ("lillmossi/Documents/github/Probability_model_for_football") # <-- fix bug

ROOT = Path(__file__).resolve().parents[1]

files = list((ROOT / "data").glob("*.csv"))
print(f"Found {len(files)} files")   # sanity check — should print 34


first = dates.min()
season_start = first.year if first.month >= 8 else first.year - 1
season_end_2digit = str(season_start + 1)[-2:]
season = f"{season_start}-{season_end_2digit}"

league = f.stem.split(" ")[0]

new_name = f"{league}_{season}"
new_name = new_name.replace(" ", "_")
new_name = new_name.replace("-", "_")
new_name = new_name.replace(" ", "_")
new_name = new_name.replace("-", "_")
new_name = new_name.replace(" ", "_")

