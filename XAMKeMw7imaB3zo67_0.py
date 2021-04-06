
def trace_word_path(word, grid):
    n, m = len(grid), len(grid[0])
    dirs = {(0, 1), (0, -1), (1, 0), (-1, 0)}
    ans = [[(i, j)] for j in range(m) for i in range(n) \
            if grid[i][j] == word[0]]
    for k in range(1, len(word)):
        ans = [a+[(a[-1][0]+i, a[-1][1]+j)] for a in ans for (i, j) in dirs
               if a[-1][0]+i in range(n) and a[-1][1]+j in range(m) and
               word[k] == grid[a[-1][0]+i][a[-1][1]+j] 
               and (a[-1][0]+i,a[-1][1]+j) not in a]
    return 'Not present' if not ans else ans[0]

