import pandas as pd
import sqlite3
import os

df = pd.read_csv("data/raw/Superstore.csv", encoding="latin1")

customers = df[["Customer ID", "Customer Name", "Segment", "City", "State", "Country"]].drop_duplicates()

products = df[["Product ID", "Product Name", "Category", "Sub-Category"]].drop_duplicates()

sales = df[["Order ID", "Order Date", "Customer ID", "Product ID", "Sales", "Quantity", "Profit"]]

conn = sqlite3.connect("data/processed/business.db")
customers.to_sql("customers", conn, if_exists="replace", index=False)
products.to_sql("products", conn, if_exists="replace", index=False)
sales.to_sql("sales", conn, if_exists="replace", index=False)
conn.close()

print(f"   - {len(customers)} customers")
print(f"   - {len(products)} products")
print(f"   - {len(sales)} sales")