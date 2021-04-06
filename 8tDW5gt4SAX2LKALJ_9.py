
def cross(r, c, rlen, clen): 
    return [(row, col) for row, col in [[r + 1, c + 1], [r + 1, c - 1], [r - 1, c + 1], [r - 1, c - 1]] \
                if 0 <= row < rlen and 0 <= col < clen]
        
def plus(r, c, rlen, clen): 
    return [(row, col) for row, col in [[r, c + 1], [r, c - 1], [r + 1, c], [r - 1, c]] \
                if 0 <= row < rlen and 0 <= col < clen]
​
def bomb_cells_set(grid):
    bcs = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != '0':
                bcs.add((r, c))
    return bcs
​
def detonate_bomb(grid, row, col):
    dirs = cross if grid[row][col] == 'x' else plus
    grid[row][col] = '0'
    for r, c in dirs(row, col, len(grid), len(grid[0])):
        if grid[r][c] != '0':
            detonate_bomb(grid, r, c)
​
def min_bombs_needed(grid):
    bcs = bomb_cells_set(grid)
    if len(bcs) == 0:
        return 0
    nb = 0
    for cell in bcs:
        if grid[cell[0]][cell[1]] != '0':
            nb += 1
            detonate_bomb(grid, *cell)
    return nb

