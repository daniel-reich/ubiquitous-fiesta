
def exit_maze(maze, directions):
  i = 9
  j = 8
  for direction in directions:
    if direction == "N":
      i -= 1
    elif direction == "S":
      i += 1
    elif direction == "E":
      j += 1
    else:
      j -= 1
    if i < 0 or i > 9 or j < 0 or j > 9:
      return "Dead"
    elif maze[i][j] == 1:
      return "Dead"
    elif maze[i][j] == 3:
      return "Finish"
  return "Lost"

