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


# Save results as CSV file
result_3.to_csv("country_sales_summary.csv", index=False)
print("\nSaved Query 3 result to country_sales_summary.csv !!!")


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



# query_n : 파이썬 문자열. 안에 들어 있는 것은 SQL 문장이다.

# Query 6 : Search text with LIKE
# retail 테이블에서 Description 안에 LIKE 라는 글자가 포함된 행만 찾아서 앞 13 행을 보여줘 !
query_6 = """
SELECT Description, Quantity, UnitPrice, TotalPrice
FROM retail
WHERE Description LIKE '%LIKE%'
LIMIT 13
"""

# % 아무 문자든 0개 이상 올 수 있음 하지만, 중간에 HEART 가 반드시 포함되어야 한다는 의미이다.
# 어차피 Description 에서 LIKE 포함 여부만 검사했는데, 왜 굳이 Quantity, UnitPrice, TotalPrice 까지 같이 가져오지?
# => WHERE 에서 Description 을 조건에 썼더라도, 그렇게 걸러진 행들에 대해 Quantity, UnitPrice, TotalPrice 도 함께 볼 수 있다 !

result_6 = pd.read_sql_query(query_6,conn)       # query_n 안에 있는 SQL 문장을 conn 으로 연결된 데이터베이스에 실행하고, 그 결과를 pandas DataFrame 으로 읽어오기 !
print(f"Query 6 : Description contains LIKE \n{result_6}")

# Query 6 : Description contains LIKE 
#                     Description  Quantity  UnitPrice  TotalPrice
# 0     ALARM CLOCK BAKELIKE PINK        24       3.75       90.00
# 1     ALARM CLOCK BAKELIKE RED         24       3.75       90.00
# 2    ALARM CLOCK BAKELIKE GREEN        12       3.75       45.00
# 3    ALARM CLOCK BAKELIKE GREEN         4       3.75       15.00
# 4    ALARM CLOCK BAKELIKE GREEN         4       3.75       15.00
# 5     ALARM CLOCK BAKELIKE RED          4       3.75       15.00
# 6    ALARM CLOCK BAKELIKE IVORY         4       3.75       15.00
# 7     ALARM CLOCK BAKELIKE RED          8       3.75       30.00
# 8   ALARM CLOCK BAKELIKE ORANGE         8       3.75       30.00
# 9    ALARM CLOCK BAKELIKE GREEN         8       3.75       30.00
# 10    ALARM CLOCK BAKELIKE RED          9       3.75       33.75
# 11   ALARM CLOCK BAKELIKE GREEN         9       3.75       33.75
# 12   ALARM CLOCK BAKELIKE IVORY         9       3.75       33.75


# Query 7 : Average sales by country

# retail 테이블에서 거래들을 Country 별로 그룹화한 뒤,
# 각 국가 그룹의 TotalPrice 평균을 SQL 집계 함수 AVG(TotalPrice)로 계산하고,
# 계산된 평균값을 avg_sales라는 별칭으로 표시하여,
# avg_sales 기준 내림차순으로 정렬한 뒤 상위 11개 국가를 보여줘 !

# retail 테이블의 거래들을 Country 별로 묶고 각 국가의 평균 TotalPrice 를 계산해서 평균값이 큰 순서대로 상위 11 개 국가를 보여줘 ! 
query_7 = """
SELECT Country, AVG(TotalPrice) AS avg_sales
FROM retail
GROUP BY Country
ORDER BY avg_sales DESC
LIMIT 11
"""

result_7 = pd.read_sql_query(query_7, conn)
print(f"Query 7 : Top 10 countries by average sales \n{result_7}")

# Query 7 : Top 10 countries by average sales 
#         Country   avg_sales
# 0   Netherlands  121.003111
# 1     Australia  117.192310
# 2         Japan  116.561900
# 3     Singapore   95.852658
# 4        Sweden   85.096075
# 5       Denmark   49.882474
# 6     Lithuania   47.458857
# 7       Lebanon   37.641778
# 8          EIRE   36.697886
# 9        Brazil   35.737500
# 10       Norway   33.767918


# Query 8 : Minimum and Maximum sales by country
# retail 테이블들의 거래들을 Country 별로 묶고,
# 각 국가의 TotalPrice 중 최소값 (min_sales) 과 최대값 (max_sales) 을 계산해서,
# Country, min_sales, max_sales 칼럼으로 결과를 반환하고,
# max_sales 기준 내림차순으로 상위 11개 국가를 보여줘 !

query_8 = """
SELECT Country,
        MIN(TotalPrice) AS min_sales,
        MAX(TotalPrice) AS max_sales
FROM retail
GROUP BY Country
ORDER BY max_sales DESC
LIMIT 11
"""

result_8 = pd.read_sql_query(query_8, conn)
print(f"Query 8 : Min / Max sales by country \n{result_8}")


# Query 8 : Min / Max sales by country 
#            Country  min_sales  max_sales
# 0   United Kingdom      0.001  168469.60
# 1      Netherlands      0.390    4992.00
# 2           France      0.290    4161.06
# 3        Singapore      2.340    3949.32
# 4            Japan      0.290    3794.40
# 5             EIRE      1.250    2365.20
# 6        Australia      0.420    1718.40
# 7            Spain      0.210    1350.00
# 8         Portugal      0.290    1241.98
# 9           Sweden      5.040    1188.00
# 10         Germany      0.390     876.00










# Close database connection
conn.close()