
def ones_infection(arr):
    fill_cols = [any(arr[r][c] == 1 for r in range(len(arr))) for c in range(len(arr[0]))]
    fill_rows = [any(arr[r][c] == 1 for c in range(len(arr[0]))) for r in range(len(arr))]
    for r in range(len(arr)):
       for c in range(len(arr[0])):
           arr[r][c] = int(fill_cols[c] or fill_rows[r])
    return arr

