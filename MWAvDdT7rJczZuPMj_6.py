
def count_word(grid, word):
​
    def j_pos(grid, row, col, x, y, cnt, pos):
        if y+1 < col and cnt <= len(word)-1 and grid[x][y+1].upper() == word[0+cnt]:
            pos.append((x, y+1))
            j_pos(grid, row, col, x, y+1, cnt+1, pos)
        if len(pos) == len(word):
            for i in pos:
                grid[i[0]][i[1]] = grid[i[0]][i[1]].lower()
    def j_neg(grid, row, col, x, y, cnt, pos):
        if y-1 >= 0 and cnt <= len(word)-1 and grid[x][y-1].upper() == word[0+cnt]:
            pos.append((x, y-1))
            j_neg(grid, row, col, x, y-1, cnt+1, pos)
        if len(pos) == len(word):
            for i in pos:
                grid[i[0]][i[1]] = grid[i[0]][i[1]].lower()
    def i_pos(grid, row, col, x, y, cnt, pos):
        if x+1 < row and cnt <= len(word)-1 and grid[x+1][y].upper() == word[0+cnt]:
            pos.append((x+1, y))
            i_pos(grid, row, col, x+1, y, cnt+1, pos)
        if len(pos) == len(word):
            for i in pos:
                grid[i[0]][i[1]] = grid[i[0]][i[1]].lower()
    def i_neg(grid, row, col, x, y, cnt, pos):
        if x-1 >= 0 and cnt <= len(word)-1 and grid[x-1][y].upper() == word[0+cnt]:
            pos.append((x-1, y))
            i_neg(grid, row, col, x-1, y, cnt+1, pos)
        if len(pos) == len(word):
            for i in pos:
                grid[i[0]][i[1]] = grid[i[0]][i[1]].lower()
    def du_pos(grid, row, col, x, y, cnt, pos):
        if x-1 >= 0 and y+1 < col and cnt <= len(word)-1 and grid[x-1][y+1].upper() == word[0+cnt]:
            pos.append((x-1, y+1))
            du_pos(grid, row, col, x-1, y+1, cnt+1, pos)
        if len(pos) == len(word):
            for i in pos:
                grid[i[0]][i[1]] = grid[i[0]][i[1]].lower()
    def du_neg(grid, row, col, x, y, cnt, pos):
        if x-1 >= 0 and y-1 >= 0 and cnt <= len(word)-1 and grid[x-1][y-1].upper() == word[0+cnt]:
            pos.append((x-1, y-1))
            du_neg(grid, row, col, x-1, y-1, cnt+1, pos)
        if len(pos) == len(word):
            for i in pos:
                grid[i[0]][i[1]] = grid[i[0]][i[1]].lower()
    def dd_pos(grid, row, col, x, y, cnt, pos):
        if x+1 < row and y+1 < col and cnt <= len(word)-1 and grid[x+1][y+1].upper() == word[0+cnt]:
            pos.append((x+1, y+1))
            dd_pos(grid, row, col, x+1, y+1, cnt+1, pos)
        if len(pos) == len(word):
            for i in pos:
                grid[i[0]][i[1]] = grid[i[0]][i[1]].lower()
    def dd_neg(grid, row, col, x, y, cnt, pos):
        if x+1 < row and y-1 >= 0 and cnt <= len(word)-1 and grid[x+1][y-1].upper() == word[0+cnt]:
            pos.append((x+1, y-1))
            dd_neg(grid, row, col, x+1, y-1, cnt+1, pos)
        if len(pos) == len(word):
            for i in pos:
                grid[i[0]][i[1]] = grid[i[0]][i[1]].lower()
​
    row = len(grid)
    col = len(grid[0])
    pos = []
    res = 0
​
    for i in range(row):
        for j in range(col):
            if grid[i][j].upper() == word[0]:
                pos.append((i, j))
                j_pos(grid, row, col, i, j, 1, pos)
                if len(pos) == len(word): res += 1
                pos = []
                pos.append((i, j))
                j_neg(grid, row, col, i, j, 1, pos)
                if len(pos) == len(word): res += 1
                pos = []
                pos.append((i, j))
                i_pos(grid, row, col, i, j, 1, pos)
                if len(pos) == len(word): res += 1
                pos = []
                pos.append((i, j))
                i_neg(grid, row, col, i, j, 1, pos)
                if len(pos) == len(word): res += 1
                pos = []
                pos.append((i, j))
                du_pos(grid, row, col, i, j, 1, pos)
                if len(pos) == len(word): res += 1
                pos = []
                pos.append((i, j))
                du_neg(grid, row, col, i, j, 1, pos)
                if len(pos) == len(word): res += 1
                pos = []
                pos.append((i, j))
                dd_pos(grid, row, col, i, j, 1, pos)
                if len(pos) == len(word): res += 1
                pos = []
                pos.append((i, j))
                dd_neg(grid, row, col, i, j, 1, pos)
                if len(pos) == len(word): res += 1
                pos = []
​
    return((res, grid))

