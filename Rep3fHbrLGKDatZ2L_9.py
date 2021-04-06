
from re import findall
​
def complete_pattern(p):
  c = list(set(p.replace('_', '')))
  n, x, y, k = len(c), 'x', 'y', 0
  while x != y:
    x, y = findall(r'(?:.{'+str(n)+'})', p.replace('_', c[k]))[:2]
    if x == y and 4 * len(x) <= len(p):
      if p.replace('_', c[k])[:4*len(x)] == 2 * (x + y): break
      x, y = 'x', 'y'
    k += 1
    if k == len(c): k, n = 0, n + 1
  return ((x+y)*(len(p)//len(x)))[p.index('_')]

