
from re import findall
​
def find_vertex(x):
  a, b, c = findall('-?\d+', x)
  a, b = int(a), int(b)
  return -b // (2 * a)

