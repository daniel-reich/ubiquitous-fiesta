
def most_overlapped_block(grid_width, points):
    grid = [[0]*grid_width for i in range(grid_width)]
    for p in points:
        ci = grid_width - p[0]
        cj = p[1] - 1
        di = p[2]
        for i in range(ci - di, ci + di + 1):
            dj = abs(di - abs(ci - i))
            for j in range(cj - dj, cj + dj + 1):
                if i>=0 and i<grid_width and j>=0 and j<grid_width:
                    grid[i][j] += 1
    m = max(map(max, grid))
    return(m)

