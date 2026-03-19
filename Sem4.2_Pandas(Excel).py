import pandas as pd

# Read an Excel file
df = pd.read_excel('file.xlsx')

# Display first few rows
print(df.head())

# Display basic info
print(df.info())

# Display statistics
print(df.describe())

# Access a column
column_data = df['column_name']

# Filter data
value = 10  # Define the threshold value
filtered_df = df[df['column_name'] > value]

# Write to Excel
df.to_excel('output.xlsx', index=False)