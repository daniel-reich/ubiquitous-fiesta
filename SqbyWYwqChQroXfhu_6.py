
def lower_triang(arr):
    for x in range(len(arr)-1,-1,-1):
        for y in range(x):
            arr[y][x] = 0
    return arr

