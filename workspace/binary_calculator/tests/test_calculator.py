## test_calculator.py

import unittest
from binary_calculator.calculator import Calculator

class TestCalculator(unittest.TestCase):
    ## Test initialization of Calculator class
    def test_initialization(self):
        calculator = Calculator('1010', '1010')
        self.assertEqual(calculator.binary1, '1010')
        self.assertEqual(calculator.binary2, '1010')

    ## Test addition of two binary numbers
    def test_addition(self):
        calculator = Calculator('1010', '1010')
        self.assertEqual(calculator.add(), '10100')

    ## Test subtraction of two binary numbers
    def test_subtraction(self):
        calculator = Calculator('1010', '1010')
        self.assertEqual(calculator.subtract(), '0')

    ## Test multiplication of two binary numbers
    def test_multiplication(self):
        calculator = Calculator('1010', '1010')
        self.assertEqual(calculator.multiply(), '1100100')

    ## Test division of two binary numbers
    def test_division(self):
        calculator = Calculator('1010', '1010')
        self.assertEqual(calculator.divide(), '1')

    ## Test division by zero
    def test_division_by_zero(self):
        calculator = Calculator('1010', '0')
        self.assertEqual(calculator.divide(), 'Cannot divide by zero')

    ## Test invalid binary input
    def test_invalid_binary(self):
        with self.assertRaises(ValueError):
            calculator = Calculator('1020', '1010')

if __name__ == '__main__':
    unittest.main()
