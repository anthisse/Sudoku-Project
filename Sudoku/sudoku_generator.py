class SudokuGenerator:
    def __init__(self, row_length=9, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells #see UI Requirements
    #def get_board(self): #returns a 2D python list of numbers
    def print_board(self):
        return
    def valid_in_row(self, row, num):
        self.row = row
        se;f.num = num
    def valid_in_col(self, col, num):
        self.col = col
        self.num = num
    def valid_in_box(self, row_start, col_start, num):
        self.row_start = row_start
        self.col_start = col_start
    def is_valid(self, row, col, num):

    def fill_box(self, row_start, col_start):

