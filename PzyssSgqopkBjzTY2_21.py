
def can_exit(maze):
  if maze[0][0]!=0:
    return False
  row = 0
  column = 0
  while True:
    if row==len(maze)-1 and column==len(maze[0])-1:
      return True
    maze[row][column] = 2
    if row > 0 and maze[row-1][column]==0:
      row -= 1
    elif column < len(maze[0])-1 and maze[row][column+1]==0:
      column += 1
    elif row < len(maze)-1 and maze[row+1][column]==0:
      row += 1
    elif column > 0 and maze[row][column-1]==0:
      column -= 1
    else:
      all_dead_ends = 1
      for i in range (len(maze)):
        if all_dead_ends==0:
          break
        for j in range (len(maze)):
          if maze[i][j]==2 and ((i > 0 and maze[i-1][j]==0) or (i < len(maze)-1 and maze[i+1][j]==0) or (j > 0 and maze[i][j-1]==0) or (j < len(maze[0])-1 and maze[i][j+1]==0)):
            row = i
            column = j
            all_dead_ends = 0
            break
      else:
        return False

