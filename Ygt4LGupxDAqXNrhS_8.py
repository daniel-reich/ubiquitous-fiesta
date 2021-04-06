
def spotlight_map(grid):
    if not grid:
        return []
    
    rows, cols = len(grid), len(grid[0])
    res = [[0]*cols for _ in range(rows)]
    neighbours = [[-1, -1], [-1, 0], [-1, 1], 
                  [0, -1], [0, 0], [0, 1], 
                  [1, -1], [1, 0], [1, 1]]
​
    for r in range(rows):
        for c in range(cols):
            total = 0
            for i, j in neighbours:
                if 0 <= r+i < rows and 0 <= c+j < cols:
                    total += grid[r+i][c+j]
            res[r][c] = total
    return res

