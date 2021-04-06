
def minesweeper(grid):
    H, W = len(grid), len(grid[0])
    for r in range(H):
        for c in range(W):
            if grid[r][c] == '?':
                cnt = 0
                for r2 in range(r - 1, r + 2):
                    for c2 in range(c - 1, c + 2):
                        if 0 <= r2 < H and 0 <= c2 < W and grid[r2][c2] == '#':
                            cnt += 1
                grid[r][c] = str(cnt)
    return grid

