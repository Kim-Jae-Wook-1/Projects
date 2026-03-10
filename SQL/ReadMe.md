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
The project includes SQL queries for:
- first 5 rows of the dataset
- transaction count by country
- total sales by country
- top products by quantity sold
- top products by total revenue

## Outcome
This project helped build a basic end-to-end workflow using Python and SQL for structured retail data.

