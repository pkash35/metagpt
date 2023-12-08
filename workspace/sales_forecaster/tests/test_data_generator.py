## test_data_generator.py

import unittest
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Import the class to be tested
from sales_forecaster.data_generator import DataGenerator

class TestDataGenerator(unittest.TestCase):
    
    ## Test the initialization of the DataGenerator class
    def test_initialization(self):
        dg = DataGenerator()
        self.assertEqual(dg.years, 1, "Incorrect default years")
        
        dg = DataGenerator(2)
        self.assertEqual(dg.years, 2, "Incorrect initialization of years")
        
    ## Test the generate function
    def test_generate(self):
        dg = DataGenerator()
        df = dg.generate()
        
        # Check the dataframe is not empty
        self.assertTrue(len(df) > 0, "Dataframe is empty")
        
        # Check the dataframe has the correct columns
        self.assertEqual(list(df.columns), ['date', 'sales'], "Incorrect dataframe columns")
        
        # Check the dataframe has the correct number of rows
        self.assertEqual(len(df), 365, "Incorrect number of rows in dataframe")
        
        # Check the dataframe's date range
        self.assertEqual(df['date'].min(), datetime.now() - timedelta(days=365), "Incorrect start date in dataframe")
        self.assertEqual(df['date'].max(), datetime.now(), "Incorrect end date in dataframe")
        
        # Check the sales data is within the correct range
        self.assertTrue(df['sales'].min() >= 1, "Sales data contains values less than 1")
        self.assertTrue(df['sales'].max() <= 100, "Sales data contains values greater than 100")
        
        # Check the sales data is integer
        self.assertTrue(np.issubdtype(df['sales'].dtype, np.integer), "Sales data is not integer")

if __name__ == '__main__':
    unittest.main()
