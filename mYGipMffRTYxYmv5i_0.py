
from itertools import permutations
​
def simple_equation(a, b, c):
  for x, y, z in permutations((a, b, c)):
    for op in "+-*/":
      if eval("%d%s%d==%d" % (x, op, y, z)):
        return "%d%s%d=%d" % (x, op, y, z)
  return ""

