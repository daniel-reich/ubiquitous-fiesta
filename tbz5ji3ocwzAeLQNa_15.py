
def exit_maze(maze, directions):
  global max_rows
  global max_cols
  max_rows = len(maze) - 1
  max_cols = len(maze[0]) - 1
  enu_maze = enumerate(maze)
​
  # Find the index of the 2
  for item in enu_maze:
    if 2 in item[1]:
      x = item[0] 
      y = item[1].index(2)
​
  # Check each move
  for move in directions:
    if move == 'N':
      x -= 1
      ans = check_move(x, y, maze)
    elif move == 'E':
      y += 1
      ans = check_move(x, y, maze)
    elif move == 'S':
      x += 1
      ans = check_move(x, y, maze)
    elif move == 'W':
      y -= 1
      ans = check_move(x, y, maze)
    if ans == 'Dead':
      return 'Dead'
    if ans != 'continue':
      return ans
  else:
    return 'Lost'
​
def check_move(a, b, m):
  if a < 0 or b < 0 or a > max_rows or b > max_cols:
    return 'Dead'
  if m[a][b] == 3:
    return 'Finish'
  elif m[a][b] == 1:
    return "Dead"
  else:
    return 'continue'

