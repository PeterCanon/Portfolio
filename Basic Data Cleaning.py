import pandas as pd

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

# Remove outliers
df = df[df['column_name'] < upper_bound]

# Standardize data
df['column_name'] = (df['column_name'] - df['column_name'].mean()) / df['column_name'].std()

# Save the cleaned data to a new Excel file
df.to_excel('cleaned_data.xlsx', index=False)
