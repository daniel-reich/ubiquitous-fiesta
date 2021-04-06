
def lower_triang(arr):
    for row in range(len(arr)):
        for col in range(row + 1, len(arr)):
            arr[row][col] = 0
    return arr

