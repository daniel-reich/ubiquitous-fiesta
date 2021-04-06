
def exit_maze(maze, directions):
    l = len(maze)
    w = len(maze[0])
    for y in range(l):
        for x in range(w):
            if maze[y][x] == 2:
                sx = x
                sy = y
​
    for i in directions:
        if i == 'N':
            sy -= 1
        elif i == 'E':
            sx += 1
        elif i == 'S':
            sy += 1
        elif i == 'W':
            sx -= 1
        else:
            return 'Bad Direction'
​
        if sy < 0 or sy >= l:
            return 'Dead'
        if sx < 0 or sx >= w:
            return 'Dead'
        if maze[sy][sx] == 1:
            return 'Dead'
        if maze[sy][sx] == 3:
            return 'Finish'
    return 'Lost'

