# snake.py
import random
import curses

class Snake:
    def __init__(self):
        self.body = [(10, 10), (10, 9), (10, 8)]
        self.direction = curses.KEY_RIGHT  # Initial direction

    def move(self, key):
        # Update direction based on user input
        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            self.direction = key

        # Calculate the new head position
        y, x = self.body[0]
        if self.direction == curses.KEY_UP:
            y -= 1
        elif self.direction == curses.KEY_DOWN:
            y += 1
        elif self.direction == curses.KEY_LEFT:
            x -= 1
        elif self.direction == curses.KEY_RIGHT:
            x += 1

        # Insert the new head position
        self.body.insert(0, (y, x))

        # Remove the tail position
        self.body.pop()

    def grow(self):
        # Add a new tail position
        self.body.append(self.body[-1])

    def check_collision(self):
        # Check if the head collides with the body or the border
        y, x = self.body[0]
        if (y, x) in self.body[1:] or y < 0 or y >= 20 or x < 0 or x >= 20:
            return True
        return False
