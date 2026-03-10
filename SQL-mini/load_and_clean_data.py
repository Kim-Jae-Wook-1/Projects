import pandas as pd

file_path = "Online Retail.xlsx"

df = pd.read_excel(file_path)

print("Rows, Columns:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nFirst 10 rows:")
print(df.head(10))