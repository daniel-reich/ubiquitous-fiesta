
def exit_maze(maze, directions):
  for i in maze:
    if 2 in i: r,c= maze.index(i),i.index(2)
  
  for i in directions:
    if i=='N': r -=1
    if i=='S': r +=1
    if i=='W': c -=1
    if i=='E': c +=1
    try:
      if maze[r][c] == 1: return 'Dead'
      if maze[r][c] == 3: return 'Finish'
    except:
      return 'Dead'
  
  return 'Lost'

