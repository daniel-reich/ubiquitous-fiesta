
def islands_perimeter(grid):
    ans = 0
    h, w = len(grid), len(grid[0])
    grid = [[0] * (w+2)] + [[0]+row+[0] for row in grid]+ [[0] * (w+2)]
    for row in range(1, h+1):
        for col in range(1, w+1):
            if grid[row][col] == 1:
                ans += 4 - sum([grid[row-1][col], grid[row+1][col], \
                                grid[row][col-1], grid[row][col-1]])
    return ans

