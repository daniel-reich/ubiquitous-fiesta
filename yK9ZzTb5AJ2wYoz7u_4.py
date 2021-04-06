
def floyd(up_to = None, n_row = None):
    if up_to != None:
        rows = 1
        while rows * (rows + 1) // 2 < up_to:
            rows += 1
    else:
        rows = n_row
    ans = []
    start = 1
    for row in range(1, rows + 1):
        ans.append(list(range(start, start + row)))
        start += row
    return ans

