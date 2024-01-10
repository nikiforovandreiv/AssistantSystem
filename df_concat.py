import pandas as pd

# Load data from each CSV file
audi_df = pd.read_csv('csv/audi.csv')
bmw_df = pd.read_csv('csv/bmw.csv')
ford_df = pd.read_csv('csv/ford.csv')
toyota_df = pd.read_csv('csv/toyota.csv')

# Add a new column 'Brand' to each DataFrame
audi_df['brand'] = 'Audi'
bmw_df['brand'] = 'BMW'
ford_df['brand'] = 'Ford'
toyota_df['brand'] = 'Toyota'

# Rearrange columns to have 'Brand' as the first column
column_order = ['brand'] + [col for col in audi_df.columns if col != 'brand']
audi_df = audi_df[column_order]
bmw_df = bmw_df[column_order]
ford_df = ford_df[column_order]
toyota_df = toyota_df[column_order]

# Concatenate all DataFrames into one
combined_df = pd.concat([audi_df, bmw_df, ford_df, toyota_df], ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_df.to_csv('csv/cars.csv', index=False)
