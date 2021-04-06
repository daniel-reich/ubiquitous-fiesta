
def is_mini_sudoku(square):
    return sum([(sum(set(i))) for i in square]) == 45

