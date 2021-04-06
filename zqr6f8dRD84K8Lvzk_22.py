
from itertools import chain
​
def hex_num(i):
  return i**3 - (i-1)**3
​
def hex_lattice(n):
  size = 1
  while hex_num(size) < n:
    size += 1
  if hex_num(size) != n:
    return "Invalid"
  w = 2 * size - 1
  row_size = 2 * w + 1
  out = []
  for i in chain(range(size, w + 1), range(w-1, size-1, -1)):
    row  = ' '.join(['o']*i)
    padding = ' '*((row_size - len(row))//2)
    out.append(padding + row + padding)
  return '\n'.join(out)

