import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("retail.db")

# Query 1: Show first 5 rows
# 원본 retail 테이블에서 Country 가 France 인 행만 남기고, 그 행들의 앞 5행만 보여줘 !
query_1 = """
SELECT *
FROM retail
WHERE Country = 'France'
LIMIT 7
"""

result_1 = pd.read_sql_query(query_1, conn)
print(f"Query 1 & First 5 rows : \n{result_1}")

# Query 1 & First 5 rows : 
#    InvoiceNo StockCode                         Description  Quantity          InvoiceDate  UnitPrice  CustomerID Country  TotalPrice
# 0     536370     22728           ALARM CLOCK BAKELIKE PINK        24  2010-12-01 08:45:00       3.75     12583.0  France        90.0
# 1     536370     22727           ALARM CLOCK BAKELIKE RED         24  2010-12-01 08:45:00       3.75     12583.0  France        90.0
# 2     536370     22726          ALARM CLOCK BAKELIKE GREEN        12  2010-12-01 08:45:00       3.75     12583.0  France        45.0
# 3     536370     21724     PANDA AND BUNNIES STICKER SHEET        12  2010-12-01 08:45:00       0.85     12583.0  France        10.2
# 4     536370     21883                    STARS GIFT TAPE         24  2010-12-01 08:45:00       0.65     12583.0  France        15.6
# 5     536370     10002         INFLATABLE POLITICAL GLOBE         48  2010-12-01 08:45:00       0.85     12583.0  France        40.8
# 6     536370     21791  VINTAGE HEADS AND TAILS CARD GAME         24  2010-12-01 08:45:00       1.25     12583.0  France        30.0




# Query 2: Count transactions by country
# retail 테이블의 거래들을 국가 (Country) 별로 묶고 각 국가의 거래 수를 세고 거래 수가 많은 순서대로 상위 8개 국가를 보여줘 !
query_2 = """
SELECT Country, COUNT(*) AS transaction_count
FROM retail
GROUP BY Country
ORDER BY transaction_count DESC
LIMIT 10
"""

result_2 = pd.read_sql_query(query_2, conn)
print(f"Query 2 (Top 10 countries by transaction count) : \n{result_2}")


# Query 2 (Top 10 countries by transaction count) : 
#           Country  transaction_count
# 0  United Kingdom             354321
# 1         Germany               9040
# 2          France               8341
# 3            EIRE               7236
# 4           Spain               2484
# 5     Netherlands               2359
# 6         Belgium               2031
# 7     Switzerland               1841
# 8        Portugal               1462
# 9       Australia               1182


# Query 3: Sum total sales by country
# retail 테이블의 거래들을 국가 (Country) 별로 묶고 각 국가의 TotalPrice 를 모두 더해서 총매출이 큰 순서대로 상위 8개 국가를 보여줘 !
query_3 = """
SELECT Country, SUM(TotalPrice) AS total_sales
FROM retail
GROUP BY Country
ORDER BY total_sales DESC
LIMIT 8
"""

result_3 = pd.read_sql_query(query_3, conn)
print(f"Query 3 (Top 10 countries by total sales) \n{result_3}")


# Query 3 (Top 10 countries by total sales) 
#           Country   total_sales
# 0  United Kingdom  7.308392e+06
# 1     Netherlands  2.854463e+05
# 2            EIRE  2.655459e+05
# 3         Germany  2.288671e+05
# 4          France  2.090240e+05
# 5       Australia  1.385213e+05
# 6           Spain  6.157711e+04
# 7     Switzerland  5.644395e+04



# Query 4: Sum quantity by product
# retail 테이블의 거래들을 상품명 (Description) 기준으로 묶고 각 상품의 판매수량 합계를 계산해서 가장 많이 팔린 상품 11개를 보여줘 !
query_4 = """
SELECT Description, SUM(Quantity) AS total_quantity
FROM retail
GROUP BY Description
ORDER BY total_quantity DESC
LIMIT 11
"""

result_4 = pd.read_sql_query(query_4, conn)
print(f"Query 4: Top 10 products by quantity sold \n{result_4}")

# Query 4: Top 10 products by quantity sold 
#                            Description  total_quantity
# 0          PAPER CRAFT , LITTLE BIRDIE           80995
# 1       MEDIUM CERAMIC TOP STORAGE JAR           77916
# 2    WORLD WAR 2 GLIDERS ASSTD DESIGNS           54415
# 3              JUMBO BAG RED RETROSPOT           46181
# 4   WHITE HANGING HEART T-LIGHT HOLDER           36725
# 5        ASSORTED COLOUR BIRD ORNAMENT           35362
# 6      PACK OF 72 RETROSPOT CAKE CASES           33693
# 7                       POPCORN HOLDER           30931
# 8                   RABBIT NIGHT LIGHT           27202
# 9              MINI PAINT SET VINTAGE            26076
# 10          PACK OF 12 LONDON TISSUES            25345


# Query 5: Sum revenue by product
# retail 테이블의 거래들을 상품명 (Description) 기준으로 묶고 각 상품의 총매출 합계를 계산해서 총매출이 큰 상품 13개를 보여줘 !
query_5 = """
SELECT Description, SUM(TotalPrice) AS total_revenue
FROM retail
GROUP BY Description
ORDER BY total_revenue DESC
LIMIT 13
"""

result_5 = pd.read_sql_query(query_5, conn)
print(f"Query 5: Top 10 products by total revenue \n{result_5}")

# Query 5: Top 10 products by total revenue 
#                            Description  total_revenue
# 0          PAPER CRAFT , LITTLE BIRDIE      168469.60
# 1             REGENCY CAKESTAND 3 TIER      142592.95
# 2   WHITE HANGING HEART T-LIGHT HOLDER      100448.15
# 3              JUMBO BAG RED RETROSPOT       85220.78
# 4       MEDIUM CERAMIC TOP STORAGE JAR       81416.73
# 5                              POSTAGE       77803.96
# 6                        PARTY BUNTING       68844.33
# 7        ASSORTED COLOUR BIRD ORNAMENT       56580.34
# 8                               Manual       53779.93
# 9                   RABBIT NIGHT LIGHT       51346.20
# 10                       CHILLI LIGHTS       46286.51
# 11     PAPER CHAIN KIT 50'S CHRISTMAS        42660.83
# 12      PICNIC BASKET WICKER 60 PIECES       39619.50


# Save results as CSV file
result_3.to_csv("country_sales_summary.csv", index=False)
print("\nSaved Query 3 result to country_sales_summary.csv !!!")

# Close database connection
conn.close()