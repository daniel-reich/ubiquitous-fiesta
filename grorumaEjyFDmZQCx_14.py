
def is_wristband(lst):
    return all(all(v == row[0] for v in row) for row in lst) \
        or all(all(row[i] == lst[0][i] for i in range(len(row))) for row in lst) \
        or all(all(lst[i][j] == lst[i+1][j+1] for j in range(len(lst[0])-1)) for i in range(len(lst)-1)) \
        or all(all(lst[i][j] == lst[i-1][j+1] for j in range(len(lst[0])-1)) for i in range(1, len(lst)))

