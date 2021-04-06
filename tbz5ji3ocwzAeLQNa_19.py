
def exit_maze(maze, directions):
  start_row = 9
  start_col = 8
  try:
    for eachdirection in directions:
      if maze[start_row][start_col] == 1:
        return 'Dead'
      if maze[start_row][start_col] == 3:
        return 'Finish'
      if eachdirection == 'N':
        start_row -= 1
      elif eachdirection == 'W':
        start_col -= 1
      elif eachdirection == 'E':
        start_col += 1
      elif eachdirection == 'S':
        start_row += 1
    if maze[start_row][start_col] == 3:
      return 'Finish'
    elif maze[start_row][start_col] == 1:
      return 'Dead'
    else:
      return 'Lost'
  except:
    return 'Dead'

