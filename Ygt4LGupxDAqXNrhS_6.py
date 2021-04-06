
def spotlight_map(grid):
    if grid == []:
        return []
    H, W = len(grid), len(grid[0])
    if H == 0:
        return []
    if W == 0:
        return [[]]
    ans = [[0 for _ in range(W)] for __ in range(H)]
    for row in range(H):
        for col in range(W):
            S = 0
            if row > 0:
                S += sum(grid[row-1][max(0, col-1):min(W, col+2)])
            S += sum(grid[row][max(0, col-1):min(W, col+2)])
            if row < H - 1:
                S += sum(grid[row+1][max(0, col-1):min(W, col+2)])
            ans[row][col] = S
    return ans

