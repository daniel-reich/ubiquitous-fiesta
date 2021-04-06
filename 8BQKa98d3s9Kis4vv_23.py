
def final(r, c, i):
    M = [[0 for col in range(c)] for row in range(r)]
    col_inc, row_inc = {}, {}
    for inc in i:
        if inc[-1] == 'r':
            row = int(inc[:-1])
            row_inc[row] = row_inc.get(row, 0) + 1
        else:
            col = int(inc[:-1])
            col_inc[col] = col_inc.get(col, 0) + 1
    for row in row_inc:
        M[row] = [row_inc[row]] * c
    for col in col_inc:
        add = col_inc[col]
        for row in range(r):
            M[row][col] += add
    return M

