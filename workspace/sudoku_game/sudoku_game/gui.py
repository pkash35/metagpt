## gui.py
import tkinter as tk
from tkinter import messagebox
from sudoku import Sudoku
from typing import Optional

class GUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.sudoku = Sudoku()
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack()

    def draw_grid(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j] = tk.Entry(self.grid_frame, width=2)
                self.entries[i][j].grid(row=i, column=j)

    def draw_numbers(self):
        for i in range(9):
            for j in range(9):
                num = self.sudoku.grid[i][j]
                if num != 0:
                    self.entries[i][j].insert(tk.END, str(num))

    def start_new_game(self):
        self.sudoku.generate_puzzle()
        self.draw_grid()
        self.draw_numbers()

    def get_user_input(self, row: int, col: int) -> Optional[int]:
        try:
            return int(self.entries[row][col].get())
        except ValueError:
            return None

    def erase_input(self, row: int, col: int):
        self.entries[row][col].delete(0, tk.END)

    def show_hint(self):
        row, col, num = self.sudoku.get_hint()
        if row != -1:
            self.entries[row][col].insert(tk.END, str(num))
        else:
            messagebox.showinfo("Hint", "No hint available")

    def show_solution(self):
        solution = self.sudoku.solve_puzzle()
        if solution:
            for i in range(9):
                for j in range(9):
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(tk.END, str(solution[i][j]))
        else:
            messagebox.showinfo("Solution", "No solution available")
