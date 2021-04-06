
def can_exit(maze):
    maze[0][0] = 5
    m = len(maze)
    n = len(maze[0])
    for i in range(m):
        for j in range(n):
            if ( i + 1 < m):
                if(maze[i + 1][j] == 5 and maze[i][j] == 0):
                    maze[i][j] = 5
            if ( i - 1 >= 0):
                if(maze[i - 1][j] == 5 and maze[i][j] == 0):
                    maze[i][j] = 5
            if ( j + 1 < n):
                if(maze[i][j + 1] == 5 and maze[i][j] == 0):
                    maze[i][j] = 5
            if ( j - 1 >= 0):
                if(maze[i][j - 1] == 5 and maze[i][j] == 0):
                    maze[i][j] = 5
    if(maze[m-1] [n-1] == 5):
        return True
    return False

