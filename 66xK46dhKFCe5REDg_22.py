
def x_and_o(board):
    grid = [x.split("|") for x in board]
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == " ":
                grid[r][c] = "X"
                if check(grid):
                    return [r + 1, c + 1]
                else: 
                    grid[r][c] = " "
    return False            
​
def check(x):
    r = any([set(i) == {"X"} for i in x])
    c = any([set(i) == {"X"} for i in zip(*x)])
    d1 = set([x[i][i] for i in range(len(x))]) == {"X"}
    d2 = set([x[i][len(x) - 1 - i] for i in range(len(x))]) == {"X"}
    return r or c or d1 or d2

