
def get_diagonals(lst):
    diag1 = []
    diag2 = []
    for i in range(len(lst)):
        diag1.append(lst[i][i])
        diag2.append(lst [i][::-1][i])
    return [diag1, diag2]

