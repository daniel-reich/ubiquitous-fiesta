
def exit_maze(maze, directions):
    ln = len(maze)
    for r in range(ln):
        for c in range(ln):
            if maze[r][c] == 2:
                x = r
                y = c
                break
    for i in directions:
        if i   == 'N':    x -= 1
        elif i == 'S':    x += 1
        elif i == 'E':    y += 1
        elif i == 'W':    y -= 1
        if not 0 <= x < ln:     return 'Dead'
        if not 0 <= y < ln:     return 'Dead'
        if maze[x][y] == 3:     return 'Finish'
        if maze[x][y] == 1:     return 'Dead'
    return 'Lost'

