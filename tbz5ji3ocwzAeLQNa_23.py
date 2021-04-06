
def exit_maze(maze, directions):
  dirs,lm,lm0 = {'N':(-1,0),'E':(0,1),'S':(1,0),'W':(0,-1)},len(maze),len(maze[0])
  for i in range(lm):
    for j in range(lm0):
      if maze[i][j] == 2:
        a,b = i,j
  for d in directions:
    x,y = dirs[d]
    i,j = a+x,b+y
    if not 0 <= i < lm or not 0 <= j < lm0 or maze[i][j] == 1:
      return "Dead"
    elif maze[i][j] == 3:
      return "Finish"
    a,b = i,j
  return 'Lost'

