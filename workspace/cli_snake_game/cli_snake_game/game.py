## game.py
import curses
from snake import Snake
from food import Food

class Game:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.score = 0
        self.snake = Snake()
        self.food = Food()

    def start_game(self):
        # Game loop
        while True:
            self.stdscr.clear()

            # Draw the snake
            for y, x in self.snake.body:
                self.stdscr.addch(y, x, '#')

            # Draw the food
            self.stdscr.addch(self.food.position[0], self.food.position[1], '*')

            # Update the screen
            self.stdscr.refresh()

            # Get user input
            key = self.stdscr.getch()

            # Move the snake with the user input
            self.snake.move(key)

            # Check for collision
            if self.snake.check_collision():
                self.end_game()

            # Check if the snake ate the food
            if self.snake.body[0] == self.food.position:
                self.snake.grow()
                self.food.generate()
                self.update_score()

    def end_game(self):
        # End the game
        self.stdscr.addstr(0, 0, "Game Over! Score: " + str(self.score))
        self.stdscr.refresh()
        curses.napms(2000)
        curses.endwin()
        quit()

    def restart_game(self):
        # Restart the game
        self.score = 0
        self.snake = Snake()
        self.food = Food()
        self.start_game()

    def update_score(self):
        # Update the score
        self.score += 1
