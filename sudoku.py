class SudokuTable:
    """class sudoku table that will help
    us modelling the game board and its rules"""
    def __init__(self):
        self.chart = [[0]*9]*9

    def print_table(self):
        """prints the game board with a format"""
        row = 0
        col = 0
        for i in range(9):
            for j in range(9):
                if col == 3:
                    print '|',
                    col = 0
                if row == 3:
                    print '----------------------'
                    row = 0
                print self.chart[i][j],
                col = col + 1
            print '\n',
            col = 0
            row = row + 1
        print '\n'

    def used_in_row(self, row, num):
        """checks if the given number exists in the given row"""
        for col in range(9):
            if self.chart[row][col] == num:
                return True
        return False

    def used_in_col(self, col, num):
        """checks if the given number exists in the given col"""
        for row in range(9):
            if self.chart[row][col] == num:
                return True
        return False

    def used_in_box(self, colstart, rowstart, num):
        """checks if the given number exists in the given 3x3 box"""
        for row in range(3):
            for col in range(3):
                if self.chart[row + rowstart][col + colstart] == num:
                    return True
        return False

    def can_place(self, col, row, num):
        """checks that all the constraints are passed"""
        a = self.used_in_col(row, num)
        b = self.used_in_row(col, num)
        c = self.used_in_box(row - row % 3, col - col % 3, num)
        return  (not a) and (not b) and (not c)

    def get_empty_loc(self):
        """checks if chart is complete and return incomplete locations"""
        for row in range(9):
            for col in range(9):
                if self.chart[row][col] == 0:
                    return (row, col)
        return (-1,-1)

def solve_soduku(sudoku):
    """DFS to solve the sudoku recursively"""
    (row, col) = sudoku.get_empty_loc()
    #sudoku.print_table()
    if (row == -1) and (col == -1):
        return True

    for num in range(1,10):
        if sudoku.can_place(row, col, num):
        	sudoku.chart[row][col] = num
        	if solve_soduku(sudoku):
        		return True
        	sudoku.chart[row][col] = 0

    return False

sudoku = SudokuTable()
sudoku.chart = [
    [8,0,0,0,0,0,0,0,0],
    [0,0,3,6,0,0,0,0,0],
    [0,7,0,0,9,0,2,0,0],
    [0,5,0,0,0,7,0,0,0],
    [0,0,0,0,4,5,7,0,0],
    [0,0,0,1,0,0,0,3,0],
    [0,0,1,0,0,0,0,6,8],
    [0,0,8,5,0,0,0,1,0],
    [0,9,0,0,0,0,4,0,0]]
print '*----------Sudoku Solver------------*\n'
print '*----------Inicial Sudoku------------*'
sudoku.print_table()
if solve_soduku(sudoku):
    print '\n*----------Solved Sudoku------------*'
    sudoku.print_table()
else:
    print '\n*----------Solved Sudoku------------*'
    print '* cant solve this sudoku *'
