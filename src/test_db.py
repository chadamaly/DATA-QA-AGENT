import sqlite3

conn = sqlite3.connect("data/processed/business.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM sales")
print("Number of orders :", cursor.fetchone()[0])

cursor.execute('SELECT "Customer Name" FROM customers LIMIT 5')
print("5 customers names :", cursor.fetchall())

conn.close()