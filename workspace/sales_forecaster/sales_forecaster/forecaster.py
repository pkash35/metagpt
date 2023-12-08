from prophet import Prophet
import pandas as pd

class Forecaster:
    def __init__(self):
        self.model = Prophet()

    def forecast(self, data: pd.DataFrame) -> pd.DataFrame:
        # Check if the dataframe is empty
        if data.empty:
            raise ValueError("Input data is empty")

        # Check if the required columns are present in the dataframe
        if not {'date', 'sales'}.issubset(data.columns):
            raise ValueError("Input data should have 'date' and 'sales' columns")

        # Prophet requires columns ds (Date) and y (value)
        data = data.rename(columns={'date': 'ds', 'sales': 'y'})

        # Fit the model with the data
        self.model.fit(data)

        # Make a future dataframe for prediction
        future = self.model.make_future_dataframe(periods=365)

        # Predict the future
        forecast = self.model.predict(future)

        return forecast
