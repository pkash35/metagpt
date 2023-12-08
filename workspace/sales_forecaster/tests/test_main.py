## test_main.py
import unittest
from unittest.mock import patch, Mock
import sys
import os

# Add the path of the main.py to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sales_forecaster import main  # Import the main module

class TestMain(unittest.TestCase):
    """
    Test case class for main.py
    """

    ## Test if the App class is instantiated
    @patch('sales_forecaster.main.App')
    def test_app_instantiation(self, MockApp):
        main.main()
        MockApp.assert_called_once()

    ## Test if the run method is called
    @patch('sales_forecaster.main.App')
    def test_app_run(self, MockApp):
        instance = MockApp.return_value
        main.main()
        instance.run.assert_called_once()

if __name__ == "__main__":
    unittest.main()
