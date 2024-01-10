import pandas as pd
from sklearn.preprocessing import LabelEncoder


def encode_and_save_mapping(df, column_name, mapping_file_path):
    encoder = LabelEncoder()
    df[column_name] = encoder.fit_transform(df[column_name])
    mapping = {index: label for index, label in enumerate(encoder.classes_)}
    with open(mapping_file_path, 'w') as file:
        for index, label in mapping.items():
            file.write(f"{index}: {label}\n")


# Load data from the CSV file
df = pd.read_csv('csv/cars.csv')

# Define the columns to be encoded
columns_to_encode = ['brand', 'model', 'transmission', 'fuelType']

# Encode and save mappings for each column
for column in columns_to_encode:
    encode_and_save_mapping(df, column, f'mapping/{column}_mapping.txt')

# Save the DataFrame with label-encoded columns to a new CSV file
df.to_csv('csv/cars_label_encode.csv', index=False)
