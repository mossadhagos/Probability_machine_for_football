import pandas as pd
from pathlib import Path

from pipeline.inspect_files import dates

ROOT = Path ("lillmossi/Documents/github/Probability_model_for_football")

ROOT = Path(__file__).resolve().parents[1]

files = list((ROOT / "data").glob("*.csv"))
print(f"Found {len(files)} files")


first = dates.min()
season_start = first.year if first.month >= 8 else first.year - 1
season_end_2digit = str(season_start + 1)[-2:]
season = f"{season_start}-{season_end_2digit}"

league = f.stem.split("_")[0]
new_name = f"{league}_{season}"
new_name = new_name.replace("E0 ",  "Premier_league")
new_name = new_name.replace("D1", "Bundes_league")
new_name = new_name.replace("F1 ", "Ligue_1")
new_name = new_name.replace("I1", "Serie_A")
new_name = new_name.replace("SP1", "La_liga")



