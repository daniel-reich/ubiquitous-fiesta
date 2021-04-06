
def is_mini_sudoku(square):
    numsSeen = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False}
    for grid in square:
        for num in grid:
            if numsSeen.get(num, None) == None or numsSeen.get(num, None) == True:
                return False
            else:
                numsSeen[num] = True
    return True

