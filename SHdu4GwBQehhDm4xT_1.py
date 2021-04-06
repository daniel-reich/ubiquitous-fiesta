
from itertools import groupby
​
def freed_prisoners(prison):
  freed = [k for k, _ in groupby(prison)]
  return len(freed) if freed[0] == 1 else 0

