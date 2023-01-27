# Load the packages
library(readxl)
library(tidyverse)

# Read the Excel file into a dataframe
df <- read_excel("data.xlsx")

# Check for missing data
print(sum(is.na(df)))

# Remove missing data
df <- df %>% drop_na()

# Check for duplicate rows
print(sum(duplicated(df)))

# Remove duplicate rows
df <- df %>% distinct()

# Check for invalid data types
print(str(df))

# Convert columns to appropriate data types
df$column_name <- as.numeric(as.character(df$column_name))
df$column_name <- as.Date(df$column_name)

# Strip leading and trailing whitespace from string columns
df$column_name <- trimws(df$column_name, which = c("both"))

# Check for outliers
summary(df)

#Remove Outliers
df <- df %>% filter(column_name < upper_bound)

# Standardize data
df$column_name <- scale(df$column_name)

# Save the cleaned data to a new excel file
write_excel_csv(df, "cleaned_data.csv")
