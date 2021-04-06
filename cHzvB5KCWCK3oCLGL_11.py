
from collections import defaultdict
def game_of_life(board):
  matrix = defaultdict(int)
  imax, jmax = 0, 0
  for j, line in enumerate(board):
    jmax = max(jmax,j)
    for i, char in enumerate(line):
      imax = max(imax,i)
      matrix[(i,j)] = char
  board2 = "\n".join(["".join([next_life((i,j),matrix) for i in range(imax+1)]) for j in range(jmax+1)])
  return board2
​
def next_life(coord, matrix):
  shifts = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
  neigbo = sum([matrix[(coord[0]+shift[0],coord[1]+shift[1])] for shift in shifts])
  if matrix[coord] == 1 and (neigbo == 2 or neigbo == 3):
    return "I"
  if matrix[coord] == 0 and neigbo == 3:
    return "I"
  return "_"

