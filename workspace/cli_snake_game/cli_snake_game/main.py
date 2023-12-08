## main.py
import curses
from game import Game

def main(stdscr):
    # Initialize the game
    game = Game(stdscr)

    # Start the game
    try:
        game.start_game()
    except Exception as e:
        # Print any exception for debugging
        stdscr.addstr(0, 0, f"Error: {e}")
        stdscr.refresh()
        stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
