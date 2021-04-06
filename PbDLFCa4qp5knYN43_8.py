
import sys
sys.setrecursionlimit(10000)
def triangle(n):
  if n <= 1:
    return 1
  else:
    return n + triangle(n-1)

