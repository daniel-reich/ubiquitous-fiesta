
def sudoku_validator(game):
​
    target = 45  # first 9 numbers sums 45
​
    # row checking
    for row in game:
        if sum(row) != target:
            return False
​
    # column cheking
    for i in range(9):  # colums control
        column_sum = 0
        for j in range(9):  # rows control
            column_sum += game[j][i]
        if column_sum != target:
            return False
​
    # 3x3 box checking
    for i in [0, 3, 6]:  #columns control
        for j in [0, 3, 6]:  # rows control
            box_sum = 0
            for k in range(3):  # block control
                box_sum += sum(game[k+j][i:i+3])
            if box_sum != target:
                return False
​
    return True

