# TODO this clutters the namespace. Consider importing only necessary methods from math & random
import math
import random
import Cell
import Board
from gui_constants import *


# Specification of SudokuGenerator
class SudokuGenerator:
    # Constructor
    def __init__(self, removed_cells, row_length=9):
        self.row_length = row_length
        self.removed_cells = removed_cells
        # TODO initialize as a 2D int list to represent the board
        self.board = self.initialize_board()

        # Dependency for fill_remaining
        self.box_length = math.sqrt(row_length)

    # Initialize the board. Set every cell's value to 0
    # TODO should this be @staticmethod?
    def initialize_board(self):
        board = []
        for row in range(BOARD_ROWS):
            row = []
            for column in range(BOARD_COLS):
                row.append(0)
            board.append(row)
        return board

    # returns a 2D python list of numbers
    def get_board(self):
        return self.board

    # Print the board to the terminal
    def print_board(self):
        for i, row in enumerate(self.get_board()):
            for j, col in enumerate(row):
                print(self.board[i][j], end=" ")
            print()

    # Check if a number is repeated in a row
    def valid_in_row(self, row, num):
        pass

    # Check if a number is repeated in a column
    def valid_in_col(self, col, num):
        pass

    # I would rather this be called is_valid_in_supercell or
    # is_valid_in_supernode but the guidelines don't allow -Ant
    # Check if a number is repeated in a supernode
    def valid_in_box(self, row_start, col_start, num):
        pass

    # Check if a number is valid in a cell by using previous three methods
    # FIXME self.valid_in_box() needs args
    def is_valid(self, row, col, num):
        return self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box()

    # Fill a 3x3 supernode with random, unique values
    def fill_box(self, row_start, col_start):
        pass

    # Fill the three supercells on the main diagonal of the board (supercells starting at (0,0), (3,3), and (6,6))
    def fill_diagonal(self):
        pass

    # BEWARE: DO NOT ALTER!
    # From https://github.com/zhoulisha/Sudoku-Project/
    # Fill the remaining cells of the board after diagonal cells have been filled
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    # BEWARE: DO NOT ALTER!
    # From https://github.com/zhoulisha/Sudoku-Project/
    # Constructs a solution by calling fill_diagonal and fill_remaining
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    # TODO Randomly remove some cells from the board by setting the value to 0. If it is already 0, do not remove it again.
    def remove_cells(self):
        pass


# BEWARE: DO NOT ALTER!
# Initialize a SudokuGenerator, fill its values, remove some cells, and return the solution as 2D lists
# From https://github.com/zhoulisha/Sudoku-Project/
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
