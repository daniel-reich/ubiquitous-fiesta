
from math import ceil
def knight_bfs(a, x, b, y):
  s = abs(a-b) + abs(x-y)
  return s+2 if not (a ^ b and x ^ y) else ceil(s/2)-1

