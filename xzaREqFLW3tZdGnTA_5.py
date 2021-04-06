
def convertCords(grid, bx, by, w):
    x = bx - 1 - w
    y = len(grid) - by - w
    return x, y
​
def createBlock(w):
    block =  []
    row = []
​
    for i in range(w * 2 + 1):
        row = []
        for j in range(w * 2 + 1):
            row.append(0)
        block.append(row)
​
    for i in range(w):
        start = ((len(block) - 1) // 2) - i
        end = len(block) - 1 - start
        for j in range(start, end + 1):
            block[i][j] = 1
​
    for i in range(len(block)):
        block[w][i] = 1
​
    for i in range(w):
        start = ((len(block) - 1) // 2) - i
        end = len(block) - 1 - start
        for j in range(start, end + 1):
            block[w * 2 - i][j] = 1
​
    return block
​
def most_overlapped_block(width, points):
    grid = []
    for i in range(width):
        row = []
        for j in range(width):
            row.append(0)
        grid.append(row)
​
    for point in points:
        bx = point[0]
        by = point[1]
        w = point[2]
        x, y = convertCords(grid, bx, by, w)
        block = createBlock(w)
​
        for by in range(len(block)):
            ay = by + y
            for bx in range(len(block)):
                ax = bx + x
                if ax >= 0 and ax < len(grid) and ay >= 0 and ay < len(grid):
                    if block[by][bx] == 1:
                        grid[ay][ax] += 1
​
    currmax = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            currscr = grid[i][j]
            if currscr > currmax:
                currmax = currscr
​
    return currmax

