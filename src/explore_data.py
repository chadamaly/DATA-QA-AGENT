import pandas as pd

df = pd.read_csv("data/raw/Superstore.csv", encoding="latin1")

print("Available columns :")
print(df.columns.tolist())
print("\nNumber of rows :", len(df))
print("\nData preview : ")
print(df.head())