
from math import sqrt, floor, ceil
​
def encryption(txt):
  txt = txt.replace(' ', '')
  l = len(txt)
  cols, rows = floor(sqrt(l)), ceil(sqrt(l))
  if cols * rows < l: cols += 1
  arr = [[' '] * cols for _ in range(rows)]
  for i in range(l):
    c, r = divmod(i, rows)
    arr[r][c] = txt[i]
  return ' '.join(''.join(row).rstrip() for row in arr)

