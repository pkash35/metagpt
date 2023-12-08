## main.py
import tkinter as tk
from gui import GUI

def main():
    root = tk.Tk()
    gui = GUI(root)
    gui.start_new_game()
    root.mainloop()

if __name__ == "__main__":
    main()
