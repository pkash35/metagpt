## test_sudoku.py
import unittest
from sudoku_game.sudoku import Sudoku

class TestSudoku(unittest.TestCase):
    def setUp(self):
        self.sudoku = Sudoku()

    ## Test initialization
    def test_initialization(self):
        self.assertEqual(len(self.sudoku.grid), 9)
        for row in self.sudoku.grid:
            self.assertEqual(len(row), 9)
            self.assertEqual(sum(row), 0)

    ## Test is_valid_placement
    def test_is_valid_placement(self):
        self.sudoku.grid[0][0] = 1
        self.assertFalse(self.sudoku.is_valid_placement(0, 1, 1))
        self.assertFalse(self.sudoku.is_valid_placement(1, 0, 1))
        self.assertFalse(self.sudoku.is_valid_placement(1, 1, 1))
        self.assertTrue(self.sudoku.is_valid_placement(0, 1, 2))

    ## Test find_empty_position
    def test_find_empty_position(self):
        self.assertEqual(self.sudoku.find_empty_position(), (0, 0))
        self.sudoku.grid[0][0] = 1
        self.assertEqual(self.sudoku.find_empty_position(), (0, 1))

    ## Test solve_puzzle
    def test_solve_puzzle(self):
        self.sudoku.solve_puzzle()
        for row in self.sudoku.grid:
            self.assertEqual(len(set(row)), 9)
        for col in range(9):
            self.assertEqual(len(set([self.sudoku.grid[row][col] for row in range(9)])), 9)

    ## Test generate_puzzle
    def test_generate_puzzle(self):
        self.sudoku.generate_puzzle()
        self.assertTrue(any(0 in row for row in self.sudoku.grid))

    ## Test get_hint
    def test_get_hint(self):
        self.sudoku.generate_puzzle()
        row, col, num = self.sudoku.get_hint()
        self.assertTrue(0 <= row <= 8)
        self.assertTrue(0 <= col <= 8)
        self.assertTrue(1 <= num <= 9)
        self.assertTrue(self.sudoku.is_valid_placement(row, col, num))

if __name__ == '__main__':
    unittest.main()
