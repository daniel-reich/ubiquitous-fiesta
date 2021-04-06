
def exit_maze(maze, directions):
  D = {'N':(-1,0), 'S':(1,0), 'E':(0,1), 'W':(0,-1)}
  board_height, board_width = range(len(maze)), range(len(maze[0]))
  r, c = get_start_pos(maze)
  for d in directions:
    dr, dc = D[d]
    r, c = r+dr, c+dc
    if r not in board_width or c not in board_height or maze[r][c] == 1:
      return 'Dead'
    if maze[r][c] == 3:
      return 'Finish'
  return 'Lost'
    
def get_start_pos(maze):
  for r, row in enumerate(maze):
    for c, p in enumerate(row):
      if p == 2:
        return r, c

