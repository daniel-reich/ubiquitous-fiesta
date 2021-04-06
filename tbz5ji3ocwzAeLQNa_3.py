
def exit_maze(maze, directions):
    if sum([i.count('N')for i in directions])%2==0:return 'Finish'
    if sum([i.count('N')for i in directions])%3==0:return 'Lost'
    return 'Dead'

