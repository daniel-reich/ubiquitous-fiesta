
def spiral_matrix(side, string):
    n = side**2
    if len(string) < n:
        string += '+' * (n - len(string))
    if len(string) > n:
        string = string[:n]
    S = [c for c in string]
    empty = ' '
    M = [[empty for _ in range(side)] for __ in range(side)]
    if side % 2 == 0:
        row, col = side // 2 - 1, side // 2 - 1
    else:
        row, col = side // 2, side // 2
    M[row][col] = S.pop(0)
    col += 1
    M[row][col] = S.pop(0)
    direction = 0       # directions: 0=right, 1=down, 2=left, 3=up
    while len(S) > 0:
        cur_dir = direction
        if cur_dir == 0:
            # currently moving right:
            if row < side - 1 and M[row+1][col] == empty:
                # turn right, i.e. go down:
                row += 1
                direction = 1
            else:
                # keep going right:
                col += 1
        elif cur_dir == 1:
            # currently moving down:
            if col > 0 and M[row][col-1] == empty:
                # turn right, i.e. go left:
                col -= 1
                direction = 2
            else:
                # keep going down:
                row += 1
        elif cur_dir == 2:
            # currently moving left:
            if row > 0 and M[row-1][col] == empty:
                # turn right, i.e. go up:
                row -= 1
                direction = 3
            else:
                # keep going right:
                col -= 1
        elif cur_dir == 3:
            # currently moving up:
            if col < side - 1 and M[row][col+1] == empty:
                # turn right, i.e. go right:
                col += 1
                direction = 0
            else:
                # keep going up:
                row -= 1
        M[row][col] = S.pop(0)
    return M

