import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


class DFTrain:
    MODEL_FILENAME = 'random_forest_regressor_model.joblib'

    def __init__(self, df):
        self.df = df.copy()
        self.rf_model = None

    def train_random_forest_regressor(self, test_size=0.2, random_state=42):
        x = self.df.drop('price', axis=1)
        y = self.df['price']

        # Split the data into training and testing sets
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state=random_state)

        # Train and evaluate Random Forest Regressor model
        self.rf_model = RandomForestRegressor()
        self.rf_model.fit(x_train, y_train)

        return self.rf_model

    def save_trained_model(self):
        if self.rf_model:
            joblib.dump(self.rf_model, 'saved_model/' + self.MODEL_FILENAME)
            print(f'Trained model saved as saved_model/{self.MODEL_FILENAME}')
        else:
            print('Error: Model not trained yet. Call train_random_forest_regressor first.')
