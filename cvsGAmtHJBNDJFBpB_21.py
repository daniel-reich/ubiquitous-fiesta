
from numpy import transpose
def can_traverse(x):
  x = transpose(list(reversed(x))).tolist()
  h = [row.index(0) for row in x]
  return all(abs(el - prev) <= 1 for el, prev in zip(h[1:], h) )

