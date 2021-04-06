
def is_mini_sudoku(square):
    return (len(set(square[0]+square[1]+square[2])) == 9 and sum(square[0]+square[1]+square[2]) == 45)

