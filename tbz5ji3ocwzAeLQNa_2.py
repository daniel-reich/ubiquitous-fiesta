
def exit_maze(maze, directions):
  for i in range(len(maze)):
    if 2 in maze[i]: y, x = i, maze[i].index(2)
  for i in directions:
    if i == "N": y-=1
    if i == "S": y+=1 
    if i == "E": x+=1 
    if i == "W": x-=1
    if max(x,y) > 9 or min(x,y) < 0:
      return "Dead"
    if maze[y][x] == 1: 
      return "Dead"
    if maze[y][x] == 3: 
      return "Finish"
  return "Finish" if maze[y][x] == 3 else "Lost"

