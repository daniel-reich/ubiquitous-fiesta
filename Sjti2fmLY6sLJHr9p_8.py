
from itertools import groupby
​
def look_and_say(start, n):
  output = [start]
  for _ in range(n-1):
    next_int = ""
    for k,g in groupby(str(output[-1])):
      next_int += str(sum(1 for _ in g)) + k
    output.append(int(next_int))
  return output

