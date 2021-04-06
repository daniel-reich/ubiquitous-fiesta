
def exit_maze(maze, directions):
  for x in range(len(maze)):
    for y in range(len(maze[x])):
      if maze[x][y]==2:
        start=[x,y]
      elif maze[x][y]==3:
        end = [x,y]
  for i in directions:
    x,y = 0,0
    if i=='N': x=-1
    elif i=='E': y=1
    elif i=='S': x=1
    elif i=='W': y=-1
    start=[start[0]+x,start[1]+y]
    if start[0]<0 or start[0]>=len(maze) or start[1]<0 or start[1]>len(maze[0]):
      return 'Dead'
    elif maze[start[0]][start[1]]==1:
      return 'Dead'
    elif start==end:
      return 'Finish'
  return 'Lost'

