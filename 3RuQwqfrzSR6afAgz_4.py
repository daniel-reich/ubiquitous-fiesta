
import itertools as it
​
def rail_fence_cipher(s, r):
  res, rows = ['']*r, list(range(r))
  cycle = it.cycle(rows + rows[::-1][1:-1])
  
  for row, i in zip(cycle, s):
    res[row] += i
    
  return ''.join(res)

