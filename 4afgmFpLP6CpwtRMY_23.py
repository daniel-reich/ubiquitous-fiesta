
def validate_list9(lst):
    return len(lst) == 9 and all(lst.count(i) == 1 for i in range(1, 10))
​
​
def sudoku_validator(x):
    for row in x:
        if not validate_list9(row):
            return False
    for j in range(9):
        col = []
        for i in range(9):
            col.append(x[i][j])
        if not validate_list9(col):
            return False
    for i in range(3):
        for j in range(3):
            box_3x3 = (x[i * 3][j * 3: (j + 1) * 3]
                       + x[i * 3 + 1][j * 3: (j + 1) * 3]
                       + x[i * 3 + 2][j * 3: (j + 1) * 3])
            if not validate_list9(box_3x3):
                return False
    return True

