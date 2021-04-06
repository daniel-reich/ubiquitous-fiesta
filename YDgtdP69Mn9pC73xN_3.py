
from collections import defaultdict
from collections import defaultdict
def num_grid(lst):
    d = defaultdict(int)
    check = []
    for r in range(len(lst)):
        for c in range(len(lst[0])):
            if lst[r][c] == '#':
                check.append((r,c))
    for m in range(len(lst)):
        for n in range(len(lst[0])):
            for t in check:
                if (abs(m-t[0]) <= 1 and abs(n-t[1]) <=1
                    and (m,n) != t):
                    d[(m,n)] += 1
    grid = lst.copy()
    for i in d:
        grid[i[0]][i[1]] = str(d[i])
    for a in range(len(grid)):
        for b in range(len(grid[0])):
            if grid[a][b] == '-':
                grid[a][b] ='0'
        for g in check:
            grid[g[0]][g[1]] = '#'
    return grid

