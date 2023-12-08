## test_main.py
import unittest
import tkinter as tk
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.append(os.path.abspath('sudoku_game'))
from main import main
from gui import GUI

class TestMain(unittest.TestCase):
    ## Test if main function is correctly initializing tkinter and GUI
    @patch('main.tk.Tk')
    @patch('main.GUI')
    def test_main(self, mock_GUI, mock_tk):
        mock_root = MagicMock()
        mock_gui = MagicMock()
        mock_tk.return_value = mock_root
        mock_GUI.return_value = mock_gui

        main()

        mock_tk.assert_called_once()
        mock_GUI.assert_called_once_with(mock_root)
        mock_gui.start_new_game.assert_called_once()
        mock_root.mainloop.assert_called_once()

    ## Test if main function is handling exceptions correctly
    @patch('main.tk.Tk')
    @patch('main.GUI')
    def test_main_exception_handling(self, mock_GUI, mock_tk):
        mock_root = MagicMock()
        mock_gui = MagicMock()
        mock_tk.return_value = mock_root
        mock_GUI.return_value = mock_gui
        mock_gui.start_new_game.side_effect = Exception("Test Exception")

        with self.assertRaises(Exception) as context:
            main()

        self.assertTrue('Test Exception' in str(context.exception))

if __name__ == "__main__":
    unittest.main()
