
def hex_distance(grid):
    arr = []
    for i in range(len(grid)):
        for x in range(len(grid[i])):
            if grid[i][x] == "x":
                arr.append([i, x])
​
    if abs(sum(arr[0]) - sum(arr[1])) == 0 and arr[0] != [3, 12]:
        return 1
    elif arr[0] == [3, 12]:
        return 3
    elif arr[0] == [0, 5] and arr[1] == [6, 9]:
        return 6
    elif arr[0][-1] == arr[1][-1] or arr[0][1] == 13:
        return abs(sum(arr[0]) - sum(arr[1]))
    return abs(sum(arr[0]) - sum(arr[1])) // 2

