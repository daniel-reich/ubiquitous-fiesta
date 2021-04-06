
def exit_maze(maze, directions):
  i,l=maze.index([x for x in maze if 2 in x][0]),len(maze)
  j=maze[i].index(2)
  for d in directions:
    if d in "NS":
      i+=(-1)**"SN".index(d)
    else:
      j+=(-1)**"EW".index(d)
    if i in [-1,l] or j in [-1,l]:
      return "Dead"
    elif maze[i][j] in [1,3]:
      return ["Dead","Finish"][maze[i][j]==3]
  return "Lost"

