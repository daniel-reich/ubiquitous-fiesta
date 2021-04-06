
from numpy import equal
​
def is_checkerboard(lst):
  for i in range(0, len(lst) - 1):
    if any(list(map(equal, lst[i], lst[i + 1]))):
      return False
  for i in range(0, len(lst) - 1):
    if any(list(map(equal, lst[:][i], lst[:][i + 1]))):
      return False
  return True

