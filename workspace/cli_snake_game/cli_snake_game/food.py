import random

class Food:
    def __init__(self, grid_size=20):
        self.position = (0, 0)
        self.grid_size = grid_size
        self.generate()

    def generate(self):
        # Generate a new position for the food within the grid
        self.position = (random.randint(0, self.grid_size), random.randint(0, self.grid_size))
