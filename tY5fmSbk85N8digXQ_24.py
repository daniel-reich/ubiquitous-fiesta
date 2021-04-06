
def ones_infection(arr):
    positions = [[i, j] for i in range(len(arr)) for j in range(len(arr[0])) if arr[i][j] == 1]
    for position in positions:
        arr[position[0]] = [1 for x in range(len(arr[0]))]
        for k in range(len(arr)):
            arr[k][position[1]] = 1
    return arr

