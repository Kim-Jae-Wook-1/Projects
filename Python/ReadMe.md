# Happiness Factors Analysis with Python

## Overview
This project explores the question:

**What factors are associated with happiness in life?**

Using the Young People Survey (YPS) dataset, I analyzed how lifestyle, health, and social variables relate to self-reported happiness.

## Dataset
- Dataset: Young People Survey (YPS)
- Format: CSV
- Observations: 1010 rows
- Variables: 150 columns

For this project, I selected:
- Target variable: `Happiness in life`
- Core features: `Health`, `Energy levels`, `Active sport`, `Healthy eating`, `Number of friends`, `Socializing`, `Loneliness`, `Mood swings`
- Control variables: `Age`, `Gender`

## Tools and Libraries
- Python
- pandas
- numpy
- matplotlib
- scipy
- seaborn
- scikit-learn

## Project Workflow
1. Loaded and inspected the YPS dataset
2. Selected target, predictors, and control variables
3. Handled missing values for numeric and categorical variables
4. Performed exploratory data analysis (EDA)
5. Visualized distributions and correlations
6. Compared multiple regression models:
   - Linear Regression
   - Huber Regression
   - Random Forest Regression
7. Interpreted model outputs and discussed limitations

## Key Analysis Tasks
- Data preprocessing and missing value handling
- Descriptive statistics for numeric and categorical variables
- Distribution plots for target and main features
- Spearman correlation analysis
- Gender-based comparison using Mann–Whitney U test
- Regression model comparison and best model selection

## Main Result
The project examined which personal and social factors are most strongly associated with happiness in life and compared several regression approaches to identify the most suitable predictive model.

## Repository Structure
- `project_code.py` or notebook: main analysis code
- `YPS.csv`: dataset file
- `Project.pdf`: full report
- `README.md`: project summary

## Notes
This project was created as an academic Python data analysis project and focuses on structured data preprocessing, visualization, statistical analysis, and regression modeling.
