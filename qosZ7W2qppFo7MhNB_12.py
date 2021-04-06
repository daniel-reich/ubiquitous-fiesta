
def hex_distance(grid):
    a, b = [], []
    for i in range(len(grid)):
        if grid[i].count('x') == 1:
            if not a:
                a = [i, grid[i].index('x')]
            else:
                b = [i, grid[i].index('x')]
        elif grid[i].count('x') == 2:
            a = [i, grid[i].index('x')]
            b = [i, grid[i].rfind('x')]
    if b[0] == a[0]:
        return abs(b[1] - a[1]) // 2
    if abs(b[1] - a[1]) < b[0] - a[0]:
        return b[0] - a[0]
    return (b[0] - a[0]) + (abs(b[1] - a[1]) - (b[0] - a[0])) // 2

