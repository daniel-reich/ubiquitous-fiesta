
def sudoku_validator(x):
    return all(len(set(x[i])) == 9 for i in range(9)) and all(len(set(x[j][i] for j in range(9))) == 9 for i in range(9)) and all(len(set(x[3*j][3*i:3+3*i]+x[1+3*j][3*i:3+3*i]+x[2+3*j][3*i:3+3*i])) == 9 for i in range(3) for j in range(3))

