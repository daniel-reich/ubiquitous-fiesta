
def lower_triang(arr):
    for x in range(len(arr)):
        for y in range(len(arr[x])):
            if y>x:
                arr[x][y] = 0
    return arr

