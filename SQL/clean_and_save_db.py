import pandas as pd
import sqlite3

# Set input and output file names (입력 엑셀 파일 이름과 출력 데이터베이스 파일 이름 설정)
file_path = "Online Retail.xlsx"
db_path = "retail.db"

# Load Excel file
df = pd.read_excel(file_path)

# Show original data size
# print(f"Original shape : {df.shape}")

print("(Rows, Columns) : ", df.shape)

# Result : (Rows, Columns) :  (541909, 8)

print(f"Column names : {df.columns.tolist()}")

# Result 
# Column names : 
# ['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country']

# Print data type of each column
print(f"Data types : {df.dtypes}")

# Results ↓
# Data types : InvoiceNo              object
# StockCode              object
# Description            object
# Quantity                int64
# InvoiceDate    datetime64[ns]
# UnitPrice             float64
# CustomerID            float64
# Country                object
# dtype: object



# Print number of missing
print(f"Missing values : {df.isnull().sum()}")

# Results ↓
# Missing values : InvoiceNo           0
# StockCode           0
# Description      1454
# Quantity            0
# InvoiceDate         0
# UnitPrice           0
# CustomerID     135080
# Country             0
# dtype: int64


# Print fisrt 10 rows of dataset
print(f"First 10 rows : {df.head(10)}")


# Results ↓
# First 10 rows :   
#    InvoiceNo StockCode                         Description  Quantity         InvoiceDate  UnitPrice   CustomerID        Country
# 0    536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6 2010-12-01 08:26:00       2.55     17850.0  United Kingdom
# 1    536365     71053                  WHITE METAL LANTERN         6 2010-12-01 08:26:00       3.39     17850.0  United Kingdom
# 2    536365    84406B       CREAM CUPID HEARTS COAT HANGER         8 2010-12-01 08:26:00       2.75     17850.0  United Kingdom
# 3    536365    84029G  KNITTED UNION FLAG HOT WATER BOTTLE         6 2010-12-01 08:26:00       3.39     17850.0  United Kingdom
# 4    536365    84029E       RED WOOLLY HOTTIE WHITE HEART.         6 2010-12-01 08:26:00       3.39     17850.0  United Kingdom
# 5    536365     22752         SET 7 BABUSHKA NESTING BOXES         2 2010-12-01 08:26:00       7.65     17850.0  United Kingdom
# 6    536365     21730    GLASS STAR FROSTED T-LIGHT HOLDER         6 2010-12-01 08:26:00       4.25     17850.0  United Kingdom
# 7    536366     22633               HAND WARMER UNION JACK         6 2010-12-01 08:28:00       1.85     17850.0  United Kingdom
# 8    536366     22632            HAND WARMER RED POLKA DOT         6 2010-12-01 08:28:00       1.85     17850.0  United Kingdom
# 9    536367     84879        ASSORTED COLOUR BIRD ORNAMENT        32 2010-12-01 08:34:00       1.69     13047.0  United Kingdom


# ------------------------ Let's preprocessing Data !!! ------------------------

# Remove rows with missing description
df = df.dropna(subset=["Description"])   # This will remove 1,454 rows with missing Description

# Remove rows with missing customer ID
df = df.dropna(subset=["CustomerID"])    # This will remove 135,080 rows with missing CustomerID

# Keep rows with positive quantity only
df = df[df["Quantity"] > 0]   # This will remove rows where Quantity is 0 or negarive

# Keep rows with positive unit price only
df = df[df["UnitPrice"] > 0]   # This will remove rows where UnitPrice is 0 or negative

# Create total price column
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]   # This will create one new column, TotalPrice = Quantity X UnitPrice

# Show Pre-processed data size 
print(f"Pre-processed data size : {df.shape}")   # Result → Pre-processed data size : (397884, 9)


# ----------------- SQLite Start ! -----------------


# Connect to SQLite database
conn = sqlite3.connect(db_path)

# db_path = "retail.db" 이었으므로, retail.db 파일을 열거나 없으면 새로 만든다 + retail.db 라는 데이터베이스 파일에 연결한다.


# !!! Save DataFrame as SQL table named 'retail' : 이게 가장 중요함
df.to_sql("retail", conn, if_exists="replace", index=False)

# Python 데이터프레임 df 를 retail 이라는 이름의 SQL 테이블로 저장한다. 해당 파일이 있으면 덮어쓰기 (replace) + pandas 맨 왼쪽 번호 index 는 저장하지 않는다 !

# Print save message
print("Saved table 'retail' into retail.db")

# Close database connection
conn.close()