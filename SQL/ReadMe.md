# Online Retail Data Processing with Python and SQL

## Overview
This project is an initiave data processing and SQL analysis project based on the Online Retail dataset.

The goal of this project was to practice a simple data workflow:
- loading Excel data with Python
- cleaning raw transaction records
- storing processed data in SQLite
- running SQL queries for sales analysis

## Tools
- Python
- pandas
- SQLite
- SQL

## Files
- `clean_and_save_db.py`: loads the Excel file, cleans the data, and saves it into SQLite DB
- `run_sql_analysis.py`: runs SQL queries on the SQLite database
- `country_sales_summary.csv`: country-level sales summary

## Data Cleaning
The following preprocessing steps were applied:
- removed rows with missing `Description`
- removed rows with missing `CustomerID`
- kept only rows with positive `Quantity`
- kept only rows with positive `UnitPrice`
- created a new column `TotalPrice = Quantity * UnitPrice`

## Example SQL Analysis
The project includes SQLite-based SQL queries using the following clauses and functions:
- `SELECT`, `FROM`, `LIMIT` for viewing the first rows of the dataset
- `SELECT`, `FROM`, `GROUP BY`, `COUNT(*)`, `ORDER BY`, and `DESC` for transaction count by country
- `SELECT`, `FROM`, `GROUP BY`, `SUM(TotalPrice)`, `ORDER BY`, and `DESC` for total sales by country
- `SELECT`, `FROM`, `GROUP BY`, `SUM(Quantity)`, `ORDER BY`, `DESC`, and `LIMIT` for top products by quantity sold
- `SELECT`, `FROM`, `GROUP BY`, `SUM(TotalPrice)`, `ORDER BY`, `DESC`, and `LIMIT` for top products by total revenue
  
## Outcome
This project helped build a basic end-to-end workflow using Python and SQL for structured retail data.

