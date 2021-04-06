
def floyd(up_to=None, n_row=None):
    res, row, last = [[1]], 0, 1
    while (n_row and row < n_row - 1) or (up_to and last < up_to):
        row += 1
        res.append(list(range(last + 1, last + row + 2)))
        last = res[-1][-1]
    return res

