
import math
def fp_eq(n1, n2):
  return abs(n1 - n2) < 0.00001
​
def triangle(perimeter,area):
  res = []
  s = perimeter / 2
  test = area ** 2 / s
  for a in range(1, (perimeter // 3) + 1):
    for b in range(max(a, math.ceil(perimeter / 2 - a)), ((perimeter - a) // 2) + 1):
      c = perimeter - a - b
      val = (s-a)*(s-b)*(s-c)
      if fp_eq(val, test):
        res.append([a, b, c])
  return res

