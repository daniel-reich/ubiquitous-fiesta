
def is_mini_sudoku(square):
    lstconcat = square[0]+square[1]+square[2]
    lstconcat.sort()
    setl = set(lstconcat)
​
    if len(setl) == 9:
        for x in range (9):
            if lstconcat[x] != x+1:
                return False
        return True
        
    return False

