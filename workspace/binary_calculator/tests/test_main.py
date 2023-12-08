import unittest
import tkinter as tk
from unittest.mock import MagicMock
from binary_calculator.main import Application

class TestApplication(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = Application(master=self.root)

    def tearDown(self):
        self.root.destroy()

    ## Test initialization
    def test_init(self):
        self.assertIsInstance(self.app, Application)
        self.assertEqual(self.app.master, self.root)

    ## Test widget creation
    def test_create_widgets(self):
        self.assertIsNotNone(self.app.binary1_entry)
        self.assertIsNotNone(self.app.binary2_entry)
        self.assertIsNotNone(self.app.add_button)
        self.assertIsNotNone(self.app.subtract_button)
        self.assertIsNotNone(self.app.multiply_button)
        self.assertIsNotNone(self.app.divide_button)
        self.assertIsNotNone(self.app.result_label)
        self.assertIsNotNone(self.app.clear_button)

    ## Test calculate method
    def test_calculate(self):
        self.app.binary1_entry.insert(0, '10')
        self.app.binary2_entry.insert(0, '01')
        self.app.calculate('add')
        self.assertEqual(self.app.result_label["text"], '11')

    ## Test add method
    def test_add(self):
        self.app.binary1_entry.insert(0, '10')
        self.app.binary2_entry.insert(0, '01')
        self.app.add()
        self.assertEqual(self.app.result_label["text"], '11')

    ## Test subtract method
    def test_subtract(self):
        self.app.binary1_entry.insert(0, '10')
        self.app.binary2_entry.insert(0, '01')
        self.app.subtract()
        self.assertEqual(self.app.result_label["text"], '1')

    ## Test multiply method
    def test_multiply(self):
        self.app.binary1_entry.insert(0, '10')
        self.app.binary2_entry.insert(0, '01')
        self.app.multiply()
        self.assertEqual(self.app.result_label["text"], '0')

    ## Test divide method
    def test_divide(self):
        self.app.binary1_entry.insert(0, '10')
        self.app.binary2_entry.insert(0, '01')
        self.app.divide()
        self.assertEqual(self.app.result_label["text"], '2')

    ## Test clear method
    def test_clear(self):
        self.app.binary1_entry.insert(0, '10')
        self.app.binary2_entry.insert(0, '01')
        self.app.clear()
        self.assertEqual(self.app.binary1_entry.get(), '')
        self.assertEqual(self.app.binary2_entry.get(), '')
        self.assertEqual(self.app.result_label["text"], '')

if __name__ == '__main__':
    unittest.main()
