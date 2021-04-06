
def exit_maze(maze, directions):
  def helper(start):
    ns = {'N': -1, 'S': 1}
    we = {'W': -1, 'E': 1}
    for d in directions:
      x, y = start[0]+ ns.get(d, 0), start[1]+ we.get(d, 0)
      try:
        local = maze[x][y]
        start[0], start[1] = x, y
        if local == 3:
          return 'Finish'
        elif local == 1:
          return 'Dead'
      except IndexError:
        return 'Dead'
    return 'Lost'
  
  start = []
  for x, lst in enumerate(maze):
    for y, item in enumerate(lst):
      if item == 2:
        start = [x, y]
        return helper(start)

