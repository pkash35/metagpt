## test_app.py

import unittest
from unittest.mock import patch, Mock
from flask import Flask
from sales_forecaster.app import App

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = App()
        self.client = self.app.app.test_client()

    ## Test the '/forecast' endpoint
    @patch('sales_forecaster.app.DataGenerator')
    @patch('sales_forecaster.app.Forecaster')
    def test_forecast(self, mock_forecaster, mock_data_generator):
        ## Mock the DataGenerator and Forecaster classes
        mock_data_generator.return_value.generate.return_value = {'yhat': [100, 200, 300]}
        mock_forecaster.return_value.forecast.return_value = {'yhat': [100, 200, 300]}

        ## Send a POST request to the '/forecast' endpoint
        response = self.client.post('/forecast', json={'years': 3})

        ## Check if the status code is 200
        self.assertEqual(response.status_code, 200)

        ## Check if the response is correct
        self.assertEqual(response.get_json(), {'forecast': [100, 200, 300]})

    ## Test the '/forecast' endpoint with invalid 'years' parameter
    def test_forecast_invalid_years(self):
        ## Send a POST request to the '/forecast' endpoint with invalid 'years' parameter
        response = self.client.post('/forecast', json={'years': 'invalid'})

        ## Check if the status code is 400
        self.assertEqual(response.status_code, 400)

        ## Check if the error message is correct
        self.assertEqual(response.get_json(), {'error': "Invalid 'years' parameter"})

    ## Test the '/forecast' endpoint without 'years' parameter
    @patch('sales_forecaster.app.DataGenerator')
    @patch('sales_forecaster.app.Forecaster')
    def test_forecast_without_years(self, mock_forecaster, mock_data_generator):
        ## Mock the DataGenerator and Forecaster classes
        mock_data_generator.return_value.generate.return_value = {'yhat': [100, 200, 300]}
        mock_forecaster.return_value.forecast.return_value = {'yhat': [100, 200, 300]}

        ## Send a POST request to the '/forecast' endpoint without 'years' parameter
        response = self.client.post('/forecast')

        ## Check if the status code is 200
        self.assertEqual(response.status_code, 200)

        ## Check if the response is correct
        self.assertEqual(response.get_json(), {'forecast': [100, 200, 300]})

if __name__ == '__main__':
    unittest.main()
