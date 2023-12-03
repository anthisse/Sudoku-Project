import pygame
from gui_constants import *


# Specification for Cell
class Cell:
    # Constructor
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    # Set the cell's current value
    def set_cell_value(self, value):
        self.value = value

    # TODO Set the cell's current sketched value
    def set_sketched_value(self, value):
        pass

    # Draw the cell
    # def draw(self, screen):
    #     # FIXME This font size definitely needs to change
    #     cell_font = pygame.font.Font(None, 30)
    #     cell_surf = cell_font.render(self.value, 1, BLACK)
    #     if self.value() == 0:
    #         cell_surf.get_rect(center=self)
    #     # For each row
    #     for row in range(BOARD_ROWS):
    #         # For each column
    #         for column in range(BOARD_COLS):
    #             # If the cell is empty


