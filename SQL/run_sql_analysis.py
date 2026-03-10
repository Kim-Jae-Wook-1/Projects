import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("retail.db")

# Query 1: Show first 5 rows

query_1 = """
SELECT *
FROM retail
LIMIT 5
"""

result_1 = pd.read_sql_query(query_1, conn)
print("\nQuery 1: First 5 rows")
print(result_1)


# Query 2: Count transactions by country

query_2 = """
SELECT Country, COUNT(*) AS transaction_count
FROM retail
GROUP BY Country
ORDER BY transaction_count DESC
LIMIT 10
"""

result_2 = pd.read_sql_query(query_2, conn)
print("\nQuery 2: Top 10 countries by transaction count")
print(result_2)


# Query 3: Sum total sales by country

query_3 = """
SELECT Country, SUM(TotalPrice) AS total_sales
FROM retail
GROUP BY Country
ORDER BY total_sales DESC
LIMIT 10
"""

result_3 = pd.read_sql_query(query_3, conn)
print("\nQuery 3: Top 10 countries by total sales")
print(result_3)

# -------------------------------
# Query 4: Sum quantity by product
# -------------------------------
query_4 = """
SELECT Description, SUM(Quantity) AS total_quantity
FROM retail
GROUP BY Description
ORDER BY total_quantity DESC
LIMIT 10
"""

result_4 = pd.read_sql_query(query_4, conn)
print("\nQuery 4: Top 10 products by quantity sold")
print(result_4)


# Query 5: Sum revenue by product

query_5 = """
SELECT Description, SUM(TotalPrice) AS total_revenue
FROM retail
GROUP BY Description
ORDER BY total_revenue DESC
LIMIT 10
"""

result_5 = pd.read_sql_query(query_5, conn)
print("\nQuery 5: Top 10 products by total revenue")
print(result_5)


# Optional: Save one result as CSV

result_3.to_csv("country_sales_summary.csv", index=False)
print("\nSaved Query 3 result to country_sales_summary.csv")

# Close database connection
conn.close()