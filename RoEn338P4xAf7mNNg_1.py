
def shortest_path(lst):
    locations = {}
    for row in range(len(lst)):
        for col in range(len(lst[0])):
            if lst[row][col] != '0':
                locations[int(lst[row][col])] = (row, col)
    if len(locations.keys()) == 0:
        return 0
    ans = 0
    row1, col1 = locations[1]
    for i in range(2, max(locations.keys()) + 1):
        row2, col2 = locations[i]
        ans += abs(row1 - row2) + abs(col1 - col2)
        row1, col1 = row2, col2
    return ans

