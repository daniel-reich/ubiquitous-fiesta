
import copy
​
def game_of_life(g):
  results = copy.deepcopy(g)
  rows, columns = len(g), len(g[0])
​
  neighbours = {(-1, 1), (0, 1), (1, 1), (-1, 0), 
        (1, 0), (-1, -1), (0,-1), (1,-1)}
​
  for row in range(rows):
    for col in range(columns):
      value = g[row][col]
      total = 0
      for a, b in neighbours:
         if row + a not in (-1, rows) and col + b not in (-1, columns):
            total += g[row+a][col+b]
      if value == 1 and total not in (2, 3):
        results[row][col] = 0
      elif value == 0 and total == 3:
        results[row][col] = 1
  return '\n'.join(''.join(str(v) for v in row) for row in results).replace('0', '_').replace('1', 'I')

