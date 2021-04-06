
def exit_maze(maze, directions):
  end = 0
  start = 0
  for i in range(len(maze)):
    for j in range(len(maze[0])):
      if maze[i][j]==3:
        end = [i,j]
      if maze[i][j]==2:
        start = [i,j]
  for i in directions:
    print(start,i)
    if i=='N' and start[0]==0 or i=='S' and start[0]==len(maze)-1 or i=='W' and start[1]==0 or i=='S' and start[1]==len(maze[0])-1:
      return 'Dead'
    else:
      if i=='N':
        start[0]-=1
      elif i=='S':
        start[0]+=1
      elif i=='W':
        start[1]-=1
      else:
        start[1]+=1
      if maze[start[0]][start[1]]==1:
        return 'Dead'
      if start==end:
        return 'Finish'
  return 'Lost'

