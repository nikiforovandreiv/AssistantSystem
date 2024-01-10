import pandas as pd

# Load data from each CSV file
df = pd.read_csv('csv/cars.csv')

# Rearrange columns to have 'price' as the last column
column_order = [col for col in df.columns if col != 'price'] + ['price']
df = df[column_order]

# Save the combined DataFrame to a new CSV file
df.to_csv('csv/cars.csv', index=False)
