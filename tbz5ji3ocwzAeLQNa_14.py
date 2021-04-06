
def exit_maze(maze, directions):
  x, y = 9, 8
  for z in directions:
    x = x-1 if z=="N" else x+1 if z=="S" else x
    y = y-1 if z=="W" else y+1 if z=="E" else y 
    try:
      if [x,y] == [1, 1]:
        return "Finish"
      elif maze[x][y] == 1:
        return "Dead"
    except:
      return "Dead"
  return "Lost"

