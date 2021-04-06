
def hex_distance(grid):
    coords = [] 
    for i in range(len(grid)):
        if grid[i].count('x') == 2:
            return (grid[i].rindex('x') - grid[i].index('x'))//2
        if 'x' in grid[i]:
            coords.append((i, grid[i].index('x')))
    (y1, x1), (y2, x2) = coords
    if x2 == x1:
        return y2 - y1
    moves = 0
    while y1 < y2:
        x1 = x1 + 1 if x2 >= x1 else x1 - 1
        y1 += 1
        moves += 1
    return moves if x2 == x1 else moves + abs(x2 - x1)//2

