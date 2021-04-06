
import math
def largest_exponential(lst):
  a = []
  for i in lst:
    a.append((math.log10(i[0]))*i[1])
  return (a.index(max(a))+1)

