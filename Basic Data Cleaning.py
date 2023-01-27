import pandas as pd
import numpy as np

# Read the Excel file into a DataFrame
df = pd.read_excel('data.xlsx')

# Check for missing data
print(df.isna().sum())

# Drop any rows with missing data
df.dropna(inplace=True)

# Check for duplicate rows
print(df.duplicated().sum())

# Remove any duplicate rows
df.drop_duplicates(inplace=True)

# Check for invalid data types
print(df.dtypes)

# Convert columns to appropriate data types
df['column_name'] = pd.to_numeric(df['column_name'], errors='coerce')
df['column_name'] = pd.to_datetime(df['column_name'], errors='coerce')

# Strip leading and trailing whitespace from string columns
for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].str.strip()

# Check for outliers
df.describe()

# Remove outliers using the Interquartile range method
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
df = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]

# Check for any remaining missing data
print(df.isna().sum())

# Fill missing data with mean value
df.fillna(df.mean(), inplace=True)

# Check for duplicate rows after cleaning
print(df.duplicated().sum())

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Standardize data
df = (df - df.mean()) / df.std()

# Save the cleaned data to a new Excel file
df.to_excel('cleaned_data.xlsx', index=False)
