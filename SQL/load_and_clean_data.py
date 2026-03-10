import pandas as pd


# Set path of Excel File
file_path = "Online Retail.xlsx"

# Read Excel file into pandas DataFrame
df = pd.read_excel(file_path)

# Print number of rows and columns
print("Rows, Columns:", df.shape)

# Result : Rows, Columns: (541909, 8)

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
# First 10 rows :   InvoiceNo StockCode                          Description  Quantity         InvoiceDate  UnitPrice  CustomerID         Country
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
