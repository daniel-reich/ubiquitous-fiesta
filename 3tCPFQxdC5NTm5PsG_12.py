
from itertools import combinations
from math import hypot
def is_isosceles(lst):
  lines = list(map(lambda x: hypot(x[0][0] - x[1][0],x[0][1]-x[1][1]),list(combinations(lst,2))))
  return len(set(lines)) == 2 and sum(sorted(lines)[:2]) > max(lines)
def find_triangles(lst):
  return len(list(filter(lambda x: is_isosceles(x),list(combinations(lst,3)))))

