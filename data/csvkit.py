import pandas as pd

df = pd.read_csv("/Users/lillmossi/Documents/github/Probability_model_for_football/data/E0.csv")

print("Shape:", df.shape)
print("\nDate column type:")
print(df["Date"].dtype)
print("\nFirst 5 dates:")
print(df["Date"].head())
print("\nFirst 5 home teams:")
print(df["HomeTeam"].head())