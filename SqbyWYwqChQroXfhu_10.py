
def lower_triang(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if j > i:
                arr[i][j] = 0
    return arr

