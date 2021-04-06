
def lower_triang(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr[i])):
            arr[i][j] = 0
    return arr

