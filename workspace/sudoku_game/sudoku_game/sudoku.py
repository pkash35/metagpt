## sudoku.py
import random
from typing import List, Tuple, Optional

class Sudoku:
    def __init__(self):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]

    def generate_puzzle(self) -> List[List[int]]:
        self.solve_puzzle()
        for _ in range(40):
            row, col = random.randint(0, 8), random.randint(0, 8)
            self.grid[row][col] = 0
        return self.grid

    def is_valid_placement(self, row: int, col: int, num: int) -> bool:
        for x in range(9):
            if self.grid[row][x] == num or self.grid[x][col] == num:
                return False

        start_row, start_col = row - row % 3, col - col % 3
        for i in range(3):
            for j in range(3):
                if self.grid[i + start_row][j + start_col] == num:
                    return False
        return True

    def find_empty_position(self) -> Optional[Tuple[int, int]]:
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    return row, col
        return None

    def solve_puzzle(self) -> Optional[List[List[int]]]:
        position = self.find_empty_position()
        if not position:
            return self.grid

        row, col = position
        for num in range(1, 10):
            if self.is_valid_placement(row, col, num):
                self.grid[row][col] = num
                if self.solve_puzzle():
                    return self.grid
                self.grid[row][col] = 0
        return None

    def get_hint(self) -> Tuple[int, int, int]:
        position = self.find_empty_position()
        if not position:
            return -1, -1, -1

        row, col = position
        for num in range(1, 10):
            if self.is_valid_placement(row, col, num):
                return row, col, num
        return -1, -1, -1
