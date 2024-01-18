import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler


class DFPreprocess:
    def __init__(self, df):
        self.df = df.copy()

    def remove_outliers_in_column(self, column):
        q1 = self.df[column].quantile(0.25)
        q3 = self.df[column].quantile(0.75)
        iqr = q3 - q1
        self.df = self.df[(self.df[column] > q1 - 1.5 * iqr) & (self.df[column] < q3 + 1.5 * iqr)]

    def remove_outliers(self):
        # Remove outliers from numerical columns
        numerical_columns = [
            'year',
            'mileage',
            'tax',
            'mpg',
            'engineSize',
            'price'
        ]
        for column in numerical_columns:
            if column in self.df.columns:
                self.remove_outliers_in_column(column)

        return self.df

    def encode_categorical_columns(self, columns):
        encoder = LabelEncoder()
        for column in columns:
            self.df[column] = encoder.fit_transform(self.df[column])

            # Save the LabelEncoder to a file
            label_encoder_filename = f'{column}_label_encoder_model.joblib'
            joblib.dump(encoder, f'saved_model/label_encoder/{label_encoder_filename}')
            print(f'Label encoder model for {column} saved as saved_model/label_encoder/{label_encoder_filename}')

    def scale_numeric_columns(self, columns):
        scalers = {}
        scaled_data = {}

        for column in columns:
            scaler = MinMaxScaler(copy=True, feature_range=(0, 1))
            scaled_data[column] = scaler.fit_transform(self.df[[column]])
            scalers[column] = scaler

            # Save the trained scaler
            scaler_filename = f'{column}_scaler_model.joblib'
            joblib.dump(scaler, f'saved_model/scaler/{scaler_filename}')
            print(f'Scaler model for {column} saved as saved_model/scaler/{scaler_filename}')

        scaled_numeric_df = pd.concat([pd.DataFrame(scaled_data[column], columns=[column]) for column in columns], axis=1)

        # Add the 'price' column back to the DataFrame without scaling it
        scaled_numeric_df['price'] = self.df['price']

        self.df = scaled_numeric_df

    def preprocess(self):
        # Remove outliers
        self.remove_outliers()

        # Encode categorical columns
        categorical_columns = [
            'brand',
            'model',
            'transmission',
            'fuelType'
        ]
        self.encode_categorical_columns(categorical_columns)

        # Scale numeric columns
        numeric_columns_to_scale = [
            'brand',
            'model',
            'year',
            'transmission',
            'mileage',
            'fuelType',
            'tax',
            'mpg',
            'engineSize'
        ]
        self.scale_numeric_columns(numeric_columns_to_scale)

        return self.df
