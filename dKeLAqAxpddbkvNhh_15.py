
def group_seats(lst, n):
    f, row, col = 0, len(lst), len(lst[0])
    for i in range(row):
        for j in range(col-n+1):
            if set(lst[i][j: j+n]) == {0}:
                f += 1
    return f

