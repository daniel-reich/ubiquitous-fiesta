
def all_explode(grid):
    counter = 0
    allex = True
    for i, row in enumerate(grid):
        if not allex:
            break
        for j, cell in enumerate(row):
            if cell == '+' or cell == 'x':
                counter += 1
                expl = ch_plus(grid, i, j) or ch_x(grid, i, j)
                if not expl and counter > 1:
                    allex = False
                    break
    return allex
​
​
def slg(l, i, j):
    if i < 0 or j < 0:
        return False
    try:
        return l[i][j]
    except IndexError:
        pass
    return False
​
​
def ch_plus(grid, i, j):
    up = slg(grid, i-1, j)
    down = slg(grid, i+1, j)
    left = slg(grid, i, j-1)
    right = slg(grid, i, j+1)
    if up == '+' or down == '+' or left == '+' or right == '+':
        return True
    else:
        return False
​
​
def ch_x(grid, i, j):
    left_up = slg(grid, i-1, j-1)
    right_up = slg(grid, i-1, j+1)
    left_down = slg(grid, i+1, j-1)
    right_down = slg(grid, i+1, j+1)
    if left_up == 'x' or right_up == 'x' or left_down == 'x' or right_down == 'x':
        return True
    else:
        return False

