
from collections import deque
def check(l):
  t = deque(sorted(l))
  if list(t)==l: return 'NO'
  for i in range(len(l)):
    t.rotate(-1)
    if list(t)==l: return 'YES'
  return 'NO'

