import unittest
import pandas as pd
from pandas._testing import assert_frame_equal
from sales_forecaster.forecaster import Forecaster

class TestForecaster(unittest.TestCase):
    def setUp(self):
        self.forecaster = Forecaster()
        self.data = pd.DataFrame({
            'date': pd.date_range(start='1/1/2020', end='1/31/2020'),
            'sales': range(1, 32)
        })

    ## Test if the Forecaster object is correctly initialized
    def test_init(self):
        self.assertIsInstance(self.forecaster, Forecaster)
        self.assertIsInstance(self.forecaster.model, Prophet)

    ## Test if the forecast method raises ValueError for empty dataframe
    def test_forecast_empty_dataframe(self):
        empty_df = pd.DataFrame()
        with self.assertRaises(ValueError) as context:
            self.forecaster.forecast(empty_df)
        self.assertEqual(str(context.exception), "Input data is empty")

    ## Test if the forecast method raises ValueError for dataframe without required columns
    def test_forecast_no_required_columns(self):
        df_no_columns = pd.DataFrame({'date': pd.date_range(start='1/1/2020', end='1/31/2020')})
        with self.assertRaises(ValueError) as context:
            self.forecaster.forecast(df_no_columns)
        self.assertEqual(str(context.exception), "Input data should have 'date' and 'sales' columns")

    ## Test if the forecast method correctly fits the model and returns a forecast
    def test_forecast(self):
        forecast = self.forecaster.forecast(self.data)
        self.assertIsInstance(forecast, pd.DataFrame)
        self.assertTrue('ds' in forecast.columns)
        self.assertTrue('yhat' in forecast.columns)

    ## Test if the forecast method correctly handles a dataframe with additional columns
    def test_forecast_additional_columns(self):
        data_additional_columns = self.data.copy()
        data_additional_columns['extra'] = range(1, 32)
        forecast = self.forecaster.forecast(data_additional_columns)
        self.assertIsInstance(forecast, pd.DataFrame)
        self.assertTrue('ds' in forecast.columns)
        self.assertTrue('yhat' in forecast.columns)

if __name__ == '__main__':
    unittest.main()
