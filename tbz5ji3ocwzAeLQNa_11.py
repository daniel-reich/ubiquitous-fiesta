
def Starting_Point(maze):
  for i in range(len(maze)):
    for j in range(len(maze)):
      if maze[i][j] == 2:
        return j,i
        
​
def exit_maze(maze, directions):
  col , line = Starting_Point(maze)
  
  for moves in directions:
    if   moves == "N": line-=1
    elif moves == "S": line+=1
    elif moves == "W": col-=1
    else: col+=1
    if line > len(maze)-1 or col > len(maze)-1:return 'Dead'
    if maze[line][col]   == 1:return 'Dead'
    elif maze[line][col] == 3:return 'Finish'
  
  return 'Lost'

