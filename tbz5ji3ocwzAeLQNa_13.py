
def exit_maze(maze, directions):
​
  row, column = 9, 8
  current_num = maze[row][column]
​
  for d in directions:
    if d == "N" or d == "S":
      row += -1 if d == "N" else 1
    else:
      column += -1 if d == "W" else 1
​
    if row > 9 or column > 9 or row < 0 or column < 0:
      return "Dead"
    else:
      current_num = maze[row][column]
      if current_num == 1:
        return "Dead"
      elif current_num == 3:
        return "Finish"
​
  return "Finish" if current_num == 3 else "Lost"

