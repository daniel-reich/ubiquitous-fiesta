
def ones_infection(arr):
    row_ones = set()
    col_ones = set()
    H, W = len(arr), len(arr[0])
    for i in range(H):
        row = arr[i]
        if 1 in row:
            row_ones.add(i)
            for col in range(W):
                if row[col] == 1:
                    col_ones.add(col)
    for row in row_ones:
        arr[row] = [1] * W
    for col in col_ones:
        for row in range(H):
            arr[row][col] = 1
    return arr

