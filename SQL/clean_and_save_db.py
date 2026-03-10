import pandas as pd
import sqlite3

# Set input and output file names
file_path = "Online Retail.xlsx"
db_path = "retail.db"

# Load Excel file
df = pd.read_excel(file_path)

# Show original data size
print("Original shape:", df.shape)

# Remove rows with missing description
df = df.dropna(subset=["Description"])

# Remove rows with missing customer ID
df = df.dropna(subset=["CustomerID"])

# Keep rows with positive quantity only
df = df[df["Quantity"] > 0]

# Keep rows with positive unit price only
df = df[df["UnitPrice"] > 0]

# Create total price column
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# Show cleaned data size
print("Cleaned shape:", df.shape)

# Connect to SQLite database
conn = sqlite3.connect(db_path)

# Save DataFrame as SQL table
df.to_sql("retail", conn, if_exists="replace", index=False)

# Print save message
print("Saved table 'retail' into retail.db")

# Close database connection
conn.close()