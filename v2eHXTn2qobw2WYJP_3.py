
from collections import defaultdict
def minesweeper_numbers(board):
  cells = {(i,j) : char
            for i, line in enumerate(board)
            for j, char in enumerate(line)}
  cells_e = defaultdict(lambda: 0)
  for coord in cells.keys():
    cells_e[coord] = cells[coord] 
  shifts = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
  res = dict()
  for (coord) in cells.keys():
    if cells[coord] == 1:
      res[coord] = 9
    else:
      res[coord] = sum([cells_e[(coord[0]+shift[0],coord[1]+shift[1])]
       for shift in shifts])
  res2 = []
  for i, line in enumerate(board):
    row =[]
    for j, char in enumerate(line):
      row.append(res[i,j])
    res2.append(row)
  return res2
        
​
​
​
​
print(minesweeper_numbers([
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1]
]))

