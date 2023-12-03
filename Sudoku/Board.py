# TODO remove noinspection line
# noinspection PyUnresolvedReferences
from Cell import Cell
from gui_constants import *
import pygame


# Specification of Board
class Board:
    # Constructor
    def __init__(self, width, height, screen, difficulty):
        self.screen = screen
        self.width = width
        self.height = height
        self.difficulty = difficulty

    # Draw an outline of the Sudoku grid and the cells
    # TODO Draw the cells
    def draw(self):
        # Draw the horizontal lines
        for row in range(1, BOARD_ROWS):
            # Every third row, draw a thicker line to accentuate supernodes
            if row % 3 == 0:
                # Draw a thicker line to accentuate supernodes
                pygame.draw.line(self.screen,
                                 BLACK,
                                 (0, row * CELL_SIZE),
                                 (WIDTH, row * CELL_SIZE),
                                 10)
            # Otherwise, draw a thin line
            else:
                pygame.draw.line(self.screen,
                                 BLACK,
                                 (0, row * CELL_SIZE),
                                 (WIDTH, row * CELL_SIZE),
                                 2)

        # Draw the vertical lines
        for column in range(1, BOARD_COLS):
            # Every third column, draw a thicker line to accentuate supernodes
            if column % 3 == 0:
                pygame.draw.line(self.screen,
                                 BLACK,
                                 (column * CELL_SIZE, 0),
                                 (column * CELL_SIZE, HEIGHT),
                                 10
                                 )
            # Otherwise, draw a thin line
            else:
                pygame.draw.line(self.screen,
                                 BLACK,
                                 (column * CELL_SIZE, 0),
                                 (column * CELL_SIZE, HEIGHT),
                                 2
                                 )

    # TODO Select a cell
    def select(self, row, col):
        pass

    # TODO return a tuple of the row and column that was clicked
    def click(self, x, y):
        pass

    # TODO Clear a cell
    def clear(self):
        pass

    # TODO set the sketched value
    def sketch(self, value):
        pass

    # TODO Set the value of the selected cell equal to value
    def place_number(self, value):
        pass

    # TODO reset all cells in the board
    def reset_to_original(self):
        pass

    # TODO Return a bool indicating if the board is full
    def is_full(self):
        pass
