
import math
def triangle(perimeter,area):
  #c, b, a = math.ceil(perimeter / 3), math.ceil((perimeter - c) / 2), perimeter - (c + b)
  tri_list = []
  for c in range(math.ceil(perimeter / 3), math.floor(perimeter / 2) + 1):
    for b in range(math.ceil((perimeter - c) / 2), c + 1):
      a = perimeter - (c + b)
      p = perimeter / 2
      if (a + b + c == perimeter) and (float("%.5f" % (math.sqrt(p * (p - a) * (p - b) * (p - c)))) == area):
        tri_list.append([a, b, c])
  return tri_list

