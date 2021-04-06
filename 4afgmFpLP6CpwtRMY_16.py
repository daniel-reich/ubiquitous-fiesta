
def sudoku_validator(x):
    i = 0
    col_list = []
    square_list = []
    for m in range(0,len(x)):
       for n in range(0,len(x[m])):
            if x[m][n] not in range(1,10):
               return False 
            if set(x[m]) != set(range(1,10)):
               return False
            if (m == 0 or m % 3 == 0) and  (n + 1) % 3 == 0:
                for p in range(0,3):
                    for q in range(0,3):
                        square_list += [x[m+p][n-q]] 
                if set(square_list) != set(range(1,10)):
                    return False
            square_list = []
    while i < 9:
        col_list = [x[j][i] for j in range(0,9)]
        if set(col_list) != set(range(1,10)):
            return False
        i += 1
    return True

