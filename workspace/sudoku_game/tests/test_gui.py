## test_gui.py
import unittest
import tkinter as tk
from unittest.mock import patch, MagicMock
from sudoku_game.gui import GUI
from sudoku_game.sudoku import Sudoku

class TestGUI(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.gui = GUI(self.root)

    def test_init(self):
        self.assertIsInstance(self.gui.root, tk.Tk)
        self.assertIsInstance(self.gui.sudoku, Sudoku)
        self.assertEqual(len(self.gui.entries), 9)
        for row in self.gui.entries:
            self.assertEqual(len(row), 9)

    def test_draw_grid(self):
        self.gui.draw_grid()
        for row in self.gui.entries:
            for entry in row:
                self.assertIsInstance(entry, tk.Entry)

    def test_draw_numbers(self):
        self.gui.sudoku.grid = [[1 if i == j else 0 for j in range(9)] for i in range(9)]
        self.gui.draw_grid()
        self.gui.draw_numbers()
        for i in range(9):
            self.assertEqual(self.gui.entries[i][i].get(), '1')

    def test_start_new_game(self):
        with patch.object(Sudoku, 'generate_puzzle') as mock_generate_puzzle:
            self.gui.start_new_game()
        mock_generate_puzzle.assert_called_once()

    def test_get_user_input(self):
        self.gui.draw_grid()
        self.gui.entries[0][0].insert(tk.END, '5')
        self.assertEqual(self.gui.get_user_input(0, 0), 5)

    def test_get_user_input_invalid(self):
        self.gui.draw_grid()
        self.gui.entries[0][0].insert(tk.END, 'a')
        self.assertIsNone(self.gui.get_user_input(0, 0))

    def test_erase_input(self):
        self.gui.draw_grid()
        self.gui.entries[0][0].insert(tk.END, '5')
        self.gui.erase_input(0, 0)
        self.assertEqual(self.gui.entries[0][0].get(), '')

    def test_show_hint(self):
        with patch.object(Sudoku, 'get_hint') as mock_get_hint:
            mock_get_hint.return_value = (0, 0, 5)
            self.gui.draw_grid()
            self.gui.show_hint()
        self.assertEqual(self.gui.entries[0][0].get(), '5')

    def test_show_solution(self):
        with patch.object(Sudoku, 'solve_puzzle') as mock_solve_puzzle:
            mock_solve_puzzle.return_value = [[i+j for j in range(9)] for i in range(9)]
            self.gui.draw_grid()
            self.gui.show_solution()
        for i in range(9):
            for j in range(9):
                self.assertEqual(self.gui.entries[i][j].get(), str(i+j))

if __name__ == '__main__':
    unittest.main()
