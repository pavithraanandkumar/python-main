import pandas as pd

# Responsibility 1: Read CSV file and manipulate data frame
df = pd.read_csv('data.csv')

# Print the first few rows of the data frame
print(df.head())

# Select specific columns
columns_of_interest = ['column1', 'column2', 'column3']
df_selected = df[columns_of_interest]

# Print the selected columns
print(df_selected.head())

# Responsibility 2: Simple data cleaning tasks
# Handle missing values
df_filled = df.fillna('')  # Replace missing values with empty strings
df_dropped = df.dropna()  # Remove rows with missing values

# Remove duplicates
df_no_duplicates = df.drop_duplicates()

# Responsibility 3: Basic data manipulation operations
# Filtering
filtered_df = df[df['column1'] > 0.5]  # Filter rows where column1 > 0.5

# Sorting
sorted_df = df.sort_values(by='column2')  # Sort by column2 in ascending order

# Grouping
grouped_df = df.groupby('column3')  # Group by column3

# Calculate mean only for numeric columns
numeric_columns = df.select_dtypes(include='number').columns
grouped_df_mean = grouped_df[numeric_columns].mean()  # Calculate mean of numeric columns

# Print the results
print(filtered_df.head())
print(sorted_df.head())
print(grouped_df_mean.head())

# Save the manipulated data to a new CSV file
df_selected.to_csv('manipulated_data.csv', index=False)
