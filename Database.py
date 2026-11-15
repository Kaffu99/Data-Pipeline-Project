import sqlite3
import csv

with open("Filtered_data.csv",mode="r") as file:
    csv_reader=csv.reader(file)
    next(csv_reader)
    all_rows=list(csv_reader)

connection=sqlite3.connect("Database.db")
cursor=connection.cursor()

cursor.execute("""
                create table if not exists Filtered_data(
                ID INTEGER,
                Product_name TEXT,
                Product_Price REAL
               )
            """)



cursor.executemany(
    "INSERT INTO filtered_data (id, product_name, product_price) VALUES (?, ?, ?)",
    all_rows
)

# 3. Save permanently and close the vault
connection.commit()
connection.close()

