# Specification of Board
class Board:
    # Constructor
    def __init__(self, width, height, screen, difficulty):
        # TODO check to see if the screen needs to be from PyGame
        self.screen = screen

        self.width = width
        self.height = height
        self.difficulty = difficulty

    # TODO Draw an outline of the Sudoku grid
    def draw(self):
        pass

    # TODO Select a cell
    def select(self, row, col):
        pass

    # TODO return a tuple of the row and column that was clicked
    def click(self, x, y):
        pass

    # TODO Clear a cell
    def clear(self):
        pass

    # TODO


