
dplus = [[1, 0], [-1, 0], [0, 1], [0, -1]]
dstar = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
​
def all_explode(grid):
    assert grid[0][0] in ['+', 'x']
    explosion_queue = [(0, 0, grid[0][0])]
    bombs = set()
    W, H = len(grid[0]), len(grid)
    for row in range(H):
        for col in range(W):
            if grid[row][col] in ['+', 'x']:
                bombs.add((row, col))
    while len(explosion_queue):
        (row, col, btype) = explosion_queue.pop(0)
        neighbourhood = dplus if btype == '+' else dstar
        bombs.remove((row, col))
        for drow, dcol in neighbourhood:
            row2, col2 = row + drow, col + dcol
            if (row2, col2) in bombs and \
               (row2, col2, grid[row2][col2]) not in explosion_queue:
                explosion_queue.append((row2, col2, grid[row2][col2]))
    return len(bombs) == 0

