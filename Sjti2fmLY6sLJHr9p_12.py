
from itertools import groupby
def look_and_say(start, n):
  lst = [start]
  start = str(start)
  for _ in range(1,n):
    start = "".join([str(len(list(g)))+k for k,g in groupby(start)])
    lst.append(int(start))
  return (lst)

