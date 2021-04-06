
def ones_infection(arr):
    ht = len(arr)
    ln = len(arr[0])
​
    for h in range(ht):
        for l in range(ln):
            if arr[h][l] == 1:
                arr[h][l] = 2
​
    for h in range(ht):
        for l in range(ln):
            if arr[h][l] == 2:
                for i in range(ht):
                    if arr[i][l] == 0:
                        arr[i][l] = 1
                for j in range(ln):
                    if arr[h][j] == 0:
                        arr[h][j] = 1
​
    for h in range(ht):
        for l in range(ln):
            if arr[h][l] == 2:
                arr[h][l] = 1
​
    return arr

