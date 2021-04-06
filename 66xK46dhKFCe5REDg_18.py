
def x_and_o(board):
  brd = [r.replace('|', '') for r in board]
  lines = [ [(0,0),(0,1),(0,2)], [(1,0),(1,1),(1,2)], [(2,0),(2,1),(2,2)], [(0,0),(1,1),(2,2)], 
      [(0,0),(1,0),(2,0)], [(0,1),(1,1),(2,1)], [(0,2),(1,2),(2,2)], [(0,2),(1,1),(2,0)] ]
  for line in lines:
    l = ''.join(brd[r][c] for r, c in line)
    if l.count('X') == 2 and l.count(' ') == 1: 
      r,c = line[l.index(' ')]
      return [r+1, c+1]
  return False

